# Legislative Document Classification and Naming Convention Act

---

## Constitutional Weight (CA)
This section designates the constitutional significance and amendability of the article.

- **Bedrock Constitutional Article**: Unmoving and inviolable. These form the permanent foundation of the Republic and may only be amended by unanimous verdict as defined in the **[Clarity Act](./CA_CLARITYACT_20260522.md)**.  
- **Foundational Constitutional Article**: Core to the functioning of the Republic and of high importance, but capable of measured amendment by overwhelming majority verdict as defined in the **[Clarity Act](./CA_CLARITYACT_20260522.md)**.

This article is designated as: **Bedrock**

---

## Hard Dependencies
List any legislative instrument(s) (in alphabetical order) that this article must depend on. List the FQLN(s) below. Any FLQN(s) mentioned in other sections are considered to be references and not actual dependencies.  
Only **Constitutional Articles (CA)** and **Schedules (SCH)** can be listed here.

Dependencies
* **[CA_CLARITYACT_20260522](./CA_CLARITYACT_20260522.md)**  
* **[CA_LEGISLATIVEFRAMEWORK_20260401](./CA_LEGISLATIVEFRAMEWORK_20260401.md)**  
* **[CA_THEINDIVIDUAL_20260401](./CA_THEINDIVIDUAL_20260401.md)**  

---

## Definitions
All capitalized terms used in this Act shall be interpreted in accordance with their definitions in the referenced instruments below.

- **Distributed Version Control System (DVCS)**: A tool for managing code changes where every legislator (contributor) has a full, local copy of the entire project repository, including its full history.  
- **Fully Qualified Legislative Name (FQLN)**: A standardized identifier in the format `TYPE_SUBJECT_YYYYMMDD`.  
- **HoC**: House of Constituents, as defined in the **[Legislative Framework Act](./CA_LEGISLATIVEFRAMEWORK_20260401.md)**.

---

## Preamble
**WHEREAS** the Hudson Republic is founded upon a binary governance structure that preserves the separation of powers, upholds federal supremacy within enumerated jurisdiction, reserves residual powers to the Ridings, and safeguards the immutable rights of the Individual;

**AND WHEREAS** every legislative instrument — whether federal or Riding-level — must be immediately identifiable as to its class, purpose, subject matter, origin, and DVCS revision history;

**AND WHEREAS** a standardized **Fully Qualified Legislative Name (FQLN)** format promotes human readability, machine parseability, version control, automated auditing, searching, sorting, and long-term archival integrity through distributed version-control systems;

**NOW THEREFORE**, the Senate and House of Constituents of the Hudson Republic enact as follows:

---

## Section 1 — Classification of Legislative Instruments
The Republic establishes ten classes of legislative instrument. Constitutional Articles (CA) are exclusive to the federal level. All other classes may exist at the Riding level but remain subordinate to federal supremacy.

### CA — Constitutional Article
Constitutional Articles form the supreme law of the Republic and are divided into two distinct tiers:

### CA - Bedrock Constitutional Articles
- **Philosophy**: Unmoving and inviolable, akin to the Canadian Shield — permanent foundations that shall not be altered.  
- **Threshold**: Unanimous vote/verdict (100% or 12/12) as defined in the **[Clarity Act](./CA_CLARITYACT_20260522.md)** across three separate readings in both the House of Constituents and the Senate.  
- **Strategic Role**: These constitute the “source code” of the Republic, primarily protecting the core, inalienable rights of the Individual. Examples include **[The Individual (Sovereign) Act](./CA_THEINDIVIDUAL_20260401.md)**. Bedrock articles are intended to remain unchanged except in the most extraordinary circumstances.

### CA - Foundational Constitutional Articles
- **Philosophy**: Resilient and architectural — core to the effective functioning of the Republic, but capable of measured evolution to better protect the Republic as it grows or faces new challenges.  
- **Threshold**: Overwhelming Majority vote/verdict (75% or 9/12) as defined in the **[Clarity Act](./CA_CLARITYACT_20260522.md)** across three separate readings in both the House of Constituents and the Senate.  
- **Strategic Role**: These establish the essential operating mechanisms, institutions, and protocols of the Republic (e.g., legislative framework, territorial structure, judicial architecture, and monetary integrity).

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

### CO - LC Types
Legislative Codes (CO) are supporting instruments that provide detailed, systematized rules to implement parent legislation. There are six distinct types of Legal Codes:

- **Civil Codes**: Govern civil matters including lawsuits, reconciliation, contracts, agreements, terms and conditions.  
- **Criminal Codes**: Define criminal offenses, scope, nature of the crime, mitigating factors, punitive measures, and rehabilitation pathways.  
- **Trade Codes**: Regulate terms and conditions of trade, temporary transfers related to Obligation Papers, cross-border regulations, agreements, pacts, and binding clauses.  
- **Technology Codes**: Address processes, frameworks, technical documentation, regulations, specifications, and implementation procedures for specific technologies or innovations.  
- **Documentation Codes**: Govern the handling, formatting, marking, security features, legal dating, personally identifiable information, and stamps of approval for official documents.  
- **Other Codes**: Cover any specialized codes that fall outside the above categories.

