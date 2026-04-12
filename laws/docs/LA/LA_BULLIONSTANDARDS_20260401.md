# Bullion Standards and Conversion Act

---

## Definitions
All capitalized terms used in this Act shall be interpreted in accordance with their definitions in the referenced instruments below.

- **Gold spot price**: The publicly verifiable international market price per troy ounce of 99.99% or higher purity gold.  
- **Ledger Unit**: The base indivisible accounting denomination, equal to 1/8 troy ounce of 95% pure copper bullion.

---

## Preamble
This Act establishes the fixed bullion ratios, conversion rules between fiat and the Hudson Ledger, rounding protocols, binary representation mechanics, and detailed specifications for Founders Edition coins and institutional bars.

---

## Section 1 — Fixed Bullion Ratios (64 : 64 : 8)
* 64 troy ounces of silver = 1 troy ounce of gold  
* 64 troy ounces of copper = 1 troy ounce of silver  
* 8 × 1/8 troy ounce copper pieces = 1 troy ounce of copper

---

## Section 2 — Smallest Unit
The base Ledger accounting unit is 1/8 troy ounce of 95% pure copper. The maximum precision of the Ledger is 32,768 × 1/8 troy ounce copper units (64 × 64 × 8).

---

## Section 3 — Conversion Formulas (Transitional)
The gold spot price is the publicly available market price for 99.99%+ pure gold.

| Asset Form       | Direction       | Formula                                                                 |
|------------------|-----------------|-------------------------------------------------------------------------|
| Bars (99.5%)     | Fiat to Ledger  | (Fiat amount ÷ (0.995 × gold spot)) × 32,768                           |
| Bars (99.5%)     | Ledger to Fiat  | (Ledger units ÷ 32,768) × (0.995 × gold spot)                          |
| Coins (95.0%)    | Fiat to Ledger  | (Fiat amount ÷ (0.95 × gold spot)) × 32,768                            |
| Coins (95.0%)    | Ledger to Fiat  | (Ledger units ÷ 32,768) × (0.95 × gold spot)                           |

---

## Section 4 — Rounding Rule
All values resulting from conversions shall be rounded **down** to the nearest whole number of 1/8 troy ounce copper units.  
**Exception**: When the transaction represents a debit or expense to the payer, any fractional remainder shall be rounded **up** at the final step. When the transaction represents a credit or income to the recipient, any fractional remainder shall be rounded **down** at the final step.

---

## Section 5 — Founders Edition Reference Coins
The Founders Edition establishes circulation standards for coins. Institutional bars (99.5% purity) are reserved exclusively for banking, trusts, savings, and reserves.

### Founders Edition Coins
**Obverse (Heads) – Common to All Editions**  
* “HUDSON REPUBLIC” in all capital letters along the top ridge.  
* Central image: Beaver gnawing on wood.  
* Purity percentage displayed along the left or right ridge.  
* Weight (“1/8 OZ” or “1 OZ”) displayed along the bottom ridge.  

**Obverse – 1 oz Coins**  
* Year (full YYYY format) displayed directly underneath the beaver.  

**Obverse – 1/8 oz Coins**  
* Year (full YYYY format) displayed along the left or right ridge of the beaver.  

**Reverse (Tails)**  
* 16-character hexadecimal serial number for unique internal tracking and circulation control.  
* The serial is split into two groups of eight characters: one group along the top ridge and the second group along the bottom ridge.  
* Central design: Beaver gnawing on an oak tree (shared motif across all metal types, differentiated by weight).

**Coin Composition and Dimensions**

| Coin Code | Metal  | Bullion Alloy (95%) | Hardener (5%) | Diameter | Thickness |
|-----------|--------|---------------------|---------------|----------|-----------|
| HGB1      | Gold   | Gold                | Copper        | 32 mm    | 2.17 mm   |
| HGB8      | Gold   | Gold                | Copper        | 16 mm    | 1.08 mm   |
| HSB1      | Silver | Silver              | Copper        | 32 mm    | 3.91 mm   |
| HSB8      | Silver | Silver              | Copper        | 16 mm    | 1.95 mm   |
| HCB1      | Copper | Copper              | Iron          | 32 mm    | 4.57 mm   |
| HCB8      | Copper | Copper              | Iron          | 16 mm    | 2.28 mm   |

Coinage Render

![Hudson Republic Banner](../../images/LA/LA_BULLIONSTANDARDS_20260401/BULLIONBEAVERS_FOUNDERS_EDITION_2026.png)

