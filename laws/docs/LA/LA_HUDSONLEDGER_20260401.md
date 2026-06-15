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

| ID (16-char hex) | DATE ([YYYYYYYYYYYY]YYYY:MM:DD:HH:MM:SS)  | INST (8-char hex) | TYPE (16-alpha) | HGB1  | HGB8 | HSB1 | HSB8 | HCB1 | HCB8 |
|------------------|-------------------------------------------|-------------------|-----------------|-------|------|------|------|------|------|
| [Signature]      | [Timestamp]                               | [Inst. Code]      | [Type Code]     | [Var] | 000  | 000  | 000  | 000  | 000  |

### Transaction Amount
* **[YYYYYYYYYYYY]**: This is the invisible extension to prevent millennium bugs.
* **HGB**: Gold beaver 1 oz field (variable length binary).  
* **Others**: Represented as a 7-coin segment in octal, recorded in binary.

---

## Section 4 — Internal Tracking and Identification

All physical bullion instruments (coins, rounds, and bars) within the Hudson Republic shall be assigned a unique, machine-readable transaction receipt identifier upon XRF verification and entry into the system. This identifier serves as a permanent receipt and custody record for auditing, banking, circulation, and enforcement purposes. It is **not** a representation of monetary value, but rather a verifiable record of provenance, custody status, and physical specifications.

### Hudson Ledger Transaction Receipt Format
**Format**: `XXXX-XXXX-XXXX-XXXX`

| Field               | Length | Base        | Description                                  |
|---------------------|--------|-------------|----------------------------------------------|
| XXXX-XXXX-XXXX-XXXX | 16     | Hexadecimal | Randomly generated unique transaction record |

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
- Upon return to normal operations, a step-down procedure must be enacted via a dedicated **Obligation Paper** with the exact FQLN: `OP_BBNORMALMULTIPLIERTRANSITION_[YYYYYYYYYYYY]YYYYMMDD.md` (where [YYYYYYYYYYYY]YYYYMMDD is the tabling date and [YYYYYYYYYYYY] is an invisible extension).  
- The step-down shall occur gradually (e.g., 4x → 2x → normal) quarter-to-quarter to mitigate transitional shocks.  
- The theoretical maximum for a change period is 4 quarters: 1 quarter of emergency ratio change and a maximum of 3 quarters for the step-down period.

**5.4 Accounting Treatment**  
Accounting software shall implement the scaling factor as a global multiplier on (1/8) troy oz copper ledger units while preserving the constitutional 64:64:8 ratios. All changes must be fully auditable on the Hudson Ledger with clear public notice.

**5.5 Reversion**  
Failure to pass the required Obligation Paper for step-down shall result in automatic reversion to normal scaling at the end of the declared emergency period.

## Section 6 - Scaling Tables

**6.1 Bullion beaver (1x scaling, no liquidity injection) - Regular (displayed), 5 octet representation**

| Power of 2 | Binary Amount         | Unit Description | Amount in HCB8 |
|------------|-----------------------|------------------|----------------|
| 2^0        | 0.000.000.000.000.001 | 1/8 copper oz    | 1 HCB8         |
| 2^1        | 0.000.000.000.000.010 | None             | 2 HCB8         |
| 2^2        | 0.000.000.000.000.100 | None             | 4 HCB8         |
| 2^3        | 0.000.000.000.001.000 | 1 copper oz      | 8 HCB8         |
| 2^4        | 0.000.000.000.010.000 | None             | 16 HCB8        |
| 2^5        | 0.000.000.000.100.000 | None             | 32 HCB8        |
| 2^6        | 0.000.000.001.000.000 | 1/8 silver oz    | 64 HCB8        |
| 2^7        | 0.000.000.010.000.000 | None             | 128 HCB8       |
| 2^8        | 0.000.000.100.000.000 | None             | 256 HCB8       |
| 2^9        | 0.000.001.000.000.000 | 1 silver oz      | 512 HCB8       |
| 2^10       | 0.000.010.000.000.000 | None             | 1,024 HCB8     |
| 2^11       | 0.000.100.000.000.000 | None             | 2,048 HCB8     |
| 2^12       | 0.001.000.000.000.000 | 1/8 gold oz      | 4,096 HCB8     |
| 2^13       | 0.010.000.000.000.000 | None             | 8,192 HCB8     |
| 2^14       | 0.100.000.000.000.000 | None             | 16,384 HCB8    |
| 2^15       | 1.000.000.000.000.000 | 1 gold oz        | 32,768 HCB8    |

