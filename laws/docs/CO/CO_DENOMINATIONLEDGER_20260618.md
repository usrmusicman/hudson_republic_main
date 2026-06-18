# Denomination Ledger Code

---

## Legal Function
Legal code type is: **Technology**

Any notes about this code: **Primary technical standard and tooling specification for the Hudson Denomination Ledger (bullion accounting system).**

---

## Hard Dependencies
List any legislative instrument(s) (in alphabetical order) that this article must depend on. List the FQLN(s) below. Any FQLN(s) mentioned in other sections are considered to be references and not actual dependencies.  
Only **Constitutional Articles (CA)**, **Legislative Articles (LA)** and **Legislative Codes (CO)** can be listed here.

Dependencies
* **[CA_THEINDIVIDUAL_20260401](../CA/CA_THEINDIVIDUAL_20260401.md)**
* **[LA_HUDSONLEDGER_20260401](../LA/LA_HUDSONLEDGER_20260401.md)**

---

## Definitions
- **HCB8 (Hudson Copper Beaver 8)**: The base indivisible accounting unit equal to 1/8 troy ounce of 95% pure copper bullion.  
- **Business Code**: Base-21 identifier in format `XXXX-XXXX` using uppercase consonants only (B–D, F–H, J–N, P–T, V–Z).  
- **Riding Code**: Base-16 hexadecimal value `YYYY` (valid characters: 0–F).  
- **Entry Address (Entropy)**: Base-16 hexadecimal value in format `XXXX-XXXX-XXXX-XXXX` (valid characters: 0–F).  
- **Action Type**: Single character prefix (`A` = Added, `R` = Removed, `F` = Fraudulent, `B` = Blacklisted).  
- **Trinity Check**: Unique combination of Action Type + Mint Year + Entry Address + Transaction Amount.  
- **Hashing Algorithm**: Default is `sha3`.  
- **Hash Strength**: Default is 512-bit.

---

## Preamble
This Legislative Code establishes the mandatory technical standards, data structures, receipt formats, and official tooling for the Hudson Denomination Ledger.

---

## Purpose
The purpose of this Code is to define precise low-level and high-level formatting rules, binary representation, liquidity scaling, Trinity Check validation, and standardized receipt generation (.hldp) for all denomination-level bullion accounting.

---

## Provisions

### High-Level Format
`V[SpecVersion]|[Timecode]|[Action Type]|[Country]|[Riding Code]|[Business Code]|[Mint Year]|[Entry Address]|[Transaction Amount]|[Metal Form]|[Scaling Factor]|[Hash]`

### Low-Level Format (Internal Binary Register)
- Timecode timezone is set to UTC.  
- Gold and Silver positions are fixed.  
- Copper is affected by the Liquidity Scaling Factor.  
- Transaction Amount uses hybrid decimal/binary octet format: `[Sign]G.ggg.SSS.sss.CCC.ccc[.ZZZ]`  
   - Sixth octet (`.ZZZ`) is displayed only when scaling factor > 1.

### Additional Rules
- **Business Code**: Must be uppercase consonants only in `XXXX-XXXX` format.  
- **Riding Code**: Exactly 4 hexadecimal characters (0–F).  
- **Entry Address**: Exactly 16 hexadecimal characters in `XXXX-XXXX-XXXX-XXXX` format.  
- **Hashing**: Default algorithm is `sha3` with 512-bit strength.  
- **Comments**: Required for every transaction (1 for `-1` switch, 5 for `-5` switch).

---

## Procedures
- All operations **must** use the official tool `hudson_ledger_offline_tool.py` or a fully compliant equivalent.  
- Trinity Check validation is mandatory before committing any record.  
- Receipts (.hldp) must be generated with full BOOKKEEPING, RECORD OF DENOMINATION, COMMENTS, INTEGRITY, and GENERATOR sections.

---

## Compliance
Non-compliance (incorrect formatting, invalid Business/Riding/Entry codes, bypassing Trinity Check, etc.) constitutes a breach of monetary integrity and may result in loss of FHI/MTI coverage and applicable penalties.

---

## Conflicts
This Code is subordinate to the **[Hudson Ledger Act](../LA/LA_HUDSONLEDGER_20260401.md)**.

---

**Original Author**: 

**House Signature**: 

**Senate Signature**: 

**Executive Office Signature**: 

**FQLN**: CO_DENOMINATIONLEDGER_20260618
