#!/usr/bin/env python3

import os
import re
import subprocess
import argparse
from pathlib import Path
from collections import defaultdict
from dataclasses import dataclass, field
from typing import Optional, Set

# === CONSTANTS & CONFIGURATION ===

# The ONLY valid top-level directories inside laws/docs/ based on the terminal output
VALID_PREFIXES: list[str] = ["CA", "CO", "EB", "EL", "FO", "LA", "LB", "OP", "SCH"]

TIERS: dict[str, int] = {
    "CA_BEDROCK": 5, "CA_FOUNDATIONAL": 4,
    "LA": 3, "CO": 2, "LB": 2, "OP": 2, "EL": 2, "EB": 2,
    "SCH": 1, "FO": 1
}

# Derived strictly from HUDSON_DEPENDENCYTREE.jpg arrows
ALLOWED_DEPENDENCIES: dict[str, list[str]] = {
    "CA": ["CA"],
    "LA": ["CA", "LA"],
    "CO": ["CA", "LA", "CO"],
    "EB": ["CA"],
    "EL": ["CA"],
    "FO": ["CA", "LA", "CO"],
    "SCH": ["CA", "LA", "CO"],
    "LB": ["CA", "LA"],
    "OP": ["CA", "LA", "CO"]
}

ROOT_CONSTITUTION: str = "CA_THEINDIVIDUAL_20260401"
CLARITY_ACT: str = "CA_CLARITYACT_20260522"

# === DATA STRUCTURES ===

@dataclass
class LegislativeDocument:
    fqln: str
    filepath: Path
    base_type: str
    precise_type: str
    deps: list[str] = field(default_factory=list)

# === UTILITY FUNCTIONS ===

def sync_submodules() -> None:
    """Ensures all legislative submodules are initialized and updated."""
    print("Synchronizing legislative submodules...")
    subprocess.run(['git', 'submodule', 'update', '--init', '--recursive'], check=True)

def get_git_commit_data(filepath: Path) -> str:
    """Fetches the latest Git commit hash, author, and date for a specific file."""
    try:
        git_log = subprocess.check_output(
            ['git', 'log', '-1', '--format=%H | %aI | %an | %s', str(filepath)],
            stderr=subprocess.STDOUT,
            text=True
        ).strip()
        return git_log if git_log else "No Git history found."
    except (subprocess.CalledProcessError, FileNotFoundError):
        return "Git metadata unavailable."

def extract_date_from_fqln(fqln: str) -> int:
    """Extracts the YYYYMMDD integer from an FQLN for chronological comparison."""
    try:
        return int(fqln.split('_')[-1])
    except (ValueError, IndexError):
        return 0

def parse_fqln(fqln: str) -> tuple[Optional[str], Optional[str], Optional[str]]:
    """Parse FQLN into TYPE, SUBJECT, DATE components."""
    parts = fqln.split('_')
    if len(parts) != 3:
        return None, None, None
    return parts[0], parts[1], parts[2]

# === INDEXING ===

def index_repository(docs_dir: Path) -> tuple[dict[str, LegislativeDocument], dict[str, list[str]], list[str]]:
    """Crawls ONLY the allowed laws/docs/ directories to build a strict registry."""
    registry: dict[str, LegislativeDocument] = {}
    subject_map: dict[str, list[str]] = defaultdict(list)
    errors: list[str] = []

    if not docs_dir.exists() or not docs_dir.is_dir():
        errors.append(f"CRITICAL: Base directory {docs_dir} does not exist.")
        return registry, subject_map, errors

    # Restrict crawling strictly to the 9 valid prefix folders
    for prefix in VALID_PREFIXES:
        prefix_dir = docs_dir / prefix
        if not prefix_dir.exists():
            continue

        for file_path in prefix_dir.glob("**/*"):
            if file_path.is_dir() or file_path.name == "remove_me":
                continue

            if file_path.suffix != ".md":
                errors.append(f"[{file_path.name}] FORMAT ERROR: Legislation must be markdown (.md).")
                continue

            fqln = file_path.stem

            try:
                content = file_path.read_text(encoding='utf-8')
                base_type = fqln.split('_')[0]
                precise_type = base_type

                if base_type == "CA":
                    weight_match = re.search(r"This article is designated as:\s*\*\*(Bedrock|Foundational)\*\*",
                                           content, re.IGNORECASE)
                    precise_type = f"CA_{weight_match.group(1).upper()}" if weight_match else "CA_FOUNDATIONAL"

                deps: list[str] = []
                dep_sections = re.findall(r"## Hard Dependencies\r?\n(.*?)(?=\r?\n---|\Z)", content, re.DOTALL)
                for section in dep_sections:
                    deps.extend(re.findall(r"\[([A-Z0-9_]+)\]", section))

                # Remove duplicates, preserve order
                deps = list(dict.fromkeys(deps))

                registry[fqln] = LegislativeDocument(
                    fqln=fqln,
                    filepath=file_path,
                    base_type=base_type,
                    precise_type=precise_type,
                    deps=deps
                )

                _, subject, _ = parse_fqln(fqln)
                if subject:
                    subject_map[subject].append(fqln)

            except Exception as e:
                errors.append(f"[{file_path.name}] READ ERROR: {str(e)}")

    return registry, subject_map, errors

