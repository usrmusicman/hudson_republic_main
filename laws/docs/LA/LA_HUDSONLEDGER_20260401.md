# Hudson Ledger Act

---

## Hard Dependencies
List any legislative instrument(s) (in alphabetical order) that this article must depend on. List the FQLN(s) below. Any FQLN(s) mentioned in other sections are considered to be references and not actual dependencies.  
Only **Constitutional Articles (CA)** and **Legislative Articles (LA)** can be listed here.

Dependencies
* **[CA_LEGALTENDER_20260401](../CA/CA_LEGALTENDER_20260401.md)**  
* **[CA_THEINDIVIDUAL_20260401](./CA_THEINDIVIDUAL_20260401.md)**

---

## Definitions
All capitalized terms used in this Act shall be interpreted in accordance with their definitions in the referenced instruments below.

- **Hudson Ledger**: The official, tamper-evident and cryptographically signed electronic record-keeping system for all bullion transactions and Ledger credits.  
- **Ledger Unit**: The base indivisible accounting denomination, equal to 1/8 troy ounce of 95% pure copper bullion.  
- **Scaling Factor**: A temporary multiplier (2x, 4x, or 8x) applied to the interpretation of copper Ledger Units during a declared Monetary Emergency.

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
The standard transaction record format is as follows:

| ID (16-char hex) | DATE (YYYYMMDD:hhmmSSss)  | INST (8-char hex) | TYPE (16-alpha) | HGB1  | HGB8 | HSB1 | HSB8 | HCB1 | HCB8 |
|------------------|---------------------------|-------------------|-----------------|-------|------|------|------|------|------|
| [Signature]      | [Timestamp]               | [Inst. Code]      | [Type Code]     | [Var] | 000  | 000  | 000  | 000  | 000  |

### Transaction Amount
* **HGB**: Gold beaver 1 oz field (variable length binary).  
* **Others**: Represented as a 7-coin segment in octal, recorded in binary.

---

## Section 4 — Internal Tracking and Identification

All physical bullion instruments (coins, rounds, and bars) within the Hudson Republic shall be assigned a unique, machine-readable transaction receipt identifier upon XRF verification and entry into the system. This identifier serves as a permanent receipt and custody record for auditing, banking, circulation, and enforcement purposes. It is **not** a representation of monetary value, but rather a verifiable record of provenance, custody status, and physical specifications.

### Hudson Ledger Transaction Receipt Format
**Format**: `YYYY-XXXXXXXXXXXXXXTT`

| Field          | Length | Base        | Description                                  |
|----------------|--------|-------------|----------------------------------------------|
| YYYY           | 4      | Decimal     | Year of entry into the system                |
| XXXXXXXXXXXXXX | 14     | Hexadecimal | Randomly generated unique transaction record |
| TT             | 2      | Hexadecimal | Origin Nation + Metal/Weight Code            |

### Origin Nation and Metal Specifications (Rightmost 2 Hex Characters)
The rightmost two hexadecimal characters of Field 3 encode critical physical and provenance data:

- **Second rightmost character**: Origin Region (after XRF verification)
- **Rightmost character**: Metal type and weight class

**Origin Nations (First "T" Character)**
| Code | Nation / Origin                                   |
|------|---------------------------------------------------|
| 0    | Hudson Republic                                   |
| 1    | Canada                                            |
| 2    | Australia                                         |
| 3    | America                                           |
| 4    | Britan                                            |
| 5    | South Africa                                      |
| 6    | Austria                                           |
| 7    | Mexico                                            |
| 8    | France                                            |
| 9    | China                                             |
| A    | Russia                                            |
| B    | Placeholder                                       |
| C    | Placeholder                                       |
| D    | Placeholder                                       |
| E    | Placeholder                                       |
| F    | Other / Unknown / Private Minted Round            |

**Metal Class and Weight (Second "T" Character)**
| Code | Metal                     | Weight    | Notes                                              |
|------|---------------------------|-----------|----------------------------------------------------|
| 0    | Copper                    | (1/8) oz  | Low value                                          |
| 1    | Copper                    | (1/4) oz  | Low value                                          |
| 2    | Copper                    | (1/2) oz  | Low value                                          |
| 3    | Copper                    | (1) oz    | Low value                                          |
| 4    | Silver                    | (1/8) oz  | Low value                                          |
| 5    | Silver                    | (1/4) oz  | Low value                                          |
| 6    | Silver                    | (1/2) oz  | Low value                                          |
| 7    | Silver                    | (1) oz    | Low value                                          |
| 8    | Gold                      | (1/8) oz  | High value                                         |
| 9    | Gold                      | (1/4) oz  | High value                                         |
| A    | Gold                      | (1/2) oz  | High value                                         |
| B    | Gold                      | (1) oz    | High value                                         |
| C    | Gold                      | (5) oz    | High value (Institutional Bars Only)               |
| D    | Gold                      | (10) oz   | High value (Institutional Bars Only)               |
| E    | Gold                      | (100) oz  | High value (Institutional Bars Only)               |
| F    | Unspecified / Suspicious  | N/A       | Can only be verified at an FHI insured institution |

The remaining 14 leftmost hexadecimal characters in Field 3 are randomly generated, providing an astronomically large collision-resistant address space.

## Section 5 — Emergency Liquidity Re-scaling Protocol

**5.1 Activation**  
A Monetary Emergency and associated Ledger re-scaling may be activated only by:  
- Overwhelming Majority verdict in the Senate (as defined in the **[Clarity Act](./CA_CLARITYACT_20260522.md)**), and  
- Signature of the National Representative.  

This shall be treated as Emergency Legislation.

**5.2 Available Scaling Factors**  
- **2x Scaling**: Treats 1/2 oz copper ledger position as the new 1 oz baseline (effective ratios shift to 64:128:4).  
- **4x Scaling**: Treats 1/4 oz copper ledger position as the new 1 oz baseline (effective ratios shift to 64:256:2).  
- **8x Scaling**: Treats the base 1/8 oz copper HCB8 ledger unit position as a full 1 oz baseline (maximum liquidity boost) (effective ratios shift to 64:512:1).

**5.3 Duration and Review**  
- Initial activation shall not exceed 90 days.  
- The scaling shall be reviewed monthly by the Senate.  
- Upon return to normal operations, a step-down procedure must be enacted via a dedicated **Obligation Paper** with the exact FQLN: `OP_BBNORMALMULTIPLIERTRANSITION_YYYYMMDD.md` (where YYYYMMDD is the tabling date).  
- The step-down shall occur gradually (e.g., 4x → 2x → normal) quarter-to-quarter to mitigate transitional shocks.  
- The theoretical maximum for a change period is 4 quarters: 1 quarter of emergency ratio change and a maximum of 3 quarters for the step-down period.

**5.4 Accounting Treatment**  
Accounting software shall implement the scaling factor as a global multiplier on (1/8) troy oz copper ledger units while preserving the constitutional 64:64:8 ratios. All changes must be fully auditable on the Hudson Ledger with clear public notice.

**5.5 Reversion**  
Failure to pass the required Obligation Paper for step-down shall result in automatic reversion to normal scaling at the end of the declared emergency period.

---

**Original Author**: 

**House Signature**: 

**Senate Signature**: 

**Executive Office Signature**: 

**FQLN**: LA_HUDSONLEDGER_20260401
