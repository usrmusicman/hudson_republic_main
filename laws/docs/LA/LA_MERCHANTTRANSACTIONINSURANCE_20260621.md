# Merchant Transaction Insurance Act

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
- **Merchant Transaction Insurance (MTI)**: Insurance coverage for physical bullion transactions conducted by merchants.  
- **Insured Transaction Record**: A transaction supported by a `.hltp` receipt, the master transaction ledger, and the backing physical bullion.  
- **Institution Routing Number**: A unique identifier assigned to each FHI-insured institution for use in the global Hudson Exchange Authorized Database.

---

## Preamble
This Act establishes Merchant Transaction Insurance (MTI) to protect commercial bullion transactions, ensure accurate record-keeping, and maintain trust in day-to-day commerce within the Hudson Republic.

---

## Section 1 — Mandatory MTI Requirement
Any merchant or business conducting physical bullion transactions of one troy ounce of gold equivalent or greater must maintain active Merchant Transaction Insurance (MTI).

---

## Section 2 — Reconciliation and Validation Requirements
All MTI-insured transactions must be supported by:
- A standard `.hltp` receipt
- The corresponding entry in `hudson_transaction_records_[Business Code]_[Year].txt`
- The physical bullion that backed the transaction

FHI-insured institutions reconciling the transaction have final authority on whether records may be synced and physical bullion accepted. The reconciling institution shall:
- Perform a full inspection and generation procedure
- Use entry code serials from the receipts via manual entry
- Employ a randomization method if a collision is detected in the database

Once all validations are complete, the transaction record shall be officially recorded and synchronized across the global Hudson Exchange Authorized Database.

If no receipts or personal ledgers are provided, the transaction shall be assayed and recorded as a denomination record (not a transaction) using the institution’s business code.

---

## Section 3 — Record Retention and Backup Requirements
All FHI-insured institutions involved in MTI-covered transactions must maintain:
- A primary copy of all records
- At least two backup copies, one of which must be in printed physical form

---

## Section 4 — Institution Routing Number
All FHI-insured institutions must maintain a unique Institution Routing Number. This number shall be appended at the very end of each recorded entry in the global Hudson Exchange Authorized Database.

---

## Section 5 — Claims Process
Claims under MTI shall be processed only upon verified discrepancies between physical bullion, receipts, and ledger records. All claims must follow the official reconciliation and validation procedure.

---

## Section 6 — Penalties for Non-Compliance
Failure to maintain MTI or comply with transaction recording and reconciliation requirements shall result in civil fines and Sequential Mandate penalties.

---

**Original Author**: 

**House Signature**: 

**Senate Signature**: 

**Executive Office Signature**: 

**FQLN**: LA_MERCHANTTRANSACTIONINSURANCE_20260621
