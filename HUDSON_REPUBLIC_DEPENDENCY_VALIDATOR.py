#!/bin/env python

import os
import re

# The Republic's Legislative Tier System
# Bedrock is placed at Tier 5 to ensure Foundational (Tier 4) cannot force upward dependencies onto it.
TIERS = {
    "CA_BEDROCK": 5,
    "CA_FOUNDATIONAL": 4,
    "LA": 3,
    "CO": 2, "LB": 2, "OP": 2, "EL": 2, "EB": 2,
    "SCH": 1, "FO": 1, "LC": 1
}

def index_repository(laws_dir):
    """Pass 1: Crawl the repository and build a registry of all instruments."""
    registry = {}
    for root, dirs, files in os.walk(laws_dir):
        for file in files:
            if file.endswith(".md"):
                filepath = os.path.join(root, file)
                fqln = file.replace(".md", "")
                base_type = fqln.split('_')[0]

                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()

                # Default to base type
                precise_type = base_type

                # Detect Bedrock vs Foundational for CAs
                if base_type == "CA":
                    weight_match = re.search(r"This article is designated as:\s*\*\*(Bedrock|Foundational)\*\*", content, re.IGNORECASE)
                    if weight_match:
                        precise_type = f"CA_{weight_match.group(1).upper()}"
                    else:
                        print(f"WARNING: {fqln} is missing a valid Constitutional Weight declaration.")
                        precise_type = "CA_FOUNDATIONAL" # Safe Fallback

                # Extract Dependencies
                deps = []
                dep_match = re.search(r"## Hard Dependencies\n.*?\n\n(.*?)\n\n---", content, re.DOTALL)
                if dep_match:
                    deps_text = dep_match.group(1)
                    deps = re.findall(r"\[([A-Z0-9_]+)\]", deps_text)

                registry[fqln] = {
                    "filepath": filepath,
                    "base_type": base_type,
                    "precise_type": precise_type,
                    "deps": deps
                }
    return registry

def lint_registry(registry):
    """Pass 2: Validate dependencies against the Naming Conventions Act."""
    errors = []

    for fqln, data in registry.items():
        doc_type = data["precise_type"]
        doc_base = data["base_type"]
        current_tier = TIERS.get(doc_type, 0)

        # Rule: LC has NO dependencies (Section 2.3.5)
        if doc_base == "LC" and len(data["deps"]) > 0:
            errors.append(f"[{fqln}] VIOLATION: Legislative Challenges (LC) shall have no dependencies.")

        # Rule: FO and SCH should be limited to 1-2 parents to prevent inheritance collisions
        if doc_base in ["FO", "SCH"] and len(data["deps"]) > 2:
            errors.append(f"[{fqln}] WARNING: {doc_base} files typically should not exceed 2 dependencies.")

        for dep_fqln in data["deps"]:
            # Resolve dependency type by checking the registry mapping
            if dep_fqln in registry:
                dep_type = registry[dep_fqln]["precise_type"]
                dep_base = registry[dep_fqln]["base_type"]
            else:
                # If dependency file doesn't exist yet, guess based on prefix
                dep_base = dep_fqln.split('_')[0]
                dep_type = "CA_FOUNDATIONAL" if dep_base == "CA" else dep_base
                errors.append(f"[{fqln}] NOTICE: Dependency {dep_fqln} not found in local registry. Validating by prefix.")

            dep_tier = TIERS.get(dep_type, 0)

            # --- CORE ARCHITECTURAL RULES ---

            # 1. Unidirectional Tier Enforcement (No Downward Dependencies)
            if dep_tier < current_tier:
                errors.append(f"[{fqln}] DOWNWARD DEPENDENCY: {doc_type} (Tier {current_tier}) illegally depends on {dep_type} (Tier {dep_tier}).")

            # 2. Bedrock Isolation (Section 2.1)
            if doc_type == "CA_BEDROCK" and dep_type != "CA_BEDROCK":
                errors.append(f"[{fqln}] BEDROCK VIOLATION: Bedrock CAs may only depend on other Bedrock CAs.")

            # 3. Emergency Isolation (Section 2.3.6)
            if doc_base in ["EL", "EB"] and dep_base != "CA":
                errors.append(f"[{fqln}] EMERGENCY VIOLATION: {doc_base} may only depend upon Constitutional Articles (CA).")

            # 4. Budget & Obligation Constraints (Section 2.3.1 & 2.3.4)
            if doc_base == "LB" and dep_base not in ["CA", "LA"]:
                errors.append(f"[{fqln}] BUDGET VIOLATION: LB may only depend upon CA or LA.")
            if doc_base == "OP" and dep_base not in ["CA", "LA", "CO"]:
                errors.append(f"[{fqln}] OBLIGATION VIOLATION: OP may only depend upon CA, LA, or CO.")

    return errors

def main():
    laws_dir = "./laws/docs"
    print("--- Hudson Republic Legislative Compiler ---")
    print("Indexing repository...")
    registry = index_repository(laws_dir)
    print(f"Indexed {len(registry)} legislative instruments.\n")

    print("Running Static Analysis...")
    errors = lint_registry(registry)

    if errors:
        print(f"Build Failed: {len(errors)} Violations Found\n")
        for error in errors:
            print(error)
        exit(1)
    else:
        print("Build Passed: 0 Violations. The Republic is secure.")

if __name__ == "__main__":
    main()
