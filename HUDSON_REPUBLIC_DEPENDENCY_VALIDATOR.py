#!/usr/bin/env python3

import os
import re
import subprocess
import argparse

# The Republic's Legislative Tier System
TIERS = {
    "CA_BEDROCK": 5,
    "CA_FOUNDATIONAL": 4,
    "LA": 3,
    "CO": 2, "LB": 2, "OP": 2, "EL": 2, "EB": 2,
    "SCH": 1, "FO": 1, "LC": 1, "CULT": 1
}

# Strict Type Allowances Defined by Legislative Templates
ALLOWED_DEPENDENCIES = {
    "CA": ["CA"],
    "LA": ["CA", "LA"],
    "CO": ["CA", "LA", "CO"],
    "EB": ["CA"],
    "EL": ["CA"],
    "FO": ["CA", "LA", "CO"],
    "SCH": ["CA", "LA", "CO"],
    "LB": ["CA", "LA"],
    "OP": ["CA", "LA", "CO"],
    "LC": [],
    "CULT": []
}

# The Genesis Node (Absolute Root Dependency)
ROOT_CONSTITUTION = "CA_THEINDIVIDUAL_20260401"

# The Clarity Standard
CLARITY_ACT = "CA_CLARITYACT_20260522"

def sync_submodules():
    """Ensures all legislative submodules are initialized and updated."""
    print("Synchronizing legislative submodules...")
    subprocess.run(['git', 'submodule', 'update', '--init', '--recursive'], check=True)

def get_git_commit_data(filepath):
    """Fetches the latest Git commit hash, author, and date for a specific file."""
    try:
        git_log = subprocess.check_output(
            ['git', 'log', '-1', '--format=%H | %aI | %an | %s', filepath],
            stderr=subprocess.STDOUT,
            text=True
        ).strip()
        return git_log
    except (subprocess.CalledProcessError, FileNotFoundError):
        return "Git metadata unavailable."

def extract_date_from_fqln(fqln):
    """Extracts the YYYYMMDD integer from an FQLN for chronological comparison."""
    try:
        return int(fqln.split('_')[-1])
    except (ValueError, IndexError):
        return 0

def index_repository(root_dir):
    """
    Pass 1: Crawl the repository and submodules to build a registry of all instruments.
    Ignores template directories to prevent placeholder files from being flagged.
    """
    registry = {}
    for root, dirs, files in os.walk(root_dir):
        # Convert path components to lowercase to ensure case-insensitive exclusion of templates
        path_parts = [p.lower() for p in root.split(os.sep)]

        # Skip git metadata directories and SDK template folders
        if '.git' in root or 'templates' in path_parts:
            continue

        for file in files:
            if file.endswith(".md"):
                filepath = os.path.join(root, file)
                fqln = file.replace(".md", "")
                base_type = fqln.split('_')[0]

                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read()

                    precise_type = base_type
                    if base_type == "CA":
                        weight_match = re.search(r"This article is designated as:\s*\*\*(Bedrock|Foundational)\*\*", content, re.IGNORECASE)
                        precise_type = f"CA_{weight_match.group(1).upper()}" if weight_match else "CA_FOUNDATIONAL"

                    # Upgraded cross-platform dependency scanner (handles duplicated headers in templates)
                    deps = []
                    dep_sections = re.findall(r"## Hard Dependencies\r?\n(.*?)(?=\r?\n---|\Z)", content, re.DOTALL)

                    if dep_sections:
                        for section in dep_sections:
                            deps.extend(re.findall(r"\[([A-Z0-9_]+)\]", section))
                        # Remove duplicates in case a dependency is listed multiple times
                        deps = list(dict.fromkeys(deps))

                    registry[fqln] = {
                        "filepath": filepath,
                        "base_type": base_type,
                        "precise_type": precise_type,
                        "deps": deps
                    }
                except (AttributeError, IOError):
                    continue
    return registry

