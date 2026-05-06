# Hudson Ledger Act

---

## Hard Dependencies
List any legislative instrument(s) (in alphabetical order) that this article must depend on. List the FQLN(s) below. Any FLQN(s) mentioned in other sections are considered to be references and not actual dependencies.  
Only **Constitutional Articles (CA)**, **Legislative Articles (LA)** and **Schedules (SCH)** can be listed here.

Dependencies
* **[CA_LEGALTENDER_20260401](../CA/CA_LEGALTENDER_20260401.md)**  

---

## Definitions
All capitalized terms used in this Act shall be interpreted in accordance with their definitions in the referenced instruments below.

- **Hudson Ledger**: The official, tamper-evident and cryptographically signed electronic record-keeping system for all bullion transactions and Ledger credits.  
- **Ledger Unit**: The base indivisible accounting denomination, equal to 1/8 troy ounce of 95% pure copper bullion.

---

## Preamble
This Act governs the Hudson Ledger, the official electronic record-keeping system for all bullion transactions and Ledger credits in the Hudson Republic. The Ledger ensures all transactions are cryptographically signed, publicly auditable, and enforceable as legal tender equivalents, in full conformity with the rights of the Individual as protected under **[The Individual (Sovereign) Act](../CA/CA_THEINDIVIDUAL_20260401.md)**.

---

## Section 1 — Hudson Ledger System
**1.1** The Hudson Ledger is the sole official, immutable, cryptographically signed electronic record for bullion transactions and Ledger credits.  
**1.2** All Ledger entries shall be publicly auditable, binding, and enforceable as legal tender equivalents.  
**1.3** Transactions recorded on the Hudson Ledger may be net-settled annually between institutions in physical bullion per the **[Banking and Reserves Act](../CA/CA_BANKANDRESERVE_20260401.md)**.

---

## Section 2 — Transaction Recording and Access
**2.1** All transactions shall be recorded on the Hudson Ledger in real time.  
**2.2** Records must include: Unique 16-character hexadecimal ID, Date/Time (YYYYMMDD:hhmmSSss), Institution code, Transaction type, and coin-type amounts.  
**2.3** Parties shall receive a standardized receipt as prima facie evidence of payment.  
**2.4** Citizens and residents shall have secure, real-time, no-cost access to their transaction history via authenticated interfaces.

---

## Section 3 — Transaction Recording Format
**3.1** The standard transaction record format is as follows:

| ID (16-char hex) | DATE (YYYYMMDD:hhmmSSss) | INST (8-char hex) | TYPE (16-alpha) | HGB | HGB8 | HSB | HSB8 | HCB | HCB8 |
|------------------|---------------------------|-------------------|-----------------|-----|------|-----|------|-----|------|
| [Signature]      | [Timestamp]               | [Inst. Code]      | [Type Code]     | [Var] | 000 | 000 | 000 | 000 | 000 |

* **HGB**: Gold beaver 1 oz field (variable length binary).  
* **Others**: Represented as a 7-coin segment in octal, recorded in binary.

---

**Original Author**: 

**House Signature**: 

**Senate Signature**: 

**Executive Office Signature**: 

**FQLN**: LA_HUDSONLEDGER_20260401