All Legislative Codes (CO) must clearly declare their Legal Function type.

### LC — Legislative Challenge
* **Purpose**: Repeal, amendment, or decommissioning of existing legislation due to unconstitutionality or overreach.  
* **Enactment**: Senate applies the threshold required by the *challenged* instrument (e.g., 12/12 for CA challenges).

### SCH — Schedule
* **Purpose**: Lists, indexes, or technical specifications (e.g., tariff schedules).  
* **Enactment**: See Section 6.2 for detailed rules.

### FO — Forms
* **Purpose**: Administrative templates, licenses, and notices.  
* **Enactment**: Created or amended by the Executive Office; **no legislative readings required**. Void if they contradict parent legislation.

---

## Section 2 — Dependency Handling and Reference Rules

To preserve constitutional hierarchy and legislative integrity, every instrument must comply with the following dependency rules. No instrument may depend upon a lower-authority instrument in a manner that would undermine its own enactment threshold.

**Legislative Framework Dependency Tree**

![Dependency Tree](../../images/CA/CA_NAMINGCONVENTION_20260401/HUDSON_DEPENDENCYTREE.png)

### 2.1 General Dependency Tree Logic
- **Bedrock Constitutional Articles** may only depend upon other **Bedrock** Constitutional Articles.  
- **Foundational Constitutional Articles** may depend upon **Bedrock** or other **Foundational** Constitutional Articles.  
- Instruments requiring **two readings** (LA, LB) may depend upon instruments requiring two or three readings.  
- Instruments requiring **one reading** (OP, CO) may depend upon instruments requiring one, two, or three readings.  
- Instruments requiring **zero readings** (SCH, FO) are generally standalone but may list Hard Dependencies for transparency.

### 2.1.1 Special Rule — The Individual (Sovereign) Act
The **CA_THEINDIVIDUAL_20260401** is a **Bedrock** Constitutional Article. It shall be listed as a **Hard Dependency** only by other Constitutional Articles. All other legislative instruments shall treat it as an **implicit foundational dependency** by inheritance.

- It shall be listed as a **Hard Dependency** only by other **Constitutional Articles (CA)**.  
- All other legislative instruments (LA, CO, SCH, FO, etc.) shall treat **CA_THEINDIVIDUAL_20260401** as an **implicit foundational dependency** by inheritance. They are not required to list it explicitly.

This rule minimizes unnecessary dependency clutter while ensuring the immutable rights of the Individual remain the bedrock of the entire legislative framework.

### 2.2 Supporting Instruments — Schedules (SCH) and Forms (FO)
Schedules (SCH) and Forms (FO) are purely supporting instruments. They share the following rules:

- They always require a minimum of zero readings and a maximum of three readings.  
- They remain non-substantive. They cannot create new rights, obligations, or authorities independent of their parent instrument(s).  
- If a Schedule or Form is not depended upon by any instrument, it defaults to no readings in either legislative house.

#### 2.2.1 Schedules (SCH) — Special Rule
A Schedule (SCH) is a purely supporting instrument containing lists, indexes, technical specifications, tariffs, annexes, or similar material.  

- When a parent instrument depends upon a Schedule, the Schedule inherits the exact enactment threshold of that parent.

#### 2.2.2 Forms (FO) — Special Rule
Forms (FO) are administrative templates only and are non-binding.  

- Forms are created or amended by the Executive Office; **no legislative readings are required**.  
- When a parent instrument depends upon a Form, the Form inherits the exact enactment threshold of that parent.

### 2.3 Other Specific Dependency Rules
1. **Legislative Budgets (LB)**: May only depend upon Legislative Articles (LA) and Constitutional Articles (CA). This directionality is not reciprocal. They may not depend upon Schedules (SCH) or other Legislative Budgets (LB).  
2. **Legislative Articles (LA)**: May only depend upon other Legislative Articles (LA), Constitutional Articles (CA), and Schedules (SCH).  
3. **Legal Codes (CO)**: May only depend upon Constitutional Articles (CA), Legislative Articles (LA), other Legal Codes (CO) and Schedules (SCH). They may not depend upon budgetary instruments such as Legislative Budgets (LB) or Obligation Papers (OP).  
4. **Obligation Papers (OP)**: May only depend upon Constitutional Articles (CA), Legislative Articles (LA), Legal Codes (CO). They may not depend upon Schedules (SCH), Legislative Budgets (LB) or other Obligation Papers (OP).  
5. **Legislative Challenges (LC)**: Shall have no dependencies. As reforming, amending, or decommissioning instruments, LCs stand independent and may target any class of legislation.  
6. **Emergency Instruments (EL and EB)**: May only depend upon Constitutional Articles (CA). They must not depend upon any peacetime legislative instruments. No derivative legislative instruments may be created from an emergency instrument, as they carry an absolute, time-bound expiration.  
7. **Cultural Instruments (CULT)**: Federal cultural items and symbols are immutable and serve ceremonial, educational, or identity purposes only. They are not binding legislative instruments and carry no dependencies. They may only be terminated by a seventy-five percent (75%) citizen referendum held simultaneously in all Ridings of the Hudson Republic.

