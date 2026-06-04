# Distributed Version Control System Implementation Act

---

## Constitutional Weight (CA)
This section designates the constitutional significance and amendability of the article.

- **Bedrock Constitutional Article**: Unmoving and inviolable. These form the permanent foundation of the Republic and may only be amended by unanimous verdict as defined in the **[Clarity Act](./CA_CLARITYACT_20260522.md)**.  
- **Foundational Constitutional Article**: Core to the functioning of the Republic and of high importance, but capable of measured amendment by overwhelming majority verdict as defined in the **[Clarity Act](./CA_CLARITYACT_20260522.md)**.

This article is designated as: **Foundational**

---

## Hard Dependencies
List any legislative instrument(s) (in alphabetical order) that this article must depend on. List the FQLN(s) below. Any FQLN(s) mentioned in other sections are considered to be references and not actual dependencies.  
Only **Constitutional Articles (CA)** can be listed here.

Dependencies
* **[CA_CLARITYACT_20260522](./CA_CLARITYACT_20260522.md)**  
* **[CA_NAMINGCONVENTION_20260401](./CA_NAMINGCONVENTION_20260401.md)**  
* **[CA_THEINDIVIDUAL_20260401](./CA_THEINDIVIDUAL_20260401.md)**

---

## Definitions
All capitalized terms used in this Act shall be interpreted in accordance with their definitions in the referenced instruments below.

- **Distributed Version Control System (DVCS)**: A tool for managing code changes where every legislator (contributor) has a full, local copy of the entire project repository, including its full history.  
- **Fully Qualified Legislative Name (FQLN)**: A standardized identifier in the format `TYPE_SUBJECT_YYYYMMDD`.

---

## Preamble
Every legislative instrument, whether federal or Riding-level, must be immediately identifiable as to its class, purpose, subject matter, origin, and DVCS revision history.  
A standardized **Fully Qualified Legislative Name (FQLN)** format promotes human readability, machine parseability, version control, automated auditing, searching, sorting, and long-term archival integrity through distributed version-control systems.  
This Act establishes the technical and procedural framework for the use of DVCS in the legislative process of the Hudson Republic, ensuring transparency, auditability, and resilience of the Republic’s legal corpus.

---

## Section 1 — Fully Qualified Legislative Name (FQLN)

**1.1** Every legislative instrument shall be identified by a standardized **Fully Qualified Legislative Name (FQLN)** in the format `TYPE_SUBJECT_YYYYMMDD`. This format ensures immediate human readability, machine parseability, version control, automated auditing, searching, sorting, and long-term archival integrity through distributed version-control systems.

**1.2 Uniqueness Requirement**  
The **SUBJECT** component (Field 2) of the FQLN must be unique within the repository at any given time. Duplicate SUBJECT names are strictly prohibited to prevent confusion, overlapping scope, or inadvertent duplication of legislative instruments within the main repository.  

If a legislative instrument is repealed, decommissioned, or otherwise removed from active effect, the same SUBJECT name may be reused for a future instrument. In such cases, the new instrument must carry a different timestamp in Field 3 (YYYYMMDD) to clearly distinguish it as a distinct legislative act. This rule preserves institutional memory while maintaining clarity and preventing namespace collisions.

---

## Section 2 — Dependency Handling and Reference Rules

To preserve constitutional hierarchy and legislative integrity, every instrument must comply with the following dependency rules. No instrument may depend upon a lower-authority instrument in a manner that would undermine its own enactment threshold.

**2.1 General Dependency Tree Logic**  
The Hudson Republic enforces a strict hierarchical dependency model to preserve constitutional integrity. An instrument may only declare **Hard Dependencies** on instruments of equal or higher constitutional weight. This prevents dilution of authority and maintains the supremacy of Bedrock and Foundational articles.