---

## Section 6 — Institutional Bars (99.5% Purity)
All institutional bars maintain a consistent square cross-section per metal, enabling perfect modular stacking in vaults (a 10 oz bar equals ten 1 oz bars in footprint).

| Metal  | Weight   | Pure Metal | Gross Mass | Length × Width     | Thickness |
|--------|----------|------------|------------|--------------------|-----------|
| Gold   | 1/8 oz   | 3.88 g     | 3.91 g     | 10.1 mm × 10.1 mm  | 2.0 mm    |
| Gold   | 1 oz     | 31.10 g    | 31.26 g    | 28.5 mm × 28.5 mm  | 2.0 mm    |
| Gold   | 10 oz    | 311.03 g   | 312.60 g   | 28.5 mm × 28.5 mm  | 20.0 mm   |
| Gold   | 100 oz   | 3,110.35 g | 3,126.00 g | 28.5 mm × 28.5 mm  | 200.0 mm  |
| Silver | 1/8 oz   | 3.88 g     | 3.91 g     | 13.7 mm × 13.7 mm  | 2.0 mm    |
| Silver | 1 oz     | 31.10 g    | 31.26 g    | 38.6 mm × 38.6 mm  | 2.0 mm    |
| Silver | 10 oz    | 311.03 g   | 312.60 g   | 38.6 mm × 38.6 mm  | 20.0 mm   |
| Silver | 100 oz   | 3,110.35 g | 3,126.00 g | 38.6 mm × 38.6 mm  | 200.0 mm  |
| Copper | 1/8 oz   | 3.88 g     | 3.91 g     | 14.8 mm × 14.8 mm  | 2.0 mm    |
| Copper | 1 oz     | 31.10 g    | 31.26 g    | 41.8 mm × 41.8 mm  | 2.0 mm    |
| Copper | 10 oz    | 311.03 g   | 312.60 g   | 41.8 mm × 41.8 mm  | 20.0 mm   |
| Copper | 100 oz   | 3,110.35 g | 3,126.00 g | 41.8 mm × 41.8 mm  | 200.0 mm  |

Institutional Bars Render

![Hudson Republic Banner](../../images/LA/LA_BULLIONSTANDARDS_20260401/BULLIONBEAVERS_FOUNDERS_EDITION_BARS_2026.jpg)

---

## Section 7 — Internal Tracking and Identification
All Hudson-minted bullion (coins, rounds, and bars) shall carry a unique 16-character hexadecimal serial number for banking, circulation, and audit purposes.  
Serial Format: H[G,S,C]B[1 or 8]-YYYY-FFFFFFFF-FFFFFFFF  
* H[G,S,C]B[1 or 8] prefix identifies metal (G = Gold, S = Silver, C = Copper) and weight (1 = 1 oz, 8 = 1/8 oz).  
* YYYY = minting year.  
* Two groups of eight hexadecimal characters (top and bottom ridges on coins; top and bottom of bars).  

For coins and rounds: Minting date on obverse; two 8-character hexadecimal groups on reverse with central beaver-on-oak-tree design between them.  
For bars: Minting date and two 8-character hexadecimal groups on the front face (one at top, one at bottom) with central beaver-on-oak-tree design between them.

---

## Section 8 — Binary Representation and Bitshift Mechanics
The fixed ratios of 64 : 64 : 8 are deliberately powers of two (2⁶), enabling the entire Ledger to be expressed in pure binary with a maximum precision of 2¹⁵ (32,768) Ledger Units.  

This architecture permits:
- Simple bit-shifting for the automatic calculation of tariffs and taxes (e.g., >>4 = 6.25 %).  
- Octal masking for human-readable “exact change” at point of sale.  
- Predictable behaviour when any single metal’s fiat price fluctuates, as the other metals absorb variance without destabilizing the Ledger.

All conversion examples and practical applications are illustrative only and must conform to the formulas and rounding rules set out in Sections 3 and 4.

## Reference Dependencies
Dependencies (in alphabetical order)  
* **[CA_BANKANDRESERVE_20260401](../CA/CA_BANKANDRESERVE_20260401.md)**  
* **[CA_LEGALTENDER_20260401](../CA/CA_LEGALTENDER_20260401.md)**  

---

**Original Author**: 

**House Signature**: 

**Senate Signature**: 

**Executive Office Signature**: 

**FQLN**: LA_BULLIONSTANDARDS_20260401