**6.2 Bullion beaver (1x scaling, no liquidity injection) - Backend Math (in memory), 6 octet representation**

| Power of 2 | Binary Amount             | Unit Description | Amount in HCB8 |
|------------|---------------------------|------------------|----------------|
| 2^0        | 0.000.000.000.000.001.000 | 1/8 copper oz    | 1 HCB8         |
| 2^1        | 0.000.000.000.000.010.000 | None             | 2 HCB8         |
| 2^2        | 0.000.000.000.000.100.000 | None             | 4 HCB8         |
| 2^3        | 0.000.000.000.001.000.000 | 1 copper oz      | 8 HCB8         |
| 2^4        | 0.000.000.000.010.000.000 | None             | 16 HCB8        |
| 2^5        | 0.000.000.000.100.000.000 | None             | 32 HCB8        |
| 2^6        | 0.000.000.001.000.000.000 | 1/8 silver oz    | 64 HCB8        |
| 2^7        | 0.000.000.010.000.000.000 | None             | 128 HCB8       |
| 2^8        | 0.000.000.100.000.000.000 | None             | 256 HCB8       |
| 2^9        | 0.000.001.000.000.000.000 | 1 silver oz      | 512 HCB8       |
| 2^10       | 0.000.010.000.000.000.000 | None             | 1,024 HCB8     |
| 2^11       | 0.000.100.000.000.000.000 | None             | 2,048 HCB8     |
| 2^12       | 0.001.000.000.000.000.000 | 1/8 gold oz      | 4,096 HCB8     |
| 2^13       | 0.010.000.000.000.000.000 | None             | 8,192 HCB8     |
| 2^14       | 0.100.000.000.000.000.000 | None             | 16,384 HCB8    |
| 2^15       | 1.000.000.000.000.000.000 | 1 gold oz        | 32,768 HCB8    |

**6.3 Bullion beaver (2x scaling liquidity injection)**

| Power of 2 | Binary Amount             | Unit Description | Amount in HCB8 |
|------------|---------------------------|------------------|----------------|
| 2^0        | 0.000.000.000.000.000.100 | 1/8 copper oz    | 1 HCB8         |
| 2^1        | 0.000.000.000.000.001.000 | None             | 2 HCB8         |
| 2^2        | 0.000.000.000.000.010.000 | None             | 4 HCB8         |
| 2^3        | 0.000.000.000.000.100.000 | 1 copper oz      | 8 HCB8         |
| 2^4        | 0.000.000.000.001.000.000 | None             | 16 HCB8        |
| 2^5        | 0.000.000.000.010.000.000 | None             | 32 HCB8        |
| 2^6        | 0.000.000.000.100.000.000 | None             | 64 HCB8        |
| 2^7        | 0.000.000.001.000.000.000 | 1/8 silver oz    | 128 HCB8       |
| 2^8        | 0.000.000.010.000.000.000 | None             | 256 HCB8       |
| 2^9        | 0.000.000.100.000.000.000 | None             | 512 HCB8       |
| 2^10       | 0.000.001.000.000.000.000 | 1 silver oz      | 1,024 HCB8     |
| 2^11       | 0.000.010.000.000.000.000 | None             | 2,048 HCB8     |
| 2^12       | 0.000.100.000.000.000.000 | None             | 4,096 HCB8     |
| 2^13       | 0.001.000.000.000.000.000 | 1/8 gold oz      | 8,192 HCB8     |
| 2^14       | 0.010.000.000.000.000.000 | None             | 16,384 HCB8    |
| 2^15       | 0.100.000.000.000.000.000 | None             | 32,768 HCB8    |
| 2^16       | 1.000.000.000.000.000.000 | 1 gold oz        | 65,536 HCB8    |

**6.4 Bullion beaver (4x scaling liquidity injection)**