# === LINTING MODULES ===

def check_cycles(registry: dict[str, LegislativeDocument], errors: list[str]) -> None:
    """Validates against circular dependencies using Depth-First Search."""
    visited: dict[str, int] = {}
    path: list[str] = []

    def dfs(node: str) -> None:
        if node not in registry:
            return
        if visited.get(node) == 1:
            cycle_start = path.index(node)
            cycle_nodes = path[cycle_start:] + [node]
            errors.append(f"[{node}] CIRCULAR DEPENDENCY DETECTED: {' -> '.join(cycle_nodes)}")
            return
        if visited.get(node) == 2:
            return

        visited[node] = 1
        path.append(node)

        for neighbor in registry[node].deps:
            dfs(neighbor)

        path.pop()
        visited[node] = 2

    for fqln in registry:
        if visited.get(fqln, 0) == 0:
            dfs(fqln)

def validate_fqln_and_paths(doc: LegislativeDocument, docs_root: Path, errors: list[str]) -> None:
    """Enforces FQLN formatting and strict directory placement."""
    f_type, f_subject, f_date = parse_fqln(doc.fqln)

    if not all([f_type, f_subject, f_date]):
        errors.append(f"[{doc.fqln}] FQLN FORMAT ERROR: Must contain exactly 3 fields separated by underscores.")
        return

    if f_type not in VALID_PREFIXES:
        errors.append(f"[{doc.fqln}] FQLN FIELD 1 ERROR: '{f_type}' is invalid. Allowed: {', '.join(VALID_PREFIXES)}.")

    if not f_subject.isalpha() or not f_subject.isupper() or len(f_subject) > 64:
        errors.append(f"[{doc.fqln}] FQLN FIELD 2 ERROR: Must be UPPERCASE alpha-only (max 64 chars).")

    if not f_date.isnumeric() or len(f_date) < 8 or len(f_date) > 16:
        errors.append(f"[{doc.fqln}] FQLN FIELD 3 ERROR: Must be numeric (8-16 chars).")
    elif int(f_date) < 20260401:
        errors.append(f"[{doc.fqln}.md] AGE VALIDATION ERROR: Legislation predates the federation.")

    # Strict path check: file MUST be inside laws/docs/PREFIX/FQLN.md
    expected_path = docs_root / f_type / f"{doc.fqln}.md"
    if doc.filepath.resolve() != expected_path.resolve():
        errors.append(f"[{doc.fqln}] DIRECTORY ERROR: File exists at {doc.filepath}, but strictly belongs at {expected_path}.")

def validate_tree_hierarchy(doc: LegislativeDocument, registry: dict[str, LegislativeDocument], errors: list[str]) -> None:
    """Enforces the visual logic defined in HUDSON_DEPENDENCYTREE.jpg."""

    # Check sovereignty baseline logic
    if doc.fqln == ROOT_CONSTITUTION and len(doc.deps) > 0:
        errors.append(f"[{doc.fqln}] GENESIS VIOLATION: [{ROOT_CONSTITUTION}] shall have no dependencies.")

    if doc.base_type not in ["CA", "FO", "SCH"] and ROOT_CONSTITUTION not in doc.deps:
        errors.append(f"[{doc.fqln}] SOVEREIGNTY VIOLATION: Must explicitly list [{ROOT_CONSTITUTION}] as a Hard Dependency.")

    if doc.base_type == "CA" and doc.fqln not in [ROOT_CONSTITUTION, CLARITY_ACT]:
        if CLARITY_ACT not in doc.deps:
            errors.append(f"[{doc.fqln}] CLARITY VIOLATION: Constitutional Articles must explicitly list [{CLARITY_ACT}] as a Hard Dependency.")

    # Determine what base types this document depends on
    resolved_dep_types: Set[str] = set()
    for dep_fqln in doc.deps:
        if dep_fqln in registry:
            resolved_dep_types.add(registry[dep_fqln].base_type)

    # Enforce exact upstream anchors based on diagram arrows
    if doc.base_type == "LA" and "CA" not in resolved_dep_types:
        errors.append(f"[{doc.fqln}] TREE VIOLATION: Legislative Articles (LA) must anchor to at least one Constitutional Article (CA).")

    elif doc.base_type == "CO" and "LA" not in resolved_dep_types:
        errors.append(f"[{doc.fqln}] TREE VIOLATION: Legal Codes (CO) must anchor to at least one Legislative Article (LA).")

    elif doc.base_type == "LB" and "LA" not in resolved_dep_types:
        errors.append(f"[{doc.fqln}] TREE VIOLATION: Legislative Budgets (LB) must anchor to a Legislative Article (LA).")

    elif doc.base_type == "OP" and "CO" not in resolved_dep_types:
        errors.append(f"[{doc.fqln}] TREE VIOLATION: Obligation Papers (OP) must anchor to a Legal Code (CO).")

    elif doc.base_type in ["EL", "EB"] and "CA" not in resolved_dep_types:
        errors.append(f"[{doc.fqln}] TREE VIOLATION: Emergency Instruments (EL/EB) must bypass standard law and anchor directly to a CA.")

