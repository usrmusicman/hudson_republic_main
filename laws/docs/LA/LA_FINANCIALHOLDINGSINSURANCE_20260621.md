# Financial Holdings Insurance Act

---

## Hard Dependencies
List any legislative instrument(s) (in alphabetical order) that this article must depend on. List the FQLN(s) below. Any FQLN(s) mentioned in other sections are considered to be references and not actual dependencies.  
Only **Constitutional Articles (CA)** and **Legislative Articles (LA)** can be listed here.

* **[CA_BANKANDRESERVE_20260401](../CA/CA_BANKANDRESERVE_20260401.md)**  
* **[CA_LEGALTENDER_20260401](../CA/CA_LEGALTENDER_20260401.md)**  
* **[CA_THEINDIVIDUAL_20260401](../CA/CA_THEINDIVIDUAL_20260401.md)**  
* **[LA_BANKINSURANCESTANDARDS_20260525](LA_BANKINSURANCESTANDARDS_20260525.md)**  
* **[LA_BULLIONSTANDARDS_20260401](../LA/LA_BULLIONSTANDARDS_20260401.md)**  
* **[LA_HUDSONLEDGER_20260401](../LA/LA_HUDSONLEDGER_20260401.md)**

---

## Definitions
- **Financial Holdings Insurance (FHI)**: Insurance coverage protecting bullion holdings recorded on the Hudson Ledger.  
- **Insured Denomination Record**: A ledger entry backed by physical bullion, a valid `.hldp` receipt, and the master ledger file.  
- **Institution Routing Number**: A unique identifier assigned to each FHI-insured institution for use in the global Hudson Exchange Authorized Database.

---

## Preamble
This Act establishes Financial Holdings Insurance (FHI) to protect the integrity of bullion holdings, ensure proper reconciliation, and maintain public confidence in the Hudson Republic’s sound money system.

---

## Section 1 — Mandatory FHI for Financial Institutions
All financial institutions operating in the Hudson Republic must maintain active Financial Holdings Insurance (FHI).

---

## Section 2 — Reconciliation and Validation Requirements
All FHI-insured ledger denominations must be supported by:
- A standard `.hldp` receipt
- The corresponding entry in `hudson_ledger_records_[Business Code]_[Year].txt`
- The physical bullion that was recorded

FHI-insured institutions have final authority on whether records may be synced and physical bullion accepted. The reconciling institution shall:
- Perform a full inspection and generation procedure
- Use entry code serials from the receipts via manual entry
- Employ a randomization method if a collision is detected in the database

Once all validations are complete, the denomination record shall be officially recorded and synchronized across the global Hudson Exchange Authorized Database.

If no receipts or personal ledgers are provided, the transaction shall be assayed and recorded as a denomination record (not a transaction) using the institution’s business code.

---

## Section 3 — Record Retention and Backup Requirements
All FHI-insured institutions must maintain:
- A primary copy of all records
- At least two backup copies, one of which must be in printed physical form

---

## Section 4 — Institution Routing Number
All FHI-insured institutions must maintain a unique Institution Routing Number. This number shall be appended at the very end of each recorded entry in the global Hudson Exchange Authorized Database.

---

## Section 5 — National Holdings Vault (NHV)
The National Holdings Vault must maintain full FHI coverage at all times. Any movement of reserves requires Senate approval by Clear Majority.

---

## Section 6 — Penalties for Breach
Failure to maintain FHI, comply with reconciliation protocols, or meet record retention requirements shall result in suspension of operations and Sequential Mandate penalties.

---

**Original Author**: 

**House Signature**: 

**Senate Signature**: 

**Executive Office Signature**: 

**FQLN**: LA_FINANCIALHOLDINGSINSURANCE_20260621