| Power of 2 | Binary Amount             | Unit Description | Amount in HCB8 |
|------------|---------------------------|------------------|----------------|
| 2^0        | 0.000.000.000.000.000.010 | 1/8 copper oz    | 1 HCB8         |
| 2^1        | 0.000.000.000.000.000.100 | None             | 2 HCB8         |
| 2^2        | 0.000.000.000.000.001.000 | None             | 4 HCB8         |
| 2^3        | 0.000.000.000.000.010.000 | 1 copper oz      | 8 HCB8         |
| 2^4        | 0.000.000.000.000.100.000 | None             | 16 HCB8        |
| 2^5        | 0.000.000.000.001.000.000 | None             | 32 HCB8        |
| 2^6        | 0.000.000.000.010.000.000 | None             | 64 HCB8        |
| 2^7        | 0.000.000.000.100.000.000 | None             | 128 HCB8       |
| 2^8        | 0.000.000.001.000.000.000 | 1/8 silver oz    | 256 HCB8       |
| 2^9        | 0.000.000.010.000.000.000 | None             | 512 HCB8       |
| 2^10       | 0.000.000.100.000.000.000 | None             | 1,024 HCB8     |
| 2^11       | 0.000.001.000.000.000.000 | 1 silver oz      | 2,048 HCB8     |
| 2^12       | 0.000.010.000.000.000.000 | None             | 4,096 HCB8     |
| 2^13       | 0.000.100.000.000.000.000 | None             | 8,192 HCB8     |
| 2^14       | 0.001.000.000.000.000.000 | 1/8 gold oz      | 16,384 HCB8    |
| 2^15       | 0.010.000.000.000.000.000 | None             | 32,768 HCB8    |
| 2^16       | 0.100.000.000.000.000.000 | None             | 65,536 HCB8    |
| 2^17       | 1.000.000.000.000.000.000 | 1 gold oz        | 131,072 HCB8   |

**6.5 Bullion beaver (8x scaling liquidity injection)**

| Power of 2 | Binary Amount             | Unit Description | Amount in HCB8 |
|------------|---------------------------|------------------|----------------|
| 2^0        | 0.000.000.000.000.000.001 | 1/8 copper oz    | 1 HCB8         |
| 2^1        | 0.000.000.000.000.000.010 | None             | 2 HCB8         |
| 2^2        | 0.000.000.000.000.000.100 | None             | 4 HCB8         |
| 2^3        | 0.000.000.000.000.001.000 | 1 copper oz      | 8 HCB8         |
| 2^4        | 0.000.000.000.000.010.000 | None             | 16 HCB8        |
| 2^5        | 0.000.000.000.000.100.000 | None             | 32 HCB8        |
| 2^6        | 0.000.000.000.001.000.000 | None             | 64 HCB8        |
| 2^7        | 0.000.000.000.010.000.000 | None             | 128 HCB8       |
| 2^8        | 0.000.000.000.100.000.000 | None             | 256 HCB8       |
| 2^9        | 0.000.000.001.000.000.000 | 1/8 silver oz    | 512 HCB8       |
| 2^10       | 0.000.000.010.000.000.000 | None             | 1,024 HCB8     |
| 2^11       | 0.000.000.100.000.000.000 | None             | 2,048 HCB8     |
| 2^12       | 0.000.001.000.000.000.000 | 1 silver oz      | 4,096 HCB8     |
| 2^13       | 0.000.010.000.000.000.000 | None             | 8,192 HCB8     |
| 2^14       | 0.000.100.000.000.000.000 | None             | 16,384 HCB8    |
| 2^15       | 0.001.000.000.000.000.000 | 1/8 gold oz      | 32,768 HCB8    |
| 2^16       | 0.010.000.000.000.000.000 | None             | 65,536 HCB8    |
| 2^17       | 0.100.000.000.000.000.000 | None             | 131,072 HCB8   |
| 2^18       | 1.000.000.000.000.000.000 | 1 gold oz        | 262,144 HCB8   |

## Section 7 - Sign interpretation.

A plus (+) sign = Thiss iss used to add entries and add or accumulate amounts.
A minus (-) sign = This is used to remove entries and subtract amounts.
A tilda (~) sign = This is used as a neutral symbol or a value of zero (0).

---

**Original Author**: 

**House Signature**: 

**Senate Signature**: 

**Executive Office Signature**: 

**FQLN**: LA_HUDSONLEDGER_20260401
