# Hudson Denomination Ledger Schedule

---

## Hard Dependencies
List any legislative instrument(s) (in alphabetical order) that this article must depend on. List the FQLN(s) below. Any FQLN(s) mentioned in other sections are considered to be references and not actual dependencies.  
Only **Constitutional Articles (CA)**, **Legislative Articles (LA)** and **Legislative Codes (CO)** can be listed here.

* **[LA_HUDSONLEDGER_20260401](../LA/LA_HUDSONLEDGER_20260401.md)**

---

## Definitions

- **HCB8 (Hudson Copper Beaver 8)**: The base indivisible accounting unit equal to 1/8 troy ounce of 95% pure copper bullion.  
- **Action Type**: Single character prefix in transaction records (`A` = Added, `S` = Subtracted).  
- **Trinity Check**: The unique combination of Action Type + Entry Address + Unadjusted Transaction Amount used to prevent double entries.  
- **Liquidity Scaling Factor**: Value (1, 2, 4, or 8) applied exclusively to copper units.  
- **Bitshift Taxation**: Right-shift operation (`>>N`) used to calculate sales, excise, and property taxes on added transactions only.

---

## Preamble
This schedule defines the transaction structure, binary representation rules, scaling mechanics, bitshift taxation, recording formats, HLTP receipt standards, and command-line interface for the Hudson Merchant Transaction Ledger. It operationalizes auditable, tamper-evident bullion accounting while preserving the constitutional 64:64:8 fixed bullion ratio architecture.

---

## Usage
This document serves as the authoritative technical reference for all software implementations (including the official offline tool `hudson_transaction_records_offline_tool.py`), validators, auditors, and manual operations. All transaction records and tools **must** conform exactly to the formats and rules defined herein.

---

## Hudson Transaction Records

### Directory Structure
- **Ledger Path**: `ledger/hudson_transaction_records_[Business Code]_[YYYY].txt`
- **Receipts Path (Added)**: `receipts/merchant_transactions_[Business Code]_[YYYY]/added/`
- **Receipts Path (Subtracted)**: `receipts/merchant_transactions_[Business Code]_[YYYY]/subtracted/`

### Transaction Record Format
**High-Level Structure**  
`V[SpecVersion]|[Timecode]|[Action qN]|[Riding]|[Business]|[Entry Address]|[Unadjusted Amount]|[Bitshift]|[Tax Amount]|[Adjusted Amount]|[Scaling]|[Hash]`

**Unadjusted / Adjusted Amount Format**  
`[Sign]u/aG.ggg.SSS.sss.CCC.ccc[.ZZZ]`

### Bitshift Taxation (Added Transactions Only)

| Bitshift | Approximate Rate | Recommended Use Case                     |
|----------|------------------|------------------------------------------|
| >>3      | 12.5%            | Maximum allowed inside the Republic      |
| >>4      | 6.25%            | Balanced market attraction & revenue     |
| >>5      | 3.125%           | High market adoption                     |
| >>6      | 1.563%           | Extreme market expansion                 |
| 0 or ~   | 0%               | No tax                                   |

**No taxation** is applied on subtracted (outgoing) transactions.

### Liquidity Scaling (Copper Only)
(See **SCH_DENOMINATIONLEDGER_20260611** for full scaling table.)

---

## Hudson Ledger Transaction Paper (.hltp)

**Filename Format**: `[Business Code]_[YYYY]_[Entry Address]_[ACTION].hltp`

**Structure**:
- **BOOKEEPING**
- **RECORD OF TRANSACTION** (Unadjusted, Taxation, Adjusted)
- **Minimum Viable Change (MVC)**
- **COMMENTS**
- **INTEGRITY**
- **GENERATOR**

---

## Command-Line Interface (`hudson_transaction_records_offline_tool.py`)

**Primary Actions**:
- `--add` / `-a`
- `--subtract` / `-s`

**Input Formats** (mutually exclusive):
- `--decimal` (e.g. `S,150.30`)
- `--binary` (hybrid G.ggg.SSS.sss.CCC.ccc)
- `--octal` (hybrid G.g.S.s.C.c)
- `--hcb8` (raw HCB8 units)

**Key Parameters**:
- `-b/--business-code` BBBB-BBBB
- `-R/--riding-code` 4 hex chars
- `-v/--value` transaction amount (per format)
- `-t/--taxation` 0/3/4/5/6
- `--scaling-factor` 1/2/4/8
- `--random` or `--entropy`

**See** `hudson_transaction_records_offline_tool.1` man page for full examples and detailed mathematics.

---

## Mathematics Summary
All amounts are converted to internal HCB8 integers.  
- **Add**: Round down (income).  
- **Subtract**: Round up (expense).  
- Taxation: Right-shift unadjusted amount, pad, and add back.  
Full examples are documented in the man page and **Hudson Transaction Calculations.txt**.

---

## Disclaimer
**All tags require lowercase names and all multi-word tags require the use of underscores (_), instead of spaces ( ).**

---

**Original Author**: 

**House Signature**:

**Senate Signature**:

**Executive Office Signature**: 

**FQLN**: SCH_DENOMINATIONLEDGER_20260611
