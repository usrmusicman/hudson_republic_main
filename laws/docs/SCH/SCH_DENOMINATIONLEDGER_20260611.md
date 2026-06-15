# Hudson Denomination Ledger Schedule

---

## Hard Dependencies
List any legislative instrument(s) (in alphabetical order) that this article must depend on. List the FQLN(s) below. Any FQLN(s) mentioned in other sections are considered to be references and not actual dependencies.  
Only **Constitutional Articles (CA)**, **Legislative Articles (LA)** and **Legislative Codes (CO)** can be listed here.

* **[LA_HUDSONLEDGER_20260401](../LA/LA_HUDSONLEDGER_20260401.md)**

---

## Definitions

- **HCB8 (Hudson Copper Beaver 8)**: The base indivisible accounting unit equal to 1/8 troy ounce of 95% pure copper bullion.  
- **Action Type**: Single character prefix in ledger records (`A` = Added, `R` = Removed, `F` = Fraudulent, `B` = Blacklisted).  
- **Trinity Check**: The unique combination of Action Type + Mint Year + Entry Address + Transaction Amount used to prevent double entries.  
- **Liquidity Scaling Factor**: Value (1, 2, 4, or 8) that applies a right bitshift exclusively to copper units.  
- **Unit Type**: Physical form factor of the bullion (Bar, Coin, or Round).

---

## Preamble
This schedule defines the denomination structure, binary representation rules, scaling mechanics, transaction recording formats, HLDP receipt standards, and command-line interface for the Hudson (Beaver) Denomination Ledger. It operationalizes the requirements for sound, auditable, and tamper-evident bullion accounting while preserving the constitutional 64:64:8 fixed bullion ratio architecture.

---

## Usage
This document serves as the authoritative technical reference for all software implementations (including the official offline tool `hudson_ledger_offline_tool.py`), validators, auditors, and manual ledger operations. All Hudson Ledger records and tools **must** conform exactly to the formats and rules defined herein.

---

## Hudson (Beaver) Denomination Ledger

### Directory Structure
- **Ledger Path**: `ledger/hudson_ledger_records_[Business Code]_[YYYY].txt`
- **Receipts Path (Added)**: `receipts/denomination_ledger_[Business Code]_[YYYY]/added/`
- **Receipts Path (Removed)**: `receipts/denomination_ledger_[Business Code]_[YYYY]/removed/`
- **Receipts Path (Fraud)**: `receipts/denomination_ledger_[Business Code]_[YYYY]/fraud/`
- **Receipts Path (Blacklist)**: `receipts/denomination_ledger_[Business Code]_[YYYY]/blacklist/`

**Note**: No hyphens (`-`) are permitted in any ledger or receipt filenames.

### Ledger Record Format
**Filename**: `hudson_ledger_records_[Business Code]_[YYYY].txt`

**High-Level Structure**  
`V[SpecVersion]|[Timecode]|[Action Type qN]|[Country]|[Riding]|[Business]|[Mint Year]|[Entry Address]|[Transaction Amount]|[Metal Form]|[Scaling Factor]|[Hash]`

**Transaction Amount Format** (Hybrid Decimal/Binary)  
`[Sign]G.ggg.SSS.sss.CCC.ccc[.ZZZ]`

- Gold and Silver octet positions remain fixed.  
- Copper is affected by the Liquidity Scaling Factor.  
- The sixth octet (`.ZZZ`) is displayed only when scaling factor > 1.

### Liquidity Scaling (Copper Only)

| Scaling Factor | HCB8 per 1 oz Gold | Binary Threshold | Example (1 oz Copper)          | Description                  |
|----------------|--------------------|------------------|--------------------------------|------------------------------|
| 1x (Normal)    | 32,768             | 2¹⁵              | 0.000.000.000.001.000.000      | Standard operation           |
| 2x             | 65,536             | 2¹⁶              | 0.000.000.000.000.100.000      | Moderate liquidity boost     |
| 4x             | 131,072            | 2¹⁷              | 0.000.000.000.000.010.000      | Significant liquidity boost  |
| 8x             | 262,144            | 2¹⁸              | 0.000.000.000.000.001.000      | Maximum emergency liquidity  |

**Key Rules**:
- Gold and Silver positions are immutable.
- Only Copper is shifted.
- Scaling requires formal declaration and step-down procedure per **LA_HUDSONLEDGER**.

### Compound Recording (-5 Switch)
When recording 1/2 oz units with the `-5` switch, five separate ledger lines share the same Entry Address but carry distinct hashes. The first line records the full 1/2 oz amount; the remaining four record zeroed amounts.

---

## Hudson Ledger Denomination Paper (.hldp)

**Filename Format**: `[Business Code]_[Mint Year]_[Entry Address]_[ACTION].hldp`

**Structure**:
- **BOOKEEPING**
- **RECORD OF DENOMINATION** (Metal, Weight, Purity, Amount, Scaling)
- **COMMENTS** (1 for -1 switch, 5 for -5 switch)
- **INTEGRITY** (Hash Value(s))
- **GENERATOR** (Full command line)

---

## Command-Line Interface (`hudson_ledger_offline_tool.py`)

**Primary Actions**:
- `--add` / `-a`
- `--remove` / `-r`
- `--fraud` / `-f`
- `--blacklist`

**Switches**:
- `-1` (Single entry)
- `-5` (Compound 5× 1/10 oz recording)

**Key Parameters**:
- `-b/--business-code` BBBB-BBBB (no vowels)
- `-R/--riding-code` 4 hex chars
- `-c/--country` ISO 3166 alpha-3
- `-m/--metal` G/S/C
- `-t/--type` b/B/c/C/r/R
- `-v/--value` 1,2,4,5,8,10,100
- `--scaling-factor` 1/2/4/8
- `--random` or `--entropy` (16 hex chars)

**Double-Entry Prevention**: Trinity Check (Action + Mint Year + Entry Address + Amount)

**See** `hudson_ledger_offline_tool.1` man page for full examples and mathematics.

---

## Disclaimer
**All tags require lowercase names and all multi-word tags require the use of underscores (_), instead of spaces ( ).**

---

**Original Author**: 

**House Signature**:

**Senate Signature**:

**Executive Office Signature**: 

**FQLN**: SCH_DENOMINATIONLEDGER_20260611
