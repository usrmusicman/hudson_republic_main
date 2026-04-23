# Borders and Duties Act

---

## Hard Dependencies
List any legislative instrument(s) (in alphabetical order) that this article must depend on. List the FQLN(s) below. Any FLQN(s) mentioned in other sections are considered to be references and not actual dependencies.  
Only **Constitutional Articles (CA)**, **Legislative Articles (LA)** and **Schedules (SCH)** can be listed here.

Dependencies
* **[CA_LEGALTENDER_20260401](../CA/CA_LEGALTENDER_20260401.md)**  
* **[CA_NAMINGCONVENTION_20260401](../CA/CA_NAMINGCONVENTION_20260401.md)**  
* **[CA_THEINDIVIDUAL_20260401](../CA/CA_THEINDIVIDUAL_20260401.md)**  

---

## Definitions
All capitalized terms used in this Act shall be interpreted in accordance with their definitions in the referenced instruments below.

- **Hudson Port Authority (HPA)**: Federal agency responsible for port security, cargo inspection, and tariff collection.  
- **Bitshift Tariff**: Tariff calculated by right-shifting the transaction value in binary representation on the Hudson Ledger.

---

## Preamble
This Act governs all entry, inspection, revenue collection, cargo handling, and security at the ports and borders of the Hudson Republic. It ensures that ports remain clean, efficient, and free of abandoned, junk, or prohibited cargo while generating revenue solely through usage-based and enforcement-based mechanisms. All federal charges at borders and ports are assessed at flat rates where applicable, with tariffs calculated via bitshift. This Act operates in full harmony with **[The Individual (Sovereign) Act](../CA/CA_THEINDIVIDUAL_20260401.md)** and the **[Legal Tender Act](../CA/CA_LEGALTENDER_20260401.md)**. All financial transactions and settlements under this Act shall be made exclusively in physical bullion in accordance with the **[Legal Tender Act](../CA/CA_LEGALTENDER_20260401.md)**.

---

## Section 1 — Revenue Sources at Ports and Borders
**1.1** Federal revenue from borders and ports shall be derived exclusively from:  
* Entry tolls and terminal fees;  
* Inspection and handling fees;  
* Storage and demurrage charges;  
* Return levies (for rejected, unfulfilled, uninsured, or refused shipments);  
* Fines for border or port violations;  
* Tariffs on international commerce.  

**1.2** All non-tariff charges shall be assessed at fixed flat rates (per shipment, container, entry attempt, or unit) and published in advance by the Hudson Port Authority (HPA).  
**1.3** All items subject to tariffs shall be published in advance by the Hudson Port Authority (HPA).

---

## Section 2 — Calculation of Tariffs
**2.1** Tariffs are calculated by bit-shifting the transaction value to the right in the official Hudson Ledger (binary representation).

| Rate   | Bitshift Operation | Logic                  |
|--------|--------------------|------------------------|
| 25%    | >> 2               | Quarter of value       |
| 12.5%  | >> 3               | Eighth of value        |
| 6.25%  | >> 4               | Sixteenth of value     |

* **Parity Limit**: No tariff may exceed parity (1:1). This is a bitshift of 0.  
* **Dust Limit**: Any amount that falls below one-eighth (1/8) troy ounce of copper after the bit-shift is automatically dropped (too small to collect).  
* **Result**: The resulting amount after the bit-shift is the tariff due.

---

## Section 3 — Philosophy of Tariffs
**3.1** Tariffs in the Hudson Republic serve exclusively as a defensive shield to protect domestic industry, national security, and economic sovereignty. They are not a tool of aggression or retaliation against trading partners. Reciprocal or punitive tariffs are prohibited. The Republic seeks fair and open trade while safeguarding its own vital interests.

**3.2** Digital products and digital distribution (software, streaming content, electronic files, online services, and similar intangible goods) are exempt from all tariffs under this Act.

**3.3** All tariffs, treaty partner statuses, and bitshift rates shall be reviewed quarterly at the conclusion of each business quarter.

**3.4** Treaty partner statuses may be established, modified, or revoked at any time as necessary to preserve the trade interests and economic sovereignty of the Hudson Republic.

