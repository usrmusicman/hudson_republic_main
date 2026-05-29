# Hudson Republic - Official Ballot Template

---

## Hard Dependencies
List any legislative instrument(s) (in alphabetical order) that this article must depend on. List the FQLN(s) below. Any FLQN(s) mentioned in other sections are considered to be references and not actual dependencies.  
Only **Constitutional Articles (CA)**, **Legislative Articles (LA)** and **Legislative Codes (CO)** can be listed here.

Dependencies
* **[CA_ELECTIONS_20260401](../CA/CA_ELECTIONS_20260401.md)**

---

## Preamble
This specification sheet contains the precise calibration matrix for optical mark recognition (OMR) scanners, alongside the strictly non-partisan double-sided ballot layout.
This document aligns with the requirements of the **[Elections Act](../CA/CA_ELECTIONS_20260401.md)**, maintaining a strictly non-partisan framework with zero party affiliations.

---

## Section 1 - Scanner Calibration & Configuration Matrix
To ensure high-speed tabulators correctly identify and read voter selections, configure your translation engine to the following bounding values based from the **Top-Left Corner Registration Mark (0.00, 0.00)**:

| Feature / Element       | X-Coordinate Start | Width Range      | Y-Coordinate Pitch (Repeat Interval) | Total Rows      |
|-------------------------|--------------------|------------------|--------------------------------------|-----------------|
| **Left Timing Track**   | 0.500" (12.70 mm)  | 0.250" (6.35 mm) | 0.750" (19.05 mm) step from top      | 18 Total Blocks |
| **Right Timing Track**  | 7.750" (196.85 mm) | 0.250" (6.35 mm) | 0.750" (19.05 mm) step from top      | 18 Total Blocks |
| **Col 1/3 Voting Boxes**| 1.000" (25.40 mm)  | 0.200" (5.08 mm) | Matches Timing Step (Rows 1-13)      | 13 Target Steps |
| **Col 2/4 Voting Boxes**| 5.100" (129.54 mm) | 0.200" (5.08 mm) | Matches Timing Step (Rows 1-13)      | 13 Target Steps |

### Page Geometry
* **Paper Dimensions:** 8.500" × 14.000" (Standard Legal Size).
* **Orientation:** Portrait.
* **Duplexing Mode:** Flip on Long Edge (Turn).
* **Scanner Quiet Zone:** Minimum margin of **0.500" (12.7 mm)** on all edges.

---

## Section 2 - Side A Layout Template (Front Page) - Roles 1 & 2

```
[FIDUCIAL: TOP-LEFT]                                                      [FIDUCIAL: TOP-RIGHT]
█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█
■                                                                                             ■
■                            HUDSON REPUBLIC - ELECTION BALLOT                                ■
■                                                                                             ■
■   INSTRUCTIONS TO VOTER:                                                                    ■
■   1. Use a black or blue pen to completely fill in the target box [ ] next to your choice.  ■
■   2. Vote for exactly ONE (1) candidate per role column.                                    ■
■   3. If you make an error, do not cross out; request a new ballot.                          ■
■                                                                                             ■
■ ------------------------------------------------------------------------------------------- ■
■   [ COLUMN 1 / ROLE 1 ]                          [ COLUMN 2 / ROLE 2 ]                      ■
■   TITLE: RIDING REPRESENTATIVE                   TITLE: SENATE MEDIATOR                     ■
■   Vote for exactly ONE (1)                       Vote for exactly ONE (1)                   ■
■ ------------------------------------------------------------------------------------------- ■
■                                                                                             ■
■   [ ] 01. CANDIDATE A-01                         [ ] 01. CANDIDATE B-01                     ■
■                                                                                             ■
■   [ ] 02. CANDIDATE A-02                         [ ] 02. CANDIDATE B-02                     ■
■                                                                                             ■
■   [ ] 03. CANDIDATE A-03                         [ ] 03. CANDIDATE B-03                     ■
■                                                                                             ■
■   [ ] 04. CANDIDATE A-04                         [ ] 04. CANDIDATE B-04                     ■
■                                                                                             ■
■   [ ] 05. CANDIDATE A-05                         [ ] 05. CANDIDATE B-05                     ■
■                                                                                             ■
■   [ ] 06. CANDIDATE A-06                         [ ] 06. CANDIDATE B-06                     ■
■                                                                                             ■
■   [ ] 07. CANDIDATE A-07                         [ ] 07. CANDIDATE B-07                     ■
■                                                                                             ■
■   [ ] 08. CANDIDATE A-08                         [ ] 08. CANDIDATE B-08                     ■
■                                                                                             ■
■   [ ] 09. CANDIDATE A-09                         [ ] 09. CANDIDATE B-09                     ■
■                                                                                             ■
■   [ ] 10. CANDIDATE A-10                         [ ] 10. CANDIDATE B-10                     ■
■                                                                                             ■
■   [ ] 11. CANDIDATE A-11                         [ ] 11. CANDIDATE B-11                     ■
■                                                                                             ■
■   [ ] 12. CANDIDATE A-12                         [ ] 12. CANDIDATE B-12                     ■
■                                                                                             ■
■ ------------------------------------------------------------------------------------------- ■
■   [ ] Write-In: _________________                [ ] Write-In: _________________            ■
■                                                                                             ■
■ █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█   ■
■                      |||||||||||||||||||||| [STYLE_ID: PAGE-1] |||||||||||||||||||||        ■
█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
[FIDUCIAL: BOTTOM-LEFT]                                                [FIDUCIAL: BOTTOM-RIGHT]
```