def validate_dependencies(doc: LegislativeDocument, registry: dict[str, LegislativeDocument],
                          errors: list[str], audit_flags: list[str]) -> None:
    """Validates physical presence (rogue elimination), structural tiers, and temporal continuity."""
    current_tier = TIERS.get(doc.precise_type, 0)
    current_date = extract_date_from_fqln(doc.fqln)

    for dep_fqln in doc.deps:
        # STRICT ROGUE DEPENDENCY CHECK
        if dep_fqln not in registry:
            errors.append(f"[{doc.fqln}] ROGUE DEPENDENCY DETECTED: '{dep_fqln}' does not exist inside laws/docs/. All dependencies must be valid, physical instruments.")
            continue

        dep_doc = registry[dep_fqln]
        dep_tier = TIERS.get(dep_doc.precise_type, 0)
        dep_date = extract_date_from_fqln(dep_fqln)

        # Template/Tier Validation
        allowed = ALLOWED_DEPENDENCIES.get(doc.base_type)
        if allowed is not None and dep_doc.base_type not in allowed:
            errors.append(f"[{doc.fqln}] TEMPLATE VIOLATION: {doc.base_type} may only depend on {allowed}. Found: {dep_doc.base_type}.")

        if dep_tier < current_tier:
            errors.append(f"[{doc.fqln}] DOWNWARD DEPENDENCY: {doc.precise_type} (Tier {current_tier}) illegally depends on {dep_doc.precise_type} (Tier {dep_tier}).")

        if doc.precise_type == "CA_BEDROCK" and dep_doc.precise_type != "CA_BEDROCK":
            errors.append(f"[{doc.fqln}] BEDROCK VIOLATION: Bedrock CAs may only depend on other Bedrock CAs.")

        # Temporal Cryptographic Audit
        if dep_date > current_date and current_date != 0 and dep_date != 0:
            audit_msg = (
                f"⚠️  HIGH-SCRUTINY CRYPTOGRAPHIC AUDIT FLAG: TEMPORAL INVERSION\n"
                f"    -> Instrument: {doc.fqln}\n"
                f"    -> Target:     {dep_fqln}\n"
                f"    -> DVCS Data:  {get_git_commit_data(doc.filepath)}\n"
            )
            audit_flags.append(audit_msg)

# === ORCHESTRATION ===

def lint_registry(docs_root: Path, registry: dict[str, LegislativeDocument], subject_map: dict[str, list[str]],
                  initial_errors: list[str]) -> tuple[list[str], list[str]]:
    """Master controller for all validation passes."""
    errors = initial_errors.copy()
    audit_flags: list[str] = []

    check_cycles(registry, errors)

    for subject, fqlns in subject_map.items():
        if len(fqlns) > 1:
            errors.append(f"SUBJECT COLLISION: '{subject}' used by: {', '.join(fqlns)}. Field 2 (SUBJECT) must be unique.")

    for doc in registry.values():
        validate_fqln_and_paths(doc, docs_root, errors)
        validate_tree_hierarchy(doc, registry, errors)
        validate_dependencies(doc, registry, errors, audit_flags)

    return errors, audit_flags

def main() -> None:
    parser = argparse.ArgumentParser(description="Hudson Republic Federated Validator (v5.0 - Strict Tree Edition)")
    parser.add_argument("--audit", action="store_true", help="Display high-scrutiny temporal audit flags.")
    args = parser.parse_args()

    if os.environ.get("GITHUB_ACTIONS") == "true":
        args.audit = True

    sync_submodules()

    docs_root = Path("laws/docs")
    print(f"Indexing federated repository (strictly monitoring {docs_root} directories)...")

    registry, subject_map, indexing_errors = index_repository(docs_root)
    print(f"Indexed {len(registry)} valid instruments.")

    errors, audit_flags = lint_registry(docs_root, registry, subject_map, indexing_errors)

    if args.audit and audit_flags:
        print("\n" + "="*80)
        print("=== FEDERATED AUDIT LOG: SECURITY & COMPLIANCE FLAGS ===")
        print("="*80)
        for flag in audit_flags:
            print(flag)
        print("="*80 + "\n")

    if errors:
        for error in sorted(list(set(errors))):
            print(error)
        print("\nBUILD FAILED: Governance framework violations detected.")
        exit(1)

    print("BUILD PASSED: The Federation dependency tree is secure and compliant.")

if __name__ == "__main__":
    main()
