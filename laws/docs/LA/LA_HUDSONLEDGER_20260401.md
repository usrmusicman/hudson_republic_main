# Hudson Ledger Act

---

## Hard Dependencies
List any legislative instrument(s) (in alphabetical order) that this article must depend on. List the FQLN(s) below. Any FQLN(s) mentioned in other sections are considered to be references and not actual dependencies.  
Only **Constitutional Articles (CA)** and **Legislative Articles (LA)** can be listed here.

Dependencies
* **[CA_LEGALTENDER_20260401](../CA/CA_LEGALTENDER_20260401.md)**  
* **[CA_THEINDIVIDUAL_20260401](../CA/CA_THEINDIVIDUAL_20260401.md)**

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
**2.2** Records must include: Unique 16-character hexadecimal ID, Date/Time ([YYYYYYYYYYYY]YYYY:MM:DD:hh:mm:SS), Institution code, Transaction type, and coin-type amounts.  
**2.3** Parties shall receive a standardized receipt as prima facie evidence of payment.  
**2.4** Citizens and residents shall have secure, real-time, no-cost access to their transaction history via authenticated interfaces.

---

## Section 3 — International Exchange Conversion Formulas (Transitional)
The gold spot price is the publicly available market price for 99.99%+ pure gold.

| Asset Form       | Direction       | Formula                                                                  |
|------------------|-----------------|--------------------------------------------------------------------------|
| Bars (99.5%)     | Fiat to Ledger  | (Fiat amount ÷ (0.995 × gold spot)) × (32,768 × Current Scaling Factor)  |
| Bars (99.5%)     | Ledger to Fiat  | (Ledger units ÷ (32,768 × Current Scaling Factor)) × (0.995 × gold spot) |
| Coins (95.0%)    | Fiat to Ledger  | (Fiat amount ÷ (0.95 × gold spot)) × (32,768 × Current Scaling Factor)   |
| Coins (95.0%)    | Ledger to Fiat  | (Ledger units ÷ (32,768 × Current Scaling Factor)) × (0.95 × gold spot)  |

---

## Section 4 — Ledger Recording Formats

### Denomination Recording Format
The standard transaction record format is as follows:

| Protocol Version | Timecode                                  | Action              | Country Code    | Riding Code                     | Business Code   | Year               | Entry Code                      | HGB1             | HGB8 | HSB1 | HSB8 | HCB1 | HCB8 | HCBZ (Optional) | Metal Code                  | Scaling Factor    | Integrity Hash |
|------------------|-------------------------------------------|---------------------|-----------------|---------------------------------|-----------------|--------------------|---------------------------------|------------------|------|------|------|------|------|-----------------|-----------------------------|-------------------|----------------|
| V[number]        | [YYYYYYYYYYYY]YYYY:MM:DD:HH:MM:SS         | [Type][Number]      | [3 upper-alpha] | [2 hex block][2 hex riding]     | [4 hex]-[4 hex] | [YYYYYYYYYYYY]YYYY | [4 hex]-[4 hex]-[4 hex]-[4 hex] | [Operation][Var] | 000  | 000  | 000  | 000  | 000  | 000             | [Metal Type][Form Factor]   | /[Scaling Factor] | [Hash]         |

### Transaction Recording Format
The standard transaction record format is as follows:

| Protocol Version | Timecode                                  | Action              | Riding Code                     | Business Code   | Entry Code                                      | Unadjusted Entry  | HGB1  | HGB8 | HSB1 | HSB8 | HCB1 | HCB8 | HCBZ (Optional) | Tax Bitshift | Taxation Adjustment  | HGB1  | HGB8 | HSB1 | HSB8 | HCB1 | HCB8 | HCBZ (Optional) | Adjusted Entry       | HGB1  | HGB8 | HSB1 | HSB8 | HCB1 | HCB8 | HCBZ (Optional) | Scaling Factor    | Integrity Hash |
|------------------|-------------------------------------------|---------------------|---------------------------------|-----------------|-------------------------------------------------|-------------------|-------|------|------|------|------|------|-----------------|--------------|----------------------|-------|------|------|------|------|------|-----------------|----------------------|-------|------|------|------|------|------|-----------------|-------------------|----------------|
| V[number]        | [YYYYYYYYYYYY]YYYY:MM:DD:HH:MM:SS         | [Type][Number]      | [2 hex block][2 hex riding]     | [4 hex]-[4 hex] | [4 hex]-[4 hex]-[4 hex]-[4 hex]-[4 hex]-[4 hex] | [Operation]u      | [Var] | 000  | 000  | 000  | 000  | 000  | 000             | >>[Number]   | [Operation]t         | [Var] | 000  | 000  | 000  | 000  | 000  | 000             | [Operation]a         | [Var] | 000  | 000  | 000  | 000  | 000  | 000             | /[Scaling Factor] | [Hash]         |

