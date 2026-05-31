# Postal System Act

---

## Hard Dependencies
List any legislative instrument(s) (in alphabetical order) that this article must depend on. List the FQLN(s) below. Any FLQN(s) mentioned in other sections are considered to be references and not actual dependencies.  
Only **Constitutional Articles (CA)** and **Legislative Articles (LA)** can be listed here.

Dependencies
* **[CA_ELECTIONS_20260401](../CA/CA_ELECTIONS_20260401.md)**  
* **[CA_GENERALADMIN_20260401](../CA/CA_GENERALADMIN_20260401.md)**  
* **[CA_TERRITORIALPROVISION_20260401](../CA/CA_TERRITORIALPROVISION_20260401.md)**  
* **[CA_THEINDIVIDUAL_20260401](./CA_THEINDIVIDUAL_20260401.md)**

---

## Definitions

- **Beaver Routing Protocol (BRP)**: The official addressing and routing protocol used by the Hudson Republic Postal Service.  
- **Riding Code (RCO)**: A 4-character hexadecimal identifier split into a 2-character Riding Block prefix and a 2-character specific Riding suffix.  
- **Individual Routable Address (IRA)**: An 8-character hexadecimal address split into a 3-character Subzone identifier (prefix) and a 5-character individual delivery endpoint (suffix).  
- **Transaction Address Field Identifier (TAFI)**: An 8-character hexadecimal ephemeral checksum used for secure transaction tracking and delivery confirmation.  
- **Reserved Addresses**: Special addresses used exclusively for elections, emergency coordination, and official government communications.

---

## Preamble

The Hudson Republic Postal System is a critical national infrastructure service designed to ensure secure, efficient, and transparent delivery of mail, ballots, government documents, and commercial parcels across all Ridings. This Act establishes the Beaver Routing Protocol (BRP), a structured, hexadecimal-based addressing system that supports the Republic’s principles of transparency, accountability, and individual sovereignty while maintaining operational resilience for elections and emergencies.

---

## Section 1 — Beaver Routing Protocol (BPR)

**1.1** All postal addresses in the Hudson Republic shall use the Beaver Routing Protocol (BRP) format consisting of four distinct fields separated by underscores (_). All alphabetic characters shall be uppercase.

**1.2 Address Format**  
`[Designation]_[RCO]_[IRA]_[TAFI]`

**1.3 Designation Field** (up to 4 alpha characters)  
- BAL = Varified Ballot Address Token (send and recieve)  
- CIV = Civilian (commercial or residential)  
- CAMP = Campground or trailer park  
- FIN = Financial institution  
- GOV = Government administration building  
- IND = Industrial use  
- MIL = Military base  
- MISC = Miscellaneous (does not fit other categories)  
- NAT = Nature reserve or conservation area  
- PORT = Ports, borders, and high-security transport points  
- REM = Remote or temporary installation  

**1.4 Riding Code (RCO)**: 4 hexadecimal characters.  
- First 2 characters (prefix) = Riding Block identifier  
- Last 2 characters (suffix) = Specific Riding within the block  

**1.5 Individual Routable Address (IRA)**: 8 hexadecimal characters.  
- First 3 characters (prefix) = Subzone identifier  
- Last 5 characters (suffix) = Individual delivery endpoint  

**1.6 Transaction Address Field Identifier (TAFI)**: 8 dynamically randomized hexadecimal characters used for secure delivery verification. The transaction is recorded for fulfillment and the TAFI identifier pool is completely reset per day (24 hours).

---

## Section 2 — Mathematical Constraints & Address Space

**2.1** The BPR protocol is designed with deliberate mathematical constraints to ensure scalability, security, and efficient routing:

**RCO Field Constraints**  
- **Riding Loss per Block (RLB)**: 2 reserved ridings per block  
- **Total Available Ridings TAR**: (16⁴) - [((16²) × RLB) + (((16²) - 2) × RLB)]

**IRA Field Constraints**  
- **Per Subzone Loss (SZL)**: 2 reserved addresses per Subzone  
- **Subzone Addressable Range (SAR)**: (16⁸) − [((16⁵) × SZL) + (((16³) − 2) × SZL)]  

