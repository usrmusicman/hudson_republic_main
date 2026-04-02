# Legislative Document Classification and Naming Convention Act

---

## Definitions
All capitalized terms used in this Act shall be interpreted in accordance with their definitions in the referenced instruments below.

- **Fully Qualified Legislative Name (FQLN)**: A standardized identifier in the format `TYPE_SUBJECT_YYYYMMDD`.
- **HoC**: House of Constituents, as defined in CA_LEGISLATIVEFRAMEWORK_20260401.
- **CA class**: Constitutional Articles requiring unanimous Senate verdict (12/12) on three readings for amendment.

---

## Preamble
**WHEREAS** the Hudson Republic is founded upon a binary governance structure that preserves the separation of powers, upholds federal supremacy within enumerated jurisdiction, reserves residual powers to the Ridings, and safeguards the immutable rights of the Individual;

**AND WHEREAS** every legislative instrument — whether federal or Riding-level — must be immediately identifiable as to its class, purpose, subject matter, origin, and revision history;

**AND WHEREAS** a standardized **Fully Qualified Legislative Name (FQLN)** format promotes human readability, machine parseability, version control, automated auditing, searching, sorting, and long-term archival integrity through distributed version-control systems;

**NOW THEREFORE**, the Senate and House of Constituents of the Hudson Republic enact as follows:

---

## Section 1 — Classification of Legislative Instruments
The Republic establishes ten classes of legislative instrument. Constitutional Articles (CA) are exclusive to the federal level. All other classes may exist at the Riding level but remain subordinate to federal supremacy.

### CA — Constitutional Article
* **Purpose**: Provisions of the Constitution or amendments.  
* **Enactment**: Requires three separate readings in the Senate with a unanimous verdict (12/12) at each stage.  
* **Scope**: Federal level only.

### LA — Legislative Article
* **Purpose**: Ordinary primary legislation enacted in peacetime.  
* **Enactment**: Originated in the HoC, reviewed by the Senate. Requires two readings in each house.

### LB — Legislative Budget
* **Purpose**: Multi-year fiscal planning (longer than one year).  
* **Enactment**: Federal budgets are tabled by the Executive; Riding budgets must not conflict with federal obligations. Requires two readings in each house.

### EL — Emergency Legislation
* **Purpose**: Legislation enacted solely during a declared state of emergency or war.  
* **Enactment**: Originated and adjudicated exclusively by the Senate. Requires **one reading**. Automatic expiry upon return to peace.  
* **Expiry**: Automatic cessation upon end of emergency. Extensions require a unanimous (12/12) Senate verdict.

### EB — Emergency Budget
* **Purpose**: Extraordinary fiscal authorizations for emergency or war periods.  
* **Enactment**: Identical to EL (Senate exclusive). Requires **one reading**. Automatic expiry upon return to peace.  
* **Expiry**: Automatic cessation upon end of emergency. Extensions require a unanimous (12/12) Senate verdict.

### OP — Obligation Paper
* **Purpose**: Binding short-term obligations (up to one year) between Ridings or between Ridings and the federal level.  
* **Enactment**: One reading in the HoC and one in the Senate.

### CO — Legal Code
* **Purpose**: Systematized, codified, and harmonized rules to implement a parent Legislative Article (LA).  
* **Enactment**: One reading in the HoC and Senate.

### LC — Legislative Challenge
* **Purpose**: Repeal, amendment, or decommissioning of existing legislation due to unconstitutionality or overreach.  
* **Enactment**: Senate applies the threshold required by the *challenged* instrument (e.g., 12/12 for CA challenges).

### SCH — Schedule
* **Purpose**: Lists, indexes, or technical specifications (e.g., tariff schedules).  
* **Enactment**: One reading in each house (peacetime); Senate only (emergency). Purely referential; must anchor to a parent instrument.

### FO — Forms
* **Purpose**: Administrative templates, licenses, and notices.  
* **Enactment**: Created or amended by the Executive Office; **no legislative readings required**. Void if they contradict parent legislation.

---

## Section 2 — Legislative Bodies and Procedural Requirements

### 2.1 Peacetime Structure
* **House of Constituents (HoC)**: The Legislative Prosecutor. Sole originating chamber for all peacetime primary legislation.  
* **Senate**: The High Constitutional Jury. Sole chamber authorized to place legislation “on trial” for final verdict.

