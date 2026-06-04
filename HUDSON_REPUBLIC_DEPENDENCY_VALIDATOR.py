#!/usr/bin/env python3

import os
import re
import subprocess
import argparse
from collections import defaultdict

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

# Explicitly Allowed Field 1 Types based on Directory Routing
VALID_FIELD_1 = ["CA", "CO", "EL", "EB", "FO", "LA", "LB", "OP", "SCH"]

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


def parse_fqln(fqln):
    """Parse FQLN into TYPE, SUBJECT, DATE components."""
    parts = fqln.split('_')
    if len(parts) != 3:
        return None, None, None
    ftype = parts[0]
    fsubject = parts[1]
    fdate = parts[2]
    return ftype, fsubject, fdate


def index_repository(root_dir):
    """
    Pass 1: Crawl the repository and build registry.
    Only processes files recursively inside the 'laws' directory.
    Enforces that all written legislation is markdown (.md) only.
    """
    registry = {}
    subject_map = defaultdict(list)   # SUBJECT -> list of FQLNs for uniqueness check
    indexing_errors = []

    for root, dirs, files in os.walk(root_dir):
        path_parts = [p.lower() for p in root.split(os.sep)]

        # Only index files under the 'laws' directory
        if 'laws' not in path_parts:
            continue

        # Skip git and template directories
        if '.git' in root or 'templates' in path_parts:
            continue

        # Capture the immediate parent directory name for validation
        parent_dir = os.path.basename(root)

        for file in files:
            # Explicit exception for gitkeep/placeholder files
            if file == "remove_me":
                continue

            filepath = os.path.join(root, file)

            # Strictly enforce .md format inside laws/docs/
            if 'docs' in path_parts:
                if not file.endswith(".md"):
                    indexing_errors.append(f"[{file}] FORMAT ERROR: All written legislation must be in the markdown (.md) format only.")
                    continue

            if file.endswith(".md"):
                fqln = file.replace(".md", "")

                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read()

                    # Determine precise type for CA documents
                    base_type = fqln.split('_')[0]
                    precise_type = base_type
                    if base_type == "CA":
                        weight_match = re.search(r"This article is designated as:\s*\*\*(Bedrock|Foundational)\*\*",
                                               content, re.IGNORECASE)
                        precise_type = f"CA_{weight_match.group(1).upper()}" if weight_match else "CA_FOUNDATIONAL"

                    # Extract Hard Dependencies
                    deps = []
                    dep_sections = re.findall(r"## Hard Dependencies\r?\n(.*?)(?=\r?\n---|\Z)", content, re.DOTALL)
                    for section in dep_sections:
                        deps.extend(re.findall(r"\[([A-Z0-9_]+)\]", section))
                    deps = list(dict.fromkeys(deps))  # Remove duplicates

                    registry[fqln] = {
                        "filepath": filepath,
                        "base_type": base_type,
                        "precise_type": precise_type,
                        "deps": deps,
                        "parent_dir": parent_dir
                    }

                    # Track SUBJECT for uniqueness validation
                    _, subject, _ = parse_fqln(fqln)
                    if subject:
                        subject_map[subject].append(fqln)

                except Exception:
                    continue

    return registry, subject_map, indexing_errors


