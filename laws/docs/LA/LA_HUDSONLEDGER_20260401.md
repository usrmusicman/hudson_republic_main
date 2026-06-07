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

| ID (16-char hex) | DATE (YYYYMMDD:hhmmSSss)  | INST (8-char hex) | TYPE (16-alpha) | HGB   | HGB8 | HSB | HSB8 | HCB | HCB8 |
|------------------|---------------------------|-------------------|-----------------|-------|------|-----|------|-----|------|
| [Signature]      | [Timestamp]               | [Inst. Code]      | [Type Code]     | [Var] | 000  | 000 | 000  | 000 | 000  |

### Transaction Amount
* **HGB**: Gold beaver 1 oz field (variable length binary).  
* **Others**: Represented as a 7-coin segment in octal, recorded in binary.

---

## Section 4 — Internal Tracking and Identification

All physical bullion instruments (coins, rounds, and bars) within the Hudson Republic shall be assigned a unique, machine-readable transaction receipt identifier upon XRF verification and entry into the system. This identifier serves as a permanent receipt and custody record for auditing, banking, circulation, and enforcement purposes. It is **not** a representation of monetary value, but rather a verifiable record of provenance, custody status, and physical specifications.

### Hudson Ledger Transaction Receipt Format
**Format**: `U-YYYY-XXXXXXXXXXXXXXTT`

| Field          | Length | Base        | Description                                  |
|----------------|--------|-------------|----------------------------------------------|
| U              | 1      | Octal (0-7) | Usage Type / Custody State                   |
| YYYY           | 4      | Decimal     | Year of entry into the system                |
| XXXXXXXXXXXXXX | 14     | Hexadecimal | Randomly generated unique transaction record |
| TT             | 2      | Hexadecimal | Randomly generated unique transaction record |

#### Field 1 — Usage Type (Octal)
| Code | Description                                                            |
|------|------------------------------------------------------------------------|
| 0    | Institutional Vault (99.5% Min Purity Bars / Central Bank Reserves)    |
| 1    | Standard Merchant Circulation (95% Min Purity Coins / Rounds)          |
| 2    | Sovereign Mint Deep Storage (Unissued / National Treasure)             |
| 3    | Escrow / Seized Assets (Under law enforcement or court audit)          |
| 4    | In-Transit (Moving securely between commercial banks or mints)         |
| 5    | Industrial / Industrial Refining Pool (Scheduled for melting/assaying) |
| 6    | Reserved for Future Legislative Use                                    |
| 7    | Reserved for Future Legislative Use                                    |

#### Field 3 — Origin Nation and Metal Specifications (Rightmost 2 Hex Characters)
The rightmost two hexadecimal characters of Field 3 encode critical physical and provenance data:

- **Second rightmost character**: Origin Region (after XRF verification)
- **Rightmost character**: Metal type and weight class

**Origin Nations (Second Rightmost Character)**
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

**Metal Class and Weight (Rightmost Character)**
| Code | Metal                     | Weight    | Notes            |
|------|---------------------------|-----------|------------------|
| 0    | Copper                    | (1/10) oz | Low value        |
| 1    | Copper                    | (1/8) oz  | Low value        |
| 2    | Copper                    | (1/4) oz  | Low value        |
| 3    | Copper                    | (1/2) oz  | Low value        |
| 4    | Copper                    | (1) oz    | Low value        |
| 5    | Silver                    | (1/10) oz | Medium value     |
| 6    | Silver                    | (1/8) oz  | Medium value     |
| 7    | Silver                    | (1/4) oz  | Medium value     |
| 8    | Silver                    | (1/2) oz  | Medium value     |
| 9    | Silver                    | (1) oz    | Medium value     |
| A    | Gold                      | (1/10) oz | High value       |
| B    | Gold                      | (1/8) oz  | High value       |
| C    | Gold                      | (1/4) oz  | High value       |
| D    | Gold                      | (1/2) oz  | High value       |
| E    | Gold                      | (1) oz    | High value       |
| F    | Unspecified / Counterfeit | N/A       | Automatic reject |

The remaining 14 leftmost hexadecimal characters in Field 3 are randomly generated, providing an astronomically large collision-resistant address space.

**Original Author**: 

**House Signature**: 

**Senate Signature**: 

**Executive Office Signature**: 

**FQLN**: LA_HUDSONLEDGER_20260401
