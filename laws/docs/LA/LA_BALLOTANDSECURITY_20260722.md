# Ballot and Security Act

---

## Hard Dependencies
List any legislative instrument(s) (in alphabetical order) that this article must depend on. List the FQLN(s) below. Any FQLN(s) mentioned in other sections are considered to be references and not actual dependencies.  
Only **Constitutional Articles (CA)** and **Legislative Articles (LA)** can be listed here.

* **[CA_CLARITYACT_20260522](../CA/CA_CLARITYACT_20260522.md)**  
* **[CA_ELECTIONS_20260401](../CA/CA_ELECTIONS_20260401.md)**  
* **[CA_THEINDIVIDUAL_20260401](../CA/CA_THEINDIVIDUAL_20260401.md)**

---

## Definitions

- **Digital Casted Ballot**: The primary electronic record of a voter's choice, secured with cryptographic hashing.  
- **Paper Backup Ballot**: Physical ballot used as a verifiable backup and audit trail.

---

## Preamble

This Act establishes the standards for ballot design, casting, security, and verification in all Hudson Republic elections. It prioritizes integrity, auditability, and scalability for large ridings through a hybrid digital + paper system.

---

## Section 1 — Ballot Specifications

**1.1 General Election Ballot (Paper Backup)**  
- **Format**: Single-sided (to prevent bleed-through), Legal Size (8.5" × 14").  
- **Layout**: Vertical stack of 4 large OMR / write-in boxes (one per role).  
- **Voting Style**: Optical Mark Recognition (OMR) with generous write-in fields.  
- **Reference**: See **[FO_GENERALPAPERBALLOT_20260722](../FO/FO_GENERALPAPERBALLOT_20260722.md)**.

**1.2 Bi-Election Ballot (Paper Backup)**  
- **Format**: Single-sided, single-role contest.  
- **Layout**: Two-column horizontal design.  
- **Voting Style**: Optical Mark Recognition (OMR) with write-in option.  
- **Reference**: See **[FO_BYELECTIONPAPERBALLOT_20260722](../FO/FO_BYELECTIONPAPERBALLOT_20260722.md)**.

---

## Section 2 — Digital Casted Ballot Record

**2.1 Format** (fields separated by vertical bars)  
`[Candidate ID Number]|[Candidate Name]|[Riding Name]|[Riding Code]|[Voter ID Number]|[Station Officer ID Number]|[Unique Hash]`

- **Candidate ID Number**: Decimal 0–199 (max 200 candidates per riding).  
- **Candidate Name**: Legal name of the candidate.  
- **Riding Name**: Name of the riding.  
- **Riding Code**: 4-character hexadecimal.  
- **Voter ID Number**: Random decimal 0–999,999,999 per election.  
- **Station Officer ID Number**: 12-character hexadecimal badge.  
- **Unique Hash**: Cryptographic hash for integrity.

---

## Section 3 — Casting Procedures

### Digital Ballot
The Station Officer must:

1. Authenticate the voter using both photo ID and Voter ID Pass.  
2. Type the Voter ID Pass number and their badge number into the master terminal to arm the one-time ballot authorization.  
3. The voter completes all prompts on the voting terminal.  
4. Each session is recorded as a Digital Casted Ballot Record (DCBR).  
5. The original VIP pass is shredded and discarded.

### Paper Ballot
The Station Officer must:

1. Authenticate the voter using both photo ID and Voter ID Pass.  
2. Provide the voter with a paper ballot (4 blank OMR boxes) and the candidate menu booklet.  
3. The voter marks the ballot and places it in a secure envelope into the ballot box.  
4. The Station Officer records Voter ID Number and Station Officer ID Number. Other fields remain blank until counting at the Subzone Election Office per the **[Postal System Act](../LA/LA_POSTALSYSTEM_20260528.md)**.  
5. The original VIP pass is shredded and discarded.

---

## Section 4 — Security and Verification

**4.1** All digital ballots are hashed with SHA3-512 and timestamped.  
**4.2** Paper backups are stored in tamper-evident, GPS-tracked containers.  
**4.3** Full audit trail available under Freedom of Information.

---

**Original Author**: 

**House Signature**: 

**Senate Signature**: 

**Executive Office Signature**: 

**FQLN**: LA_BALLOTANDSECURITY_20260722
