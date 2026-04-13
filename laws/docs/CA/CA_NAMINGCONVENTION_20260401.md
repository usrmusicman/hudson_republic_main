# Legislative Document Classification and Naming Convention Act

## Definitions
All capitalized terms used in this Act shall be interpreted in accordance with their definitions in the referenced instruments below.

- **Distributed Version Control System (DVCS)**: A tool for managing code changes where every legislator (developer) has a full, local copy of the entire project repository, including its full history.
- **Fully Qualified Legislative Name (FQLN)**: A standardized identifier in the format `TYPE_SUBJECT_YYYYMMDD`.
- **HoC**: House of Constituents, as defined in **[CA_LEGISLATIVEFRAMEWORK_20260401](./CA_LEGISLATIVEFRAMEWORK_20260401.md)**.
- **CA class**: Constitutional Articles requiring unanimous approval (100%) in the House of Constituents and a unanimous verdict (12/12) in the Senate across three readings in each house.

## Preamble
**WHEREAS** the Hudson Republic is founded upon a binary governance structure that preserves the separation of powers, upholds federal supremacy within enumerated jurisdiction, reserves residual powers to the Ridings, and safeguards the immutable rights of the Individual;

**AND WHEREAS** every legislative instrument — whether federal or Riding-level — must be immediately identifiable as to its class, purpose, subject matter, origin, and DVCS revision history;

**AND WHEREAS** a standardized **Fully Qualified Legislative Name (FQLN)** format promotes human readability, machine parseability, version control, automated auditing, searching, sorting, and long-term archival integrity through distributed version-control systems;

**NOW THEREFORE**, the Senate and House of Constituents of the Hudson Republic enact as follows:

## Section 1 — Classification of Legislative Instruments
The Republic establishes ten classes of legislative instrument. Constitutional Articles (CA) are exclusive to the federal level. All other classes may exist at the Riding level but remain subordinate to federal supremacy.

### CA — Constitutional Article
* **Purpose**: Provisions of the Constitution or amendments.  
* **Enactment**: Requires three separate readings in the House of Constituents with unanimous approval (100%), followed by three separate readings in the Senate with a unanimous verdict (12/12) at each stage.  
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
* **Enactment**: See Section 6.2 for detailed rules.

### FO — Forms
* **Purpose**: Administrative templates, licenses, and notices.  
* **Enactment**: Created or amended by the Executive Office; **no legislative readings required**. Void if they contradict parent legislation.

## Section 6 — Dependency Handling and Reference Rules

To preserve constitutional hierarchy and legislative integrity, every instrument must comply with the following dependency rules. No instrument may depend upon a lower-authority instrument in a manner that would undermine its own enactment threshold.__

**Legislative Framework Dependency Tree**

![Dependency Tree](../../images/CA/CA_NAMINGCONVENTION_20260401/HUDSON_DEPENDENCYTREE.png)

### 6.1 General Dependency Tree Logic
- Instruments requiring **three readings** (CA class) may only depend upon other instruments that also require three readings.  
- Instruments requiring **two readings** (LA, LB) may depend upon instruments requiring two or three readings.  
- Instruments requiring **one reading** (OP, CO, SCH, LC, FO) may depend upon instruments requiring one, two, or three readings.

### 6.2 Supporting Instruments — Schedules (SCH) and Forms (FO)
Schedules (SCH) and Forms (FO) are purely supporting instruments. They share the following rules:

- They always require a **minimum of zero readings** and a **maximum of three readings**.  
- They remain non-substantive. They cannot create new rights, obligations, or authorities independent of their parent instrument.  
- **One-way reference only**: The parent instrument (CA, LA, LB, etc.) references the Schedule or Form. The Schedule or Form itself lists **no dependencies**.  
- If a Schedule or Form is not depended upon by any instrument, it defaults to **no readings** in either legislative house (Senate or HoC).