**3.5** Any modifications to tariffs during a declared emergency shall be authorized exclusively through Emergency Legislation (EL) and shall not be incorporated into the **[Tariff and Treaties Schedule](../SCH/SCH_TARIFFANDTREATIES_20260401.md)**.

**3.6** The National Representative shall have sole authority to adjust tariffs, treaty partner statuses, and bitshift rates for a period not exceeding one business quarter (three months). Upon expiration of this period, the Senate shall review the adjustments. If the Senate determines that the adjustments are not in the best interests of the Republic, the default Senate-approved tariffs, treaty partner statuses, and bitshift rates shall be immediately restored. If the Senate determines that the adjustments are in the best interests of the Republic, any permanent changes must follow the full legislative amendment process for the associated schedule **[Tariff and Treaties Schedule](../SCH/SCH_TARIFFANDTREATIES_20260401.md)**, in accordance with the Legislative Article instrument type outlined in the **[Legislative Document Classification and Naming Convention Act](../CA/CA_NAMINGCONVENTION_20260401.md)**.

---

## Section 4 — Inbound and Outbound Traffic Policy
**4.1 Inbound Traffic**: All inbound cargo, persons, and conveyances may be blocked, searched, inspected, transferred, or confiscated under the conditions and priorities set out in this Act and the associated Schedules.

**4.2 Outbound Traffic**: All outbound traffic shall be fulfilled without delay unless it is determined to be criminal in nature following a joint investigation by the Hudson Intelligence Service (HIS) and the Hudson Port Authority (HPA). In such cases, the shipment may be detained, seized, or refused in accordance with applicable criminal law.

---

## Section 5 — Port Authority Priority Security
**5.1** Cargo shall be classified into priority levels based on risk, compliance, and content.

### 5.2 Priority 0 — Normal Trade Routine
Lawful commercial shipments with no security concerns. Proceed via standard processing with minimal inspection, provided documentation and Legal Tender Act bullion payments are met.

### 5.3 Priority 1 — Prohibited but Not Illegal
Goods that harm the public or are invasive to Republic ecosystems.  
* **Handling**: Returned to the merchant or importer.  
* **Consequence**: Importer pays a flat return penalty in physical bullion.

### 5.4 Priority 2 to 4 — Illegal but Not Criminal
Items that warrant fines rather than imprisonment.  
* **Handling**: Immediate forfeiture and destruction.  
* **Consequence**: Fines in bullion. Domestic businesses may lose their commerce license for ≥ 5 years. Outside actors may be barred for 5 years.

### 5.5 Priority 5 to 7 — Illegal (Criminal)
Serious contraband leading to criminal and civil charges.  
* **Handling**: Immediate forfeiture and destruction.  
* **Consequence**: Criminal charges and bullion fines. Outside actors barred for 25 years. Domestic merchants face permanent or long-term license revocation.

---

## Section 6 — Payment and Settlement
**6.1** All charges must be paid exclusively in physical bullion meeting Legal Tender Act standards.  
**6.2** Payment is due at the time of transaction or assessment, based on the metal value at the exact time of transaction in the payer’s jurisdiction.  
**6.3** Hudson-minted beaver bullion is accepted but not required.

---

## Section 7 — Rejection, Abandonment, and Return
**7.1** If a shipment is rejected, unfulfilled, or uninsured:  
* The responsible party pays a flat return levy for storage and handling.  
* The party has **ninety (90) days** from the Notice of Assessment to pay and arrange return.  
**7.2** Failure to act within 90 days results in automatic forfeiture of the property to the Republic.

---

## Section 8 — Forfeiture and Disposal
**8.1** Forfeited goods may be recycled, destroyed, auctioned, or retained for Republic use.  
**8.2** Any surplus proceeds after full cost recovery shall accrue to the **Federal Stability Fund**.

---

## Section 9 — Anti-Litter and Security Principle
**9.1** The Republic prohibits the accumulation of abandoned or junk cargo at any port.  
**9.2** Efficiency is maintained through flat-rate levies, strict 90-day forfeiture, bitshift tariffs, and mandatory bullion settlement.  
**9.3** This Act ensures no federal income tax, property tax, or domestic sales tax shall ever be levied at the federal level.

---

**Original Author**:

**House Signature**:

**Senate Signature**:

**Executive Office Signature**:

**FQLN**: LA_BORDERSDUTIES_20260401