---

## Section 3 - Side B Layout Template (Back Page) - Roles 3 & 4

```
[FIDUCIAL: TOP-LEFT]                                                      [FIDUCIAL: TOP-RIGHT]
█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█
■                                                                                             ■
■                            HUDSON REPUBLIC - ELECTION BALLOT                                ■
■                                       (PAGE 2)                                              ■
■                                                                                             ■
■ ------------------------------------------------------------------------------------------- ■
■   [ COLUMN 3 / ROLE 3 ]                          [ COLUMN 4 / ROLE 4 ]                      ■
■   TITLE: SENATOR                                 TITLE: NATIONAL REPRESENTATIVE             ■
■   Vote for exactly ONE (1)                       Vote for exactly ONE (1)                   ■
■ ------------------------------------------------------------------------------------------- ■
■                                                                                             ■
■   [ ] 01. CANDIDATE C-01                         [ ] 01. CANDIDATE D-01                     ■
■                                                                                             ■
■   [ ] 02. CANDIDATE C-02                         [ ] 02. CANDIDATE D-02                     ■
■                                                                                             ■
■   [ ] 03. CANDIDATE C-03                         [ ] 03. CANDIDATE D-03                     ■
■                                                                                             ■
■   [ ] 04. CANDIDATE C-04                         [ ] 04. CANDIDATE D-04                     ■
■                                                                                             ■
■   [ ] 05. CANDIDATE C-05                         [ ] 05. CANDIDATE D-05                     ■
■                                                                                             ■
■   [ ] 06. CANDIDATE C-06                         [ ] 06. CANDIDATE D-06                     ■
■                                                                                             ■
■   [ ] 07. CANDIDATE C-07                         [ ] 07. CANDIDATE D-07                     ■
■                                                                                             ■
■   [ ] 08. CANDIDATE C-08                         [ ] 08. CANDIDATE D-08                     ■
■                                                                                             ■
■   [ ] 09. CANDIDATE C-09                         [ ] 09. CANDIDATE D-09                     ■
■                                                                                             ■
■   [ ] 10. CANDIDATE C-10                         [ ] 10. CANDIDATE D-10                     ■
■                                                                                             ■
■   [ ] 11. CANDIDATE C-11                         [ ] 11. CANDIDATE D-11                     ■
■                                                                                             ■
■   [ ] 12. CANDIDATE C-12                         [ ] 12. CANDIDATE D-12                     ■
■                                                                                             ■
■ ------------------------------------------------------------------------------------------- ■
■   [ ] Write-In: _________________                [ ] Write-In: _________________            ■
■                                                                                             ■
■ █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█   ■
■                      |||||||||||||||||||||| [STYLE_ID: PAGE-2] |||||||||||||||||||||        ■
█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
[FIDUCIAL: BOTTOM-LEFT]                                                [FIDUCIAL: BOTTOM-RIGHT]
```

---

## Disclaimer
**All variable types require lowercase names and all multi-word variable names require the use of underscores (_), instead of spaces ( ).**

---

**Original Author**:

**House Signature** (only if attached to a parent instrument):

**Senate Signature** (only if attached to a parent instrument):

**Executive Office Signature**:

**FQLN**: FO_BALLOTGENERAL_20260529