#### 6.2.1 Schedules (SCH) — Special Rule
A Schedule (SCH) is a purely supporting instrument containing lists, indexes, technical specifications, tariffs, annexes, or similar material.  

- When a parent instrument depends upon a Schedule, the Schedule inherits the exact enactment threshold of that parent.

#### 6.2.2 Forms (FO) — Special Rule
Forms (FO) are administrative templates only and are non-binding.  

- Forms are created or amended by the Executive Office; **no legislative readings are required**.  
- When a parent instrument depends upon a Form, the Form inherits the exact enactment threshold of that parent.

### 6.3 Other Specific Dependency Rules
1. **Legislative Budgets (LB)**: May only depend upon Legislative Articles (LA) and Constitutional Articles (CA). This directionality is not reciprocal. They may not depend upon Schedules (SCH) or other Legislative Budgets (LB).  
2. **Legislative Articles (LA)**: May only depend upon other Legislative Articles (LA), Constitutional Articles (CA), and Schedules (SCH).  
3. **Legal Codes (CO)**: May only depend upon Constitutional Articles (CA), Legislative Articles (LA), other Legal Codes (CO) and Schedules (SCH). They may not depend upon budgetary instruments such as Legislative Budgets (LB) or Obligation Papers (OP).  
4. **Obligation Papers (OP)**: May only depend upon Constitutional Articles (CA), Legislative Articles (LA), Legal Codes (CO). They may not depend upon Schedules (SCH), Legislative Budgets (LB) or other Obligation Papers (OP).  
5. **Legislative Challenges (LC)**: Shall have no dependencies. As reforming, amending, or decommissioning instruments, LCs stand independent and may target any class of legislation.  
6. **Emergency Instruments (EL and EB)**: May only depend upon Constitutional Articles (CA). They must not depend upon any peacetime legislative instruments. No derivative legislative instruments may be created from an emergency instrument, as they carry an absolute, time-bound expiration.  
7. **Cultural Instruments (CULT)**: Federal cultural items and symbols are immutable and serve ceremonial, educational, or identity purposes only. They are not binding legislative instruments and carry no dependencies. They may only be terminated by a seventy-five percent (75%) citizen referendum held simultaneously in all Ridings of the Hudson Republic.

## Section 7 — Purpose and Effect
This Act ensures machine-parseable legislative history, clear distinction between peacetime and emergency law, total transparency, auditable archival integrity, and a logically consistent dependency hierarchy that preserves constitutional supremacy.

## Section EX1 — Dependency Examples

**EX1.1**  
A Legislative Article (LA) that depends upon a Schedule (SCH) requires the SCH to undergo the same two readings as the LA.

**EX1.2**  
A Schedule (SCH) referenced by an Emergency instrument (EL or EB) requires only one reading.

**EX1.3**  
A Schedule (SCH) depended upon by a Form (FO) defaults to one reading unless it is also depended upon by a higher-threshold instrument elsewhere.

**EX1.4**  
A standalone Schedule (SCH) that is not depended upon by any instrument defaults to one reading in each house (or Senate-only in emergency).

**EX1.5**  
A Legal Code (CO) may depend upon CA, LA, other CO instruments, and SCH, but may not depend upon LB or OP.

**EX1.6**  
An Obligation Paper (OP) may depend upon any equal or higher authority, including LA and CA.

**EX1.7**  
A Form (FO) may depend upon any legislative instrument, as it is administrative and non-binding.

## Reference Dependencies
Dependencies (in alphabetical order)  
* **[CA_LEGISLATIVEFRAMEWORK_20260401](./CA_LEGISLATIVEFRAMEWORK_20260401.md)**  
* **[CA_THEINDIVIDUAL_20260401](./CA_THEINDIVIDUAL_20260401.md)**  

**Original Author**: 

**House Signature**: 

**Senate Signature**: 

**Executive Office Signature**: 

**FQLN**: CA_NAMINGCONVENTION_20260401