- **Bedrock Constitutional Articles (CA(B))** may only depend upon other **Bedrock Constitutional Articles**.  
- **Foundational Constitutional Articles (CA(F))** may depend upon **Bedrock** and other **Foundational** articles.  
- All legislative instruments outside of **Forms (FO)**, **Legislative Challenges (LC)**, **Cultural Items (CULT)**, and **Schedules (SCH)** must maintain a hard dependency on **[The Individual Act](./CA_THEINDIVIDUAL_20260401.md)**.  
- All **Constitutional Articles (CA)**, both bedrock and foundational, with the sole exception of the listed instruments themselves, must depend on **[The Individual Act](./CA_THEINDIVIDUAL_20260401.md)** and the **[Clarity Act](./CA_CLARITYACT_20260522.md)**.  
- **[The Individual Act](./CA_THEINDIVIDUAL_20260401.md)** shall carry zero dependencies.  
- **Emergency Instruments (EL, EB)** may only depend upon **Constitutional Articles (CA)**.  
- **Legislative Challenges (LC)** and **Cultural Items (CULT)** shall carry **no dependencies** under any circumstance.  
- Circular dependencies are strictly prohibited to prevent dependency loop errors within the validator stack.

**2.2 Supporting Instruments — Schedules (SCH) and Forms (FO)**  
Schedules (SCH) and Forms (FO) are purely supporting instruments. They share the following rules:

- They always require a minimum of zero readings and a maximum of three readings.  
- They inherit the enactment threshold and legal weight of the **highest-tier parent instrument** they depend upon.  
- **Authors must be careful with intent**: listing a Constitutional Article (CA) as a dependency will bind the Schedule or Form to constitutional-level standards, even if the primary parent legislation targeted is a Legislative Article (LA).  
- They remain non-substantive. They cannot create new rights, obligations, or authorities independent of their parent instrument(s).  
- If a Schedule or Form is not depended upon by any instrument, it defaults to no readings in either legislative house.

**2.3 Temporal Inversions and Implicit Amendments**  
Any legislative dependency created by temporal inversion (e.g., an instrument referencing a successor instrument that technically precedes it in the registry) shall be automatically classified as an "Implicit Technical Amendment." Such dependencies are considered legally valid and compliant provided the Git commit metadata timestamp supports the chronological validity of the reference. This clause supersedes strict linear hierarchy validation for these specific instances.

1. **Presumption of Amendment**: The individual shall interpret this state as an implicit technical amendment to the implementation layers of the parent instrument, preserving the historical baseline of the parent law while consuming the updated dependency specification.  
2. **Rogue Policy Injection Safeguard**: Because a temporal inversion bypasses synchronous bicameral readings, it shall automatically trigger a high-scrutiny cryptographic audit flag.  
3. **DVCS Verification Protocol**: To ensure the inversion does not mask a rogue policy injection, auditors must utilize the repository's native Distributed Version Control System (DVCS) functions (e.g., `git log -p` or `git diff`) to verify the exact commit history. The delta must prove that the dependency bump was executed by an authorized signature and carries purely administrative or technical adjustments aligned with the parent instrument's original intent.  
4. **FQLN Date Field**: The FQLN date is when the legislation is drafted in first reading. Since git handles integrity and versioning, the date field can be ignored from the dependency resolution process. The date field is used for archival purposes only.

---

## Section 3 - Legislative Dependency Matrix
This is a visualization of the hard dependencies that can be associated with each legislative instrument type.

