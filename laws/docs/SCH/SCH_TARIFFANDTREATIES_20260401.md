# Tariff and Treaties Schedule

---

## Definitions
All capitalized terms used in this Schedule shall be interpreted in accordance with their definitions in the referenced instruments below.

- **Lifecycle State**: The stage of processing of the imported good.  
  - **raw**: Unprocessed raw material.  
  - **partial**: Partially processed and ready for further manufacturing.  
  - **complete**: Fully finished product ready for packaging and sale.  
  - **all**: Applies to every stage of the product lifecycle.

- **Treaties**: Trade agreements recognized by the Hudson Republic.  
  - **standard**: Standard trade access granted to Satellite States and territories in the adoption process.  
  - **nap**: North America Pact (trade agreement covering North American partners).  
  - **gtpa**: Global Trade Partner Agreement (trade agreement covering designated global partners).  
  - **all**: Applies to every approved treaty type.  
  - **none**: No treaty benefits apply.

- **Treaty State** or **Membership Status**: The current operational status of a treaty membership.  
  - **active**: The treaty is fully in effect.  
  - **review**: The treaty is under active review; either party has thirty (30) days to nullify it. Failure to renegotiate results in suspension (existing treaties) or denial (new treaties).  
  - **suspended**: The treaty is temporarily void; either party has ninety (90) days to rectify the matter through negotiation or formal apology where applicable. Failure to resolve negotiations leads to denial. The National Representative may impose immediate suspension if a partner is deemed a threat or is taking unfair advantage.  
  - **denied**: The treaty is fully nullified; affected parties must wait at least ninety (90) days after the next general election to reapply.

- **Exemptions**: Tariff relief categories tied to specific treaties.  
  - **standard**: Full tariff exemption for Satellite States and adoption candidates.  
  - **basic**: Exemption for essential staples (food, water, agricultural products).  
  - **technology**: Exemption for high-technology items (computers, electronic components) available only to approved treaty partners.  
  - **none**: No exemptions apply.

- **Value in Fiat**: The declared value of the imported good in the exporter’s fiat currency prior to conversion.  
- **Value in Bullion Beavers**: The equivalent value after conversion to Hudson Bullion Beavers using the formulas in **[LA_BULLIONSTANDARDS_20260401](../LA/LA_BULLIONSTANDARDS_20260401.md)**.  
- **Bitshift Adjustment**: The binary right-shift operation applied to calculate the tariff rate.  
- **HCB8**: The smallest unit of Hudson Copper Bullion (1/8 troy ounce of 95% pure copper).

---

## Preamble
This Schedule provides the definitive, machine-readable tariff rates and treaty framework for all imports and exports under the authority of the **[Borders and Duties Act](../LA/LA_BORDERSDUTIES_20260401.md)**. It establishes standardized product classifications, lifecycle stages, treaty categories, exemptions, and conversion protocols to ensure transparency, predictability, and consistency in the application of tariffs. All valuations and payments shall be conducted exclusively in physical bullion in accordance with the **[Legal Tender Act](../CA/CA_LEGALTENDER_20260401.md)**. This Schedule is purely referential and derives its authority from its parent instrument.

---

## Usage

### Tariff Schedule

**Product or Material**: Name of the line item subject to tariff.  
**Lifecycle State**: Stage of processing at time of import.  
**Treaties**: Applicable trade agreements.  
**Treaty State**: Current operational status of the treaty membership (affects the entire membership and all covered items).  
**Exemptions**: Any tariff relief granted under the selected treaty.  
**Value in Fiat**: Declared value in exporter’s currency (amount, currency).  
**Value in Bullion Beavers**: Converted value using **[LA_BULLIONSTANDARDS_20260401](../LA/LA_BULLIONSTANDARDS_20260401.md)** formulas.  
**Bitshift Adjustment**: Binary right-shift used to calculate the tariff.  
**Percentage (%)**: Equivalent percentage rate.  
**Weight (Per Unit)**: Weight of the item for assessment purposes.

| Product or Material | Lifecycle State | Treaties   | Treaty State | Exemptions | Value in Fiat (Currency Type) | Value in Bullion Beavers (HCB8) | Bitshift Adjustment | Percentage | Weight (Per Unit) |
|---------------------|-----------------|------------|--------------|------------|-------------------------------|---------------------------------|---------------------|------------|-------------------|
| Copper              | all             | standard   | active       | standard   | amount                        | amount                          | >>2                 | 25%        | 1 oz              |
| Maple Syrup         | complete        | standard   | active       | standard   | amount                        | amount                          | >>3                 | 12.5%      | 100 g             |
| Lumber              | raw             | none       | active       | none       | amount                        | amount                          | >>3                 | 12.5%      | 1 kg              |

**Note**: Treaty State applies at the line-item level. Membership status affects the entire membership and any items covered under that treaty.

### Treaties Schedule

**Treaty Name**: Official name of the treaty.  
**Membership Status**: Current standing of the treaty relationship.  
**Country(s) or Region(s)**: Participating nations or regions (lowercase with underscores).  
**Adoption Date**: Date the National Representative signed the treaty (YYYYMMDD).  
**Renewal Date**: Next scheduled renewal or review date (YYYYMMDD).

| Treaty Name | Membership Status | Country(s) or Region(s)                             | Adoption Date (YYYYMMDD) | Renewal Date (YYYYMMDD) |
|-------------|-------------------|-----------------------------------------------------|--------------------------|-------------------------|
| standard    | active            | hudson_ridings,satellite_states,adoption_candidates | YYYYMMDD                 | YYYYMMDD                |
| nap         | review            | usa,mexico,greenland                                | tbd                      | tbd                     |
| gtpa        | review            | uk,eu,uae,japan,korea,india                         | tbd                      | tbd                     |

**Note**: If only specific countries or regions within a treaty experience a status change, a new row shall be added for those affected parties only. All tags must use lowercase letters and underscores (_) in place of spaces.

---

## Disclaimer
**All tags require lowercase names and all multi-word tags require the use of underscores (_), instead of spaces ( ).**

---

**Original Author**: 

**House Signature**: 

**Senate Signature**: 

**Executive Office Signature**: 

**FQLN**: SCH_TARIFFANDTREATIES_20260401