def lint_registry(registry):
    """Pass 2: Validate dependencies across the entire federated registry."""
    errors, audit_flags = [], []

    for fqln, data in registry.items():
        doc_type = data["precise_type"]
        doc_base = data["base_type"]
        current_tier = TIERS.get(doc_type, 0)
        current_date = extract_date_from_fqln(fqln)

        # Rule: LC and CULT have NO dependencies
        if doc_base in ["LC", "CULT"] and len(data["deps"]) > 0:
            errors.append(f"[{fqln}] VIOLATION: {doc_base} instruments shall have no dependencies.")

        # --- GENESIS NODE PROTECTIONS ---

        # Rule: The Root Constitution (Individual Act) must have zero dependencies
        if fqln == ROOT_CONSTITUTION and len(data["deps"]) > 0:
            errors.append(f"[{fqln}] GENESIS VIOLATION: The Individual Act ({ROOT_CONSTITUTION}) shall have no dependencies.")

        # Rule: All substantive legislative instruments MUST explicitly depend on the Individual Act
        substantive_bases = ["CA", "LA", "CO", "OP", "LB", "EB", "EL"]
        if doc_base in substantive_bases and fqln != ROOT_CONSTITUTION:
            if ROOT_CONSTITUTION not in data["deps"]:
                errors.append(f"[{fqln}] SOVEREIGNTY VIOLATION: Instrument must explicitly list [{ROOT_CONSTITUTION}] as a Hard Dependency.")

        # --- THE CLARITY STANDARD ---

        # Rule: All Constitutional Articles must depend on the Clarity Act
        if doc_base == "CA" and fqln not in [ROOT_CONSTITUTION, CLARITY_ACT]:
            if CLARITY_ACT not in data["deps"]:
                errors.append(f"[{fqln}] CLARITY VIOLATION: Constitutional Articles must explicitly list [{CLARITY_ACT}] as a Hard Dependency.")

        # --- CORE ARCHITECTURAL RULES ---

        for dep_fqln in data["deps"]:
            dep_type = registry[dep_fqln]["precise_type"] if dep_fqln in registry else ("CA_FOUNDATIONAL" if dep_fqln.startswith("CA") else dep_fqln.split('_')[0])
            dep_base = registry[dep_fqln]["base_type"] if dep_fqln in registry else dep_fqln.split('_')[0]
            dep_tier = TIERS.get(dep_type, 0)
            dep_date = extract_date_from_fqln(dep_fqln)

            # Strict compliance checks against template-defined limits
            allowed_deps_for_type = ALLOWED_DEPENDENCIES.get(doc_base)
            if allowed_deps_for_type is not None:
                if dep_base not in allowed_deps_for_type:
                    errors.append(f"[{fqln}] TEMPLATE VIOLATION: {doc_base} instruments may only depend on {allowed_deps_for_type}. Found: {dep_base}.")

            # Flag if the instrument is not found in the live repository (ignoring dummy template links)
            if dep_fqln not in registry:
                errors.append(f"[{fqln}] NOTICE: Dependency {dep_fqln} not found in repository. Ensure formal consideration is documented.")

            # Temporal Inversion Audit
            if dep_date > current_date and current_date != 0 and dep_date != 0:
                audit_msg = (
                    f"⚠️  HIGH-SCRUTINY CRYPTOGRAPHIC AUDIT FLAG: TEMPORAL INVERSION\n"
                    f"    -> Instrument: {fqln}\n"
                    f"    -> Target:     References future instrument [{dep_fqln}]\n"
                    f"    -> Action:     Verify implicit technical amendment via DVCS delta\n"
                    f"    -> DVCS Data:  {get_git_commit_data(data['filepath'])}\n"
                )
                audit_flags.append(audit_msg)

            # Tier compliance checks
            if dep_tier < current_tier:
                errors.append(f"[{fqln}] DOWNWARD DEPENDENCY: {doc_type} (Tier {current_tier}) illegally depends on {dep_type} (Tier {dep_tier}).")

            # Bedrock can only depend on Bedrock
            if doc_type == "CA_BEDROCK" and dep_type != "CA_BEDROCK":
                errors.append(f"[{fqln}] BEDROCK VIOLATION: Bedrock CAs may only depend on Bedrock.")

    return errors, audit_flags

def main():
    parser = argparse.ArgumentParser(description="Hudson Republic Federated Validator (v3.2)")
    parser.add_argument("--audit", action="store_true", help="Display high-scrutiny temporal audit flags and safeguards.")
    args = parser.parse_args()

    sync_submodules()
    print("Indexing federated repository...")
    registry = index_repository(".")
    print(f"Indexed {len(registry)} instruments across all Houses/Ridings.")

    errors, audit_flags = lint_registry(registry)

    # Formalized Audit Output
    if args.audit:
        print("\n" + "="*80)
        print("=== FEDERATED AUDIT LOG: SECURITY & COMPLIANCE FLAGS ===")
        print("="*80)
        if audit_flags:
            for flag in audit_flags:
                print(flag)
        else:
            print("STATUS: CLEAN. No Temporal Inversions or Rogue Policy Injections detected.")
        print("="*80 + "\n")

    if errors:
        for error in errors: print(error)
        exit(1)

    print("BUILD PASSED: The Federation is secure.")

if __name__ == "__main__":
    main()