def lint_registry(registry, subject_map, indexing_errors):
    """Pass 2: Validate dependencies and enforce FQLN/Path constraints."""
    errors = indexing_errors.copy()
    audit_flags = []

    # === CIRCULAR DEPENDENCY VALIDATION ===
    visited = {}
    path = []

    def dfs(node):
        if node not in registry:
            return
        if visited.get(node) == 1:
            # Cycle detected
            cycle_start = path.index(node)
            cycle_nodes = path[cycle_start:] + [node]
            errors.append(f"[{node}] CIRCULAR DEPENDENCY DETECTED: {' -> '.join(cycle_nodes)}")
            return
        if visited.get(node) == 2:
            return

        visited[node] = 1
        path.append(node)

        for neighbor in registry[node]["deps"]:
            dfs(neighbor)

        path.pop()
        visited[node] = 2

    # Run the Depth-First Search over the registry
    for fqln in registry:
        if visited.get(fqln, 0) == 0:
            dfs(fqln)

    # === FQLN SUBJECT UNIQUENESS VALIDATION ===
    for subject, fqlns in subject_map.items():
        if len(fqlns) > 1:
            errors.append(f"SUBJECT COLLISION: The SUBJECT '{subject}' is used by multiple instruments: {', '.join(fqlns)}. "
                          f"Field 2 (SUBJECT) must be unique within the laws directory at any given time.")

    for fqln, data in registry.items():
        doc_type = data["precise_type"]
        doc_base = data["base_type"]
        current_tier = TIERS.get(doc_type, 0)
        current_date = extract_date_from_fqln(fqln)
        parent_dir = data["parent_dir"]

        # === STRICT FQLN FIELD & PATH VALIDATION ===
        parts = fqln.split('_')
        if len(parts) != 3:
            errors.append(f"[{fqln}] FQLN FORMAT ERROR: Must contain exactly 3 fields separated by underscores.")
        else:
            f_type, f_subject, f_date = parts

            # Field 1: Allowed List and Uppercase Alpha only
            if f_type not in VALID_FIELD_1:
                errors.append(f"[{fqln}] FQLN FIELD 1 ERROR: Type '{f_type}' is invalid. Allowed types are: {', '.join(VALID_FIELD_1)}.")
            if not f_type.isalpha() or not f_type.isupper() or len(f_type) > 4:
                errors.append(f"[{fqln}] FQLN FIELD 1 ERROR: Type '{f_type}' must be UPPERCASE alpha-only and cannot exceed 4 characters.")

            # Field 2: Uppercase Alpha only, <= 64 chars
            if not f_subject.isalpha() or not f_subject.isupper() or len(f_subject) > 64:
                errors.append(f"[{fqln}] FQLN FIELD 2 ERROR: Subject '{f_subject}' must be UPPERCASE alpha-only and cannot exceed 64 characters.")

            # Field 3: Numeric only, minimum 8 and maximum 16 characters
            if not f_date.isnumeric() or len(f_date) < 8 or len(f_date) > 16:
                errors.append(
                    f"[{fqln}] FQLN FIELD 3 ERROR: Date '{f_date}' must be numeric-only "
                    f"and must be between 8 and 16 characters in length."
                )

            # Strict Path Evaluation (laws/docs/[FIELD 1]/[FQLN].md)
            expected_path_suffix = os.path.normpath(f"laws/docs/{f_type}/{fqln}.md")
            actual_path = os.path.normpath(data["filepath"])
            if not actual_path.endswith(expected_path_suffix):
                 errors.append(f"[{fqln}] DIRECTORY ERROR: Legislation must be located exactly at {expected_path_suffix}.")

        # Rule: LC and CULT have NO dependencies
        if doc_base in ["LC", "CULT"] and len(data["deps"]) > 0:
            errors.append(f"[{fqln}] VIOLATION: {doc_base} instruments shall have no dependencies.")

        # GENESIS NODE PROTECTIONS
        if fqln == ROOT_CONSTITUTION and len(data["deps"]) > 0:
            errors.append(f"[{fqln}] GENESIS VIOLATION: The Individual Act ({ROOT_CONSTITUTION}) shall have no dependencies.")

        # All substantive instruments must depend on The Individual Act
        substantive_bases = ["CA", "LA", "CO", "OP", "LB", "EB", "EL"]
        if doc_base in substantive_bases and fqln != ROOT_CONSTITUTION:
            if ROOT_CONSTITUTION not in data["deps"]:
                errors.append(f"[{fqln}] SOVEREIGNTY VIOLATION: Instrument must explicitly list [{ROOT_CONSTITUTION}] as a Hard Dependency.")

        # All CA must depend on Clarity Act
        if doc_base == "CA" and fqln not in [ROOT_CONSTITUTION, CLARITY_ACT]:
            if CLARITY_ACT not in data["deps"]:
                errors.append(f"[{fqln}] CLARITY VIOLATION: Constitutional Articles must explicitly list [{CLARITY_ACT}] as a Hard Dependency.")

        # Dependency tier and type validation
        for dep_fqln in data["deps"]:
            if dep_fqln not in registry:
                errors.append(f"[{fqln}] NOTICE: Dependency {dep_fqln} not found in repository.")
                continue

            dep_type = registry[dep_fqln]["precise_type"]
            dep_base = registry[dep_fqln]["base_type"]
            dep_tier = TIERS.get(dep_type, 0)
            dep_date = extract_date_from_fqln(dep_fqln)

            # Template compliance
            allowed = ALLOWED_DEPENDENCIES.get(doc_base)
            if allowed is not None and dep_base not in allowed:
                errors.append(f"[{fqln}] TEMPLATE VIOLATION: {doc_base} may only depend on {allowed}. Found: {dep_base}.")

            # Tier compliance
            if dep_tier < current_tier:
                errors.append(f"[{fqln}] DOWNWARD DEPENDENCY: {doc_type} (Tier {current_tier}) illegally depends on {dep_type} (Tier {dep_tier}).")

            # Bedrock restriction
            if doc_type == "CA_BEDROCK" and dep_type != "CA_BEDROCK":
                errors.append(f"[{fqln}] BEDROCK VIOLATION: Bedrock CAs may only depend on other Bedrock CAs.")

            # Temporal Inversion Audit
            if dep_date > current_date and current_date != 0 and dep_date != 0:
                audit_msg = (
                    f"⚠️  HIGH-SCRUTINY CRYPTOGRAPHIC AUDIT FLAG: TEMPORAL INVERSION\n"
                    f"    -> Instrument: {fqln}\n"
                    f"    -> Target:     {dep_fqln}\n"
                    f"    -> DVCS Data:  {get_git_commit_data(data['filepath'])}\n"
                )
                audit_flags.append(audit_msg)

    return errors, audit_flags


def main():
    parser = argparse.ArgumentParser(description="Hudson Republic Federated Validator (v3.8 - Full Structuring & Cycle Detection)")
    parser.add_argument("--audit", action="store_true", help="Display high-scrutiny temporal audit flags.")
    args = parser.parse_args()

    sync_submodules()
    print("Indexing federated repository (laws directory only)...")

    registry, subject_map, indexing_errors = index_repository(".")
    print(f"Indexed {len(registry)} instruments across the laws directory.")

    errors, audit_flags = lint_registry(registry, subject_map, indexing_errors)

    if args.audit and audit_flags:
        print("\n" + "="*80)
        print("=== FEDERATED AUDIT LOG: SECURITY & COMPLIANCE FLAGS ===")
        print("="*80)
        for flag in audit_flags:
            print(flag)
        print("="*80 + "\n")

    if errors:
        for error in errors:
            print(error)
        exit(1)

    print("BUILD PASSED: The Federation is secure.")


if __name__ == "__main__":
    main()