### Transaction and Denomination Fields
* **[YYYYYYYYYYYY]**: This is the invisible extension to prevent millennium bugs.  
* **[2 hex block]**: This is the riding block routing address.  
* **[2 hex riding]**: This is the individual riding routing address.  
* **HGB1**: Gold beaver 1 oz field (variable length decimal base10 value).  
* **HGB8, HSB1, HSB8, HCB1, HCB8, HCBZ**: Represented as a 7-coin segment in octal, recorded in binary.

---

## Section 5 — Internal Tracking and Identification

All physical bullion instruments (coins, rounds, and bars) within the Hudson Republic shall be assigned a unique, machine-readable transaction receipt identifier upon XRF verification and entry into the system. This identifier serves as a permanent receipt and custody record for auditing, banking, circulation, and enforcement purposes. It is **not** a representation of monetary value, but rather a verifiable record of provenance, custody status, and physical specifications.

## Section 6 — Emergency Liquidity Re-scaling Protocol

**6.1 Activation**  
A Monetary Emergency and associated Ledger re-scaling may be activated solely by:  
- Formal declaration of a Monetary Emergency by the National Representative, and  
- An Overwhelming Majority verdict of the Senate (as defined in the **[Clarity Act](./CA_CLARITYACT_20260522.md)**).  

This activation shall be treated as Emergency Legislation.

**6.2 Available Scaling Factors and Tariff Measures**  
During a declared Monetary Emergency, the chosen scaling factor (2x, 4x, or 8x) shall be applied to copper Ledger Units. Concurrently, a **100% tariff** (equivalent to a bitshift of `>>0`) shall be imposed on all affected inbound transactions for the duration of the emergency.  

The National Representative shall retain discretion to adjust the tariff rate downward (through lower bitshift values) in consultation with the Senate when circumstances so warrant. Any such adjustment must be publicly announced and recorded on the Hudson Ledger.

**6.3 Duration, Step-Down, and Review**  
- The initial activation of a Monetary Emergency shall not exceed ninety (90) days.  
- The scaling factor and associated tariff measures shall be subject to monthly review by the Senate.  
- Upon return to normal operations, a mandatory step-down procedure must be enacted through a dedicated **Obligation Paper** bearing the exact FQLN: `OP_BBNORMALMULTIPLIERTRANSITION_[YYYYYYYYYYYY]YYYYMMDD.md`.  
- The step-down shall proceed gradually by one bitshift to the right per quarter (three months) until the standard tariff rate is restored (e.g., 100% → 50% → 25% → normal).  
- The full transition period shall not exceed four quarters: one quarter at full emergency scaling and tariff, followed by up to three quarters of step-down.

**6.4 Accounting Treatment**  
Accounting software and systems shall implement the scaling factor as a global multiplier applied exclusively to the (1/8) troy ounce copper ledger unit while strictly preserving the constitutional 64:64:8 bullion ratios. All emergency measures, including the associated tariff, must be fully auditable and accompanied by clear public notice on the Hudson Ledger.  

The scaling factor formally declared by the National Representative (with Senate approval) shall constitute the sole official and legally binding scaling factor during both normal and emergency periods.

**6.5 Reversion**  
Failure to enact the required Obligation Paper for step-down shall result in the automatic reversion to normal scaling factors and tariff rates at the conclusion of the declared emergency period.

## Section 7 - Scaling Tables

**7.1 Bullion beaver (1x scaling, no liquidity injection) - Regular (displayed), 5 octet representation**

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

**7.2 Bullion beaver (1x scaling, no liquidity injection) - Backend Math (in memory), 6 octet representation**

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

**7.3 Bullion beaver (2x scaling liquidity injection)**

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

**7.4 Bullion beaver (4x scaling liquidity injection)**

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

**7.5 Bullion beaver (8x scaling liquidity injection)**

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

## Section 8 - Sign interpretation.

A plus (+) sign = This is used to add entries and add or accumulate amounts.
A minus (-) sign = This is used to remove entries and subtract amounts.
A tilde (~) sign = This is used as a neutral symbol or a value of zero (0).

---

**Original Author**: 

**House Signature**: 

**Senate Signature**: 

**Executive Office Signature**: 

**FQLN**: LA_HUDSONLEDGER_20260401
