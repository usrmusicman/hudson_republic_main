# Hudson Republic - Special Accessibility Ballot Template

---

## Hard Dependencies
List any legislative instrument(s) (in alphabetical order) that this article must depend on. List the FQLN(s) below. Any FLQN(s) mentioned in other sections are considered to be references and not actual dependencies.  
Only **Constitutional Articles (CA)**, **Legislative Articles (LA)** and **Legislative Codes (CO)** can be listed here.

Dependencies
* **[CA_ELECTIONS_20260401](../CA/CA_ELECTIONS_20260401.md)**

---

## Preamble
This specification sheet contains the exact dimensional constraints, Intelligent Character Recognition (ICR) capture zones, and the physical print layout for the **Legal-Size Special Accessibility Ballot**. 
This document aligns with the requirements of the **[Elections Act](../CA/CA_ELECTIONS_20260401.md)**, maintaining a strictly non-partisan framework with zero party affiliations.

---

## Section 1 - Scanner Calibration & Configuration Matrix (ICR Zones)
Because this ballot relies on large write-in fields instead of optical checkboxes, the scanner software must be configured to crop and capture high-resolution image zones for human or AI transcription.
All coordinates are measured from the **Top-Left Corner Registration Mark (0.00, 0.00)**.

| Feature / Element         | X-Coordinate Start | Operational Width  | Y-Coordinate Range                | Target Function       |
|---------------------------|--------------------|--------------------|-----------------------------------|-----------------------|
| **Left Timing Track**     | 0.500" (12.70 mm)  | 0.250" (6.35 mm)   | 0.500" to 13.000"                 | Scanner Feed Sync     |
| **Right Timing Track**    | 7.750" (196.85 mm) | 0.250" (6.35 mm)   | 0.500" to 13.000"                 | Scanner Feed Sync     |
| **Zone 1 (Riding Rep)**   | 1.000" (25.40 mm)  | 6.500" (165.10 mm) | 3.500" to 5.000" (Height: 1.5")   | ICR Text Capture Zone |
| **Zone 2 (Senate Med)**   | 1.000" (25.40 mm)  | 6.500" (165.10 mm) | 5.750" to 7.250" (Height: 1.5")   | ICR Text Capture Zone |
| **Zone 3 (Senator)**      | 1.000" (25.40 mm)  | 6.500" (165.10 mm) | 8.000" to 9.500" (Height: 1.5")   | ICR Text Capture Zone |
| **Zone 4 (National Rep)** | 1.000" (25.40 mm)  | 6.500" (165.10 mm) | 10.250" to 11.750" (Height: 1.5") | ICR Text Capture Zone |

### Page Geometry
* **Paper Dimensions:** 8.500" × 14.000" (Standard Legal Size).
* **Orientation:** Portrait.
* **Format:** Single-sided (to prevent ink bleed-through from thick markers or heavy pen pressure into the ICR capture zones).
* **Scanner Quiet Zone:** Minimum margin of **0.500" (12.7 mm)** on all edges.

---

## Section 2 - Layout Template (Portrait Vertical Stack)

```
[FIDUCIAL: TOP-LEFT]                                    [FIDUCIAL: TOP-RIGHT]
█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█
■                                                                           ■
■              HUDSON REPUBLIC - SPECIAL ACCESSIBILITY BALLOT               ■
■                                                                           ■
■ INSTRUCTIONS TO VOTER: Print the full name of your chosen candidate       ■
■ clearly inside the box designated for each role. Do not write parties.    ■
■ ------------------------------------------------------------------------- ■
■                                                                           ■
■  [ ROLE 1 ] RIDING REPRESENTATIVE                                         ■
■  ┌─────────────────────────────────────────────────────────────────────┐  ■
■  │                                                                     │  ■
■  │                                                                     │  ■
■  │                                                                     │  ■
■  └─────────────────────────────────────────────────────────────────────┘  ■
■                                                                           ■
■  [ ROLE 2 ] SENATE MEDIATOR                                               ■
■  ┌─────────────────────────────────────────────────────────────────────┐  ■
■  │                                                                     │  ■
■  │                                                                     │  ■
■  │                                                                     │  ■
■  └─────────────────────────────────────────────────────────────────────┘  ■
■                                                                           ■
■  [ ROLE 3 ] SENATOR                                                       ■
■  ┌─────────────────────────────────────────────────────────────────────┐  ■
■  │                                                                     │  ■
■  │                                                                     │  ■
■  │                                                                     │  ■
■  └─────────────────────────────────────────────────────────────────────┘  ■
■                                                                           ■
■  [ ROLE 4 ] NATIONAL REPRESENTATIVE                                       ■
■  ┌─────────────────────────────────────────────────────────────────────┐  ■
■  │                                                                     │  ■
■  │                                                                     │  ■
■  │                                                                     │  ■
■  └─────────────────────────────────────────────────────────────────────┘  ■
■                                                                           ■
■ █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█ ■
■                  |||||||||||||| [STYLE_ID: SPEC-LEG-V] ||||||||||||||     ■
█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
[FIDUCIAL: BOTTOM-LEFT]                              [FIDUCIAL: BOTTOM-RIGHT]
```

---

## Disclaimer
**All variable types require lowercase names and all multi-word variable names require the use of underscores (_), instead of spaces ( ).**

---

**Original Author**:

**House Signature** (only if attached to a parent instrument):

**Senate Signature** (only if attached to a parent instrument):

**Executive Office Signature**:

**FQLN**: FO_BALLOTSPECIAL_20260529