| Instrument Listed (Below)      | CA(B) | CA(F) | CO | CULT | EL | EB | FO | LA | LB | LC | OP | SCH |
|--------------------------------|-------|-------|----|------|----|----|----|----|----|----|----|-----|
| CA(B) - Bedrock                | ✔     | X     | X  | X    | X  | X  | X  | X  | X  | X  | X  | X   |
| CA(F) - Foundational           | ✔     | ✔     | X  | X    | X  | X  | X  | X  | X  | X  | X  | X   |
| CULT - Cultural Item           | X     | X     | X  | X    | X  | X  | X  | X  | X  | X  | X  | X   |
| EL - Emergency Legislation     | ✔     | ✔     | X  | X    | X  | X  | X  | X  | X  | X  | X  | X   |
| EB - Emergency Budget          | ✔     | ✔     | X  | X    | X  | X  | X  | X  | X  | X  | X  | X   |
| FO - Forms                     | ✔     | ✔     | ✔  | X    | X  | X  | X  | ✔  | X  | X  | X  | X   |
| LA - Legislative Article       | ✔     | ✔     | X  | X    | X  | X  | X  | ✔  | X  | X  | X  | X   |
| LB - Legislative Budget        | ✔     | ✔     | X  | X    | X  | X  | X  | ✔  | X  | X  | X  | X   |
| LC - Legislative Challenge     | X     | X     | X  | X    | X  | X  | X  | X  | X  | X  | X  | X   |
| OP - Obligation Paper          | ✔     | ✔     | ✔  | X    | X  | X  | X  | ✔  | X  | X  | X  | X   |
| SCH - Schedule                 | ✔     | ✔     | ✔  | X    | X  | X  | X  | ✔  | X  | X  | X  | X   |

---

## Section 4 — File Organization and Asset Management

To ensure long-term maintainability, clarity, and scalability of the legislative repository, all instruments shall follow this standardized file structure:

**4.1 Legislative Text Files**  
All primary legislative text files shall be stored in:  
`[root]/laws/docs/[INSTRUMENT_TYPE]/[INSTRUMENT_FQLN].md`

**4.2 Associated Image Assets**  
All supporting image assets shall be stored in a dedicated subdirectory using the instrument’s full **FQLN** as the folder name:  
`[root]/laws/images/[INSTRUMENT_TYPE]/[INSTRUMENT_FQLN]/[FILENAME]`

**4.3 Associated Attachment Assets**  
All supporting attachment assets shall be stored in a dedicated subdirectory using the instrument’s full **FQLN** as the folder name:  
`[root]/laws/attachments/[INSTRUMENT_TYPE]/[INSTRUMENT_FQLN]/[FILENAME]`

This separation of legislative text from attachments and visual assets streamlines repository maintenance, improves organization, and simplifies long-term archival and auditing.

---

## Section 5 — Purpose and Effect
This Act ensures machine-parseable legislative history, clear distinction between peacetime and emergency law, total transparency, auditable archival integrity, and a logically consistent dependency hierarchy that preserves constitutional supremacy, with particular protection for Bedrock provisions.

---

## Section 6 — Legal Validity and Binding Criteria

**6.1 Genesis Date**  
No legislative instrument is considered legally binding if it predates the genesis draft date of the Hudson Republic federation: **20260401** (April 1, 2026). All instruments bearing an earlier FQLN timestamp are deemed historical or superseded and hold no enforceable legal authority.

**6.2 Authorized Formats**  
A legislative instrument is legally binding only if it exists in one of the following forms:  
- Digital Markdown (`.md`) format maintained within the official legislative repository; or  
- Physical printed copy preserved in the Republic’s official **Disaster Backup Archive**.

**6.3 Disaster Backup Archive**  
The Disaster Backup Archive shall organize all printed instruments using the same **Fully Qualified Legislative Name (FQLN)** structure for consistency and auditability. This archive serves as the authoritative offline record in the event of digital system failure.

**6.4 Supplemental Materials**  
Diagrams, charts, schematics, images, spreadsheets, and all other attached or supporting files are considered **supplemental** in nature. They provide clarification, illustration, or technical detail but do not themselves constitute legally binding provisions. Only the primary Markdown legislative text (or its authorized physical print) holds binding force.

---

**Original Author**: 

**House Signature**: 

**Senate Signature**: 

**Executive Office Signature**: 

**FQLN**: CA_DVCSIMPLEMENTATION_20260604
