# Merchant Transaction Ledger Code

---

## Legal Function
Legal code type is: **Technology**

Any notes about this code: **Primary technical standard for recording merchant-level bullion transactions, taxation, and HLTP receipts.**

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
- **Action Type**: Single character prefix (`A` = Added, `S` = Subtracted).  
- **Trinity Check**: Unique combination of Action Type + Entry Address + Unadjusted Transaction Amount.  
- **Hashing Algorithm**: Default is `sha3`.  
- **Hash Strength**: Default is 512-bit.

---

## Preamble
This Legislative Code establishes the mandatory standards for recording all merchant bullion transactions on the Hudson Transaction Ledger.

---

## Purpose
The purpose of this Code is to define transaction record format, input methods, bitshift taxation rules, scaling mechanics, and tooling requirements for accurate, auditable merchant commerce records.

---

## Provisions

### High-Level Format
`V[SpecVersion]|[Timecode]|[Action qN]|[Riding Code]|[Business Code]|[Entry Address]|[Unadjusted Amount]|[Bitshift]|[Tax Amount]|[Adjusted Amount]|[Scaling]|[Hash]`

### Low-Level Format (Internal Binary Register)
- Timecode timezone is set to UTC.  
- Copper is affected by Liquidity Scaling Factor.  
- Gold and Silver positions remain fixed.  
- Transaction Amount uses hybrid format: `[Sign]u/aG.ggg.SSS.sss.CCC.ccc[.ZZZ]`  
	- Sixth octet (`.ZZZ`) is displayed only when scaling factor > 1.

### Additional Rules
- **Business Code**: Must be uppercase consonants only in `XXXX-XXXX` format.  
- **Riding Code**: Exactly 4 hexadecimal characters (0–F).  
- **Entry Address**: Exactly 24 hexadecimal characters in `XXXX-XXXX-XXXX-XXXX` format.  
- **Hashing**: Default algorithm is `sha3` with 512-bit strength.  
- **Comments**: Required for every transaction.

---

## Procedures
- All merchant transactions must be recorded using the official tool `hudson_transaction_records_offline_tool.py` or a compliant equivalent.  
- Trinity Check validation is mandatory.  
- Receipts (.hltp) must be generated with full BOOKKEEPING, RECORD OF TRANSACTION, COMMENTS, INTEGRITY, and GENERATOR sections.

---

## Compliance
Non-compliance (incorrect formatting, invalid codes, bypassing checks, etc.) constitutes a breach of the monetary framework and may result in loss of MTI coverage and penalties.

---

## Conflicts
This Code is subordinate to the **[Hudson Ledger Act](../LA/LA_HUDSONLEDGER_20260401.md)**.

---

**Original Author**: 

**House Signature**: 

**Senate Signature**: 

**Executive Office Signature**: 

**FQLN**: CO_TRANSACTIONLEDGER_20260618