### 2.4 Temporal Inversions and Implicit Amendments
Any legislative dependency created by temporal inversion (e.g., an instrument referencing a successor instrument that technically precedes it in the registry) shall be automatically classified as an "Implicit Technical Amendment." Such dependencies are considered legally valid and compliant provided the Git commit metadata timestamp supports the chronological validity of the reference. This clause supersedes strict linear hierarchy validation for these specific instances.

1. **Presumption of Amendment**: The individual shall interpret this state as an implicit technical amendment to the implementation layers of the parent instrument, preserving the historical baseline of the parent law while consuming the updated dependency specification.
2. **Rogue Policy Injection Safeguard**: Because a temporal inversion bypasses synchronous bicameral readings, it shall automatically trigger a high-scrutiny cryptographic audit flag. 
3. **DVCS Verification Protocol**: To ensure the inversion does not mask a rogue policy injection, auditors must utilize the repository's native Distributed Version Control System (DVCS) functions (e.g., `git log -p` or `git diff`) to verify the exact commit history. The delta must prove that the dependency bump was executed by an authorized signature and carries purely administrative or technical adjustments aligned with the parent instrument's original intent.
4. **FQLN Date Field**: The FQLN date is when the legislation is drafted in first reading. Since git handles integrity and versioning the date field can be ignored from the dependency resolution process. The date field is used for acrhival purposses only.

---

## Section 3 — File Organization and Asset Management

To ensure long-term maintainability, clarity, and scalability of the legislative repository, all instruments shall follow this standardized file structure:

### 3.1 Legislative Text Files
All primary legislative text files shall be stored in:  
`[root]/laws/docs/[INSTRUMENT_TYPE]/[INSTRUMENT_FQLN].md`

### 3.2 Associated Image Assets
All supporting image assets (diagrams, dependency trees, charts, illustrations, etc.) for a specific instrument shall be stored in a dedicated subdirectory using the instrument’s full **FQLN** as the folder name:  
Individual image files may use any descriptive name, but best practice is to prefix the filename with the full **FQLN** followed by an underscore.
`[root]/laws/images/[INSTRUMENT_TYPE]/[INSTRUMENT_FQLN]/[FILENAME]`

### 3.3 Associated Attachment Assets
All supporting attachments assets (spreedsheets, pdfs, project source files, presentation files, etc.) for a specific instrument shall be stored in a dedicated subdirectory using the instrument’s full **FQLN** as the folder name:  
Individual attachment files may use any descriptive name, but best practice is to prefix the filename with the full **FQLN** followed by an underscore.
`[root]/laws/attachments/[INSTRUMENT_TYPE]/[INSTRUMENT_FQLN]/[FILENAME]`

This separation of legislative text, from attachments and visual assets streamlines repository maintenance, improves organization, and simplifies long-term archival and auditing.

---

## Section 4 — Purpose and Effect
This Act ensures machine-parseable legislative history, clear distinction between peacetime and emergency law, total transparency, auditable archival integrity, and a logically consistent dependency hierarchy that preserves constitutional supremacy, with particular protection for Bedrock provisions.

---

## Section EX1 — Dependency Examples

**EX1.1**  
A **Bedrock** Constitutional Article amending core individual rights must explicitly list **[CA_THEINDIVIDUAL_20260401](../CA/CA_THEINDIVIDUAL_20260401.md)** as a Hard Dependency.

**EX1.2**  
A **Foundational** Constitutional Article may depend upon Bedrock articles (e.g., referencing **[The Individual (Sovereign) Act](./CA_THEINDIVIDUAL_20260401.md)**) but the reverse is not permitted.

**EX1.3**  
A Schedule (SCH) such as **SCH_BULLIONDENOMINATIONS** lists only its direct parent and does not list **CA_THEINDIVIDUAL**.

**EX1.4**  
A Legal Code (CO) on criminal procedure does **not** list **CA_THEINDIVIDUAL_20260401** explicitly, but must still comply with its principles.

**EX1.5**  
If a new Constitutional Article is created that has no direct bearing on individual rights, it may still list **CA_THEINDIVIDUAL_20260401** for emphasis and clarity, but this is not mandatory.

## Section EX2 — Dependency and File Organization Examples

**EX2.1 — File Organization Example**  
For a Legislative Code with the FQLN **CO_HAZCHEMICALDISPOSAL_20260504**:
- Legislative text: `[root]/laws/docs/CO/CO_HAZCHEMICALDISPOSAL_20260504.md`
- Associated images: `[root]/laws/images/CO/CO_HAZCHEMICALDISPOSAL_20260504/CO_HAZCHEMICALDISPOSAL_20260504_DIAGRAM.png`
- Associated attachment: `[root]/laws/images/CO/CO_HAZCHEMICALDISPOSAL_20260504/CO_HAZCHEMICALDISPOSAL_20260504_ENVIRONMENTIMPACT.ods`

---

**Original Author**: 

**House Signature**: 

**Senate Signature**: 

**Executive Office Signature**: 

**FQLN**: CA_NAMINGCONVENTION_20260401