### 2.2 Emergency / Wartime Structure
* **HoC Suspension**: The House of Constituents is automatically suspended during a Proclamation of Emergency.  
* **Senate Authority**: The Senate assumes exclusive authority to originate and adjudicate emergency instruments (EL, EB).  
* **Expiry**: All emergency measures expire immediately upon the return of peace.

### 2.3 Executive Office
* **Minting**: The National Representative performs an independent constitutional review and either “mints” (enacts) or “decommissions” (terminates) the instrument. No power to amend or delay.

---

## Section 3 — Supremacy and Scope
* **Federal Supremacy**: No Riding may enact measures that contradict federal instruments or Constitutional Articles.  
* **Residual Powers**: Ridings may only enact LA, LB, EL, EB, OP, CO, LC, SCH, and FO within their devolved residual jurisdictions (see CA_LEGISLATIVEFRAMEWORK_20260401).

---

## Section 4 — Fully Qualified Legislative Name (FQLN)
Every instrument must follow the strict format: `Field1_Field2_Field3`

1. **Field 1 (Type)**: Exactly four uppercase letters (e.g., `LA_`, `CA_`).  
2. **Field 2 (Subject)**: 1–64 uppercase letters (A–Z only), no spaces or symbols (e.g., `TAXREFORM`).  
3. **Field 3 (Date)**: 8–16 numeric characters in `YYYYMMDD` format.

**Example**: `LA_LANDUSEACT_20260315`

---

## Section 5 — Maintenance and Application
* **File Format**: All instruments shall be written in Markdown (`.md`).  
* **Version Control**: Repositories must use systems supporting immutable history and cryptographic commit signing.  
* **Clean Repository**: Filenames consist of the three FQLN fields. The full revision history resides within the document header.

---

## Section 6 — Dependency Handling and Reference Rules
To preserve constitutional hierarchy and legislative integrity, every instrument must comply with the following dependency rules. No instrument may depend upon a lower-authority instrument in a manner that would undermine its own enactment threshold.

### 6.1 General Dependency Tree Logic
- Instruments requiring **three readings** (CA class) may only reference and depend upon other instruments that also require three readings.  
- Instruments requiring **two readings** (LA, LB) may reference and depend upon instruments requiring two or three readings.  
- Instruments requiring **one reading** (OP, CO, SCH, LC, FO) may reference and depend upon instruments requiring one, two, or three readings.

See this link for the dependency tree as ASCII art: [Constitutional Articles](../../images/CA/CA_NAMINGCONVENTION_20260401/HUDSON_DEPENDENCYTREE_ASCII_20260401.txt)

![Constitutional Articles](../../images/CA/CA_NAMINGCONVENTION_20260401/HUDSON_DEPENDENCYTREE_20260401.jpg)

### 6.2 Specific Dependency Rules
1. **Legislative Budgets (LB)**: May reference and depend upon Legislative Articles (LA) or Constitutional Articles (CA). This directionality is not reciprocal.  
2. **Legislative Articles (LA)**: May only reference and depend upon other LA instruments or CA instruments.  
3. **Legal Codes (CO), Obligation Papers (OP), Schedules (SCH), and Forms (FO)**: May reference and depend upon any legislative instrument of equal or higher authority.  
4. **Legislative Challenges (LC)**: Shall have no dependencies. As reforming, amending, or decommissioning instruments, LCs stand independent and may target any class of legislation.  
5. **Emergency Instruments (EL and EB)**: May only depend upon Constitutional Articles (CA). They must not depend upon any peacetime legislative instruments. No derivative legislative instruments may be created from an emergency instrument, as they carry an absolute, time-bound expiration and are not originated in the House of Constituents.  
6. **Cultural Instruments (CULT)**: Federal cultural items and symbols are immutable and serve ceremonial, educational, or identity purposes only. They are not binding legislative instruments and carry no dependencies. They may only be terminated by a seventy-five percent (75%) citizen referendum held simultaneously in all Ridings of the Hudson Republic.

---

## Section 7 — Purpose and Effect
This Act ensures machine-parseable legislative history, clear distinction between peacetime and emergency law, total transparency, auditable archival integrity, and a logically consistent dependency hierarchy that preserves constitutional supremacy.

---

## Reference Dependencies
Dependencies (in alphabetical order)  
* CA_LEGISLATIVEFRAMEWORK_20260401  
* CA_THEINDIVIDUAL_20260401  

---

**Original Author**: 

**House Signature**: 

**Senate Signature**: 

**Executive Office Signature**: 

**FQLN**: CA_NAMINGCONVENTION_20260401  
**Revision**: 00000001