**TAFI Field Constraints**  
- **TAFI Loss**: 2 reserved addresses (all zeros and all F's)  

**Total Addressable Space (TAS)**: SAR × TAR  

---

## Section 3 — Visual Representation of BPR

| Field (Separated by an underscore) | Component                                   | Format (Characters) | Function                                      |
|------------------------------------|---------------------------------------------|---------------------|-----------------------------------------------|
| **1**                              | Designation                                 | Up to 4 Alpha       | Priority & Infrastructure Filter              |
| **2 (Prefix)**                     | RCO (Block)                                 | 2 Hex               | Riding Block Routing                          |
| **2 (Suffix)**                     | RCO (Riding)                                | 2 Hex               | Specific Riding within Block                  |
| **3 (Prefix)**                     | IRA (Prefix)                                | 3 Hex               | Subzone Routing                               |
| **3 (Suffix)**                     | IRA (Suffix)                                | 5 Hex               | Individual Delivery Endpoint                  |
| **4**                              | Transaction Address Field Identifier (TAFI) | 8 Hex               | Ephemeral Cryptographic Token                 |

---

## Section 4 — Reserved Addresses

**4.1** Reserved addresses are determined by all-zero or all-F patterns in the relevant suffix fields:
- **RCO / IRA Suffix all zeros** = Return or relay address.  
- **RCO / IRA Suffix all F's** = Broadcast address.  
- **TAFI all zeros or all F's** = Reserved return/relay or broadcast.

**4.2** Key Reserved Addresses (examples):
- **0000** (RCO level): National Elections and Emergency Coordination Office (return).  
- **FFFF** (RCO level): National Elections and Emergency Coordination Office (broadcast).  
- **000** (Subzone prefix) + `00000` (suffix): Riding/Subzone elections and emergency coordination offices (return/relay).  
- **FFF** (Subzone prefix) + `FFFFF` (suffix): Riding/Subzone broadcast addresses.

**4.3** These reserved addresses remain closed except during active election periods or declared emergencies.

## Section 5 - Routing Procedure

**Returns**: Subzone --> Riding --> Block --> National
**Broadcasts**: National --> Block --> Riding --> Subzone

---

## Section EX1 — Illustrative Examples (Non-binding)

**EX1.1 Civilian Delivery**  
A parcel addressed to a civilian in Riding BB02, Subzone 001, Individual 02A2B:  
`CIV_BB02_00102A2B_A2BC0345`

**EX1.2 National Election Return**  
Ballot return from all Block Elections Offices to the National Elections Office:  
`GOV_0000_00000000_00000000`

**EX1.3 National Broadcast**  
Government emergency pamphlet or VIP pass distribution throughout the entire republic:  
`GOV_FFFF_FFFFFFFF_FFFFFFFF`

**EX1.4 Riding Block Election Return**  
Ballot return from all Ridings Elections Offices to a Block Elections Office:  
`GOV_BB00_00000000_00000000`

**EX1.5 Riding Block Broadcast**  
Government emergency pamphlet or VIP pass distribution throughout the entire senate represented riding block:  
`GOV_BBFF_FFFFFFFF_FFFFFFFF`

**EX1.6 Riding Election Return**  
Ballot return from all Subzone Elections Offices to a Riding Elections Office:  
`GOV_BB02_00000000_00000000`

**EX1.7 Riding Broadcast**  
Government emergency pamphlet or VIP pass distribution throughout the Riding BB02:  
`GOV_BB02_FFFFFFFF_FFFFFFFF`

**EX1.8 Subzone Election Return**  
Ballot return from all polling stations to a Subzone Elections Office (Subzone 20A):  
`GOV_BB02_20A00000_00000000`

**EX1.9 Subzone Broadcast**  
Government emergency pamphlet or VIP pass distribution throughout Subzone 20A:  
`GOV_BB02_20AFFFFF_FFFFFFFF`

---

**Original Author**:

**House Signature**:

**Senate Signature**:

**Executive Office Signature**:

**FQLN**: LA_POSTALSYSTEM_20260528
