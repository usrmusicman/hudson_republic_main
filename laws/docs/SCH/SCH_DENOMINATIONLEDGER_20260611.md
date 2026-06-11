# Hudson Denomination Ledger Schedule

---

## Hard Dependencies
List any legislative instrument(s) (in alphabetical order) that this article must depend on. List the FQLN(s) below. Any FQLN(s) mentioned in other sections are considered to be references and not actual dependencies.  
Only **Constitutional Articles (CA)**, **Legislative Articles (LA)** and **Legislative Codes (CO)** can be listed here.

* **[CA_THEINDIVIDUAL_20260401](./CA_THEINDIVIDUAL_20260401.md)**
* **[LA_HUDSONLEDGER_20260401](../LA/LA_HUDSONLEDGER_20260401.md)**

---

## Definitions

- **HCB8 (Hudson Copper Beaver 8)**: The base indivisible accounting unit equal to 1/8 troy ounce of copper bullion.  
- **Action Type**: Single character prefix in ledger records (`A` = Added, `R` = Removed, `F` = Fraudulent, `B` = Blacklisted).  
- **q Counter**: Sequential identifier (1–9999) for bulk entries sharing the same Entry Address within one execution of the tool. Resets to 1 on every new run.  
- **Trinity Check**: The unique combination of Action Type + Entry Address + Transaction Amount used to prevent double entries.  
- **Liquidity Divisor**: Value (1, 2, 4, or 8) that applies a right bitshift to copper units only.  
- **Unit Type**: Physical form factor of the bullion (Bar, Coin, or Round).

---

## Preamble
This schedule defines the denomination structure, binary representation rules, scaling mechanics, transaction recording formats, HLDP receipt standards, and command-line interface for the Hudson (Beaver) Ledger. It operationalizes the requirements for sound, auditable, and tamper-evident bullion accounting while preserving the fixed 64:64:8 ratio architecture.

---

## Usage
This document serves as the authoritative technical reference for all software implementations (including the official offline tool), validators, auditors, and manual ledger operations. All Hudson Ledger records and tools **must** conform exactly to the formats and rules defined herein.

---

## Hudson (Beaver) Ledger
This is the bullion registration ledger for the Hudson Republic.

### Directory Structure
Receipts Path (Added): receipts/added/[Business Code]_[Entry Address]_[ACTION].hldp  
Receipts Path (Removed): receipts/removed/[Business Code]_[Entry Address]_[ACTION].hldp  
Receipts Path (Fraud): receipts/fraud/[Business Code]_[Entry Address]_[ACTION].hldp  
Receipts Path (Blacklisted): receipts/blacklist/[Business Code]_[Entry Address]_[ACTION].hldp  
Hudson (Beaver) Ledger Path: ledger/hudson_ledger_records_[Business Code]_[YYYYYYYYYYYY]YYYY.txt

### Ledger Records
Name: Ledger Record  
Version: 1  
File Type (Short): txt  
File Type (Long): Plain Text File  
File Metadata: text/plain  
Filename: hudson_ledger_records_[Business Code]_[YYYYYYYYYYYY]YYYY.txt

### Ledger Records Internals 

**High level**  
[Action Type]|[Specification Version]|[Timecode]|[Country Code]|[Riding Code]|[Business Code]|[Entry Address]|[Transaction Amount]|[Metal Code]|[Liquidity Divisor]|[Associated Hash]

**Low Level**  
"V"N"|"q[QQQ]Q"|"([YYYYYYYYYYYY]YYYY:MM:DD:hh:mm:ss)"|"OOO"|"RRRR"|"BBBB-BBBB"|"[YYYYYYYYYYYY]YYYY_XXXXXXXXXXXXXXXX"|"$G.ggg.SSS.sss.CCC.ccc.ZZZ"|"Mb"|/"n"|"H

**Unchanging Characters**  
All characters that are in between double quotes are rendered as is and are not interpreted.

**Dynamically Expanding / Invisible field characters**  
Any characters in between square braces are considered to exist, but not displayed currently on the ledger. These are for future expansion to prevent bugs related to date collisions, millennium bugs, buffer overflows, etc...

**Dynamic Elements of the ledger**  
() = Date inside using custom format.  
| = The primary field separator.

**Action Type**  
q = This character tells what type of operation will occur. A for added, R for removed, F for fraudulent and B for blacklisted.  
Q = This is a base10 number which is used to denote bulk entries of the same [Entry Address], per transaction. Valid values are (0-9). This iterates from the number 1 upward to 9999. It resets back to 1 for a new transaction. This reset is per run of the python script for better accountability.

**Specification Version**  
V = Version of the specification.  
N = This is a variable length, base10, integer number value only that represents the specification version.

**Country Code**  
OOO = Country code (3 uppercase alpha characters only). Valid values are (A-Z).

**Riding Code**  
RRRR = Riding code (4 hexadecimal characters only). Valid values are (0-F)

**Business Code**  
BBBB-BBBB = This is a base21, uppercase alpha character string. There are no vowels allowed (A, E, I, O, U). Valid values are (B-D,F-H,J-N,P-T,V-Z).  
- Reserved addresses are BBBB-BBBB for unregistered businesses and ZZZZ-ZZZZ for public sector services.

**Timecode**  
([YYYYYYYYYYYY]YYYY:MM:DD:hh:mm:ss)

**Entry Address**  
Y = This is the year the bullion was issued. It is a base10 number, valid values are (0-9).  
X = This is a randomly generated base16 number, valid values are (0-F).

**Transaction Amount**  
$ = This is the sign used, (+) is used for addition and (-) is used for subtraction.  
G = This is a base10, variable length field number which is measured in gold units of (1) troy oz increments. Valid values are (0-9).  
g = This is a base2 number which is measured in gold units of (1/8) troy oz increments. Valid values are (0-1).  
S = This is a base2 number which is measured in silver units of (1) troy oz increments. Valid values are (0-1).  
s = This is a base2 number which is measured in silver units of (1/8) troy oz increments. Valid values are (0-1).  
C = This is a base2 number which is measured in copper units of (1) troy oz increments. Valid values are (0-1).  
c = This is a base2 number which is measured in copper units of (1/8) troy oz increments. Valid values are (0-1).  
Z = This is a base2 number which is measured in copper units of (1/8) troy oz increments. The .ZZZ field is only shown in the transaction when the chosen divisor is greater than 1. Valid values are (0-1).

**Metal Code**  
M = This is the metal type chosen at the command line. G is for gold, S is for silver, C is for copper.  
b = This is the form factor whether in bars, coins or rounds. The values that represent these are "B" and "R" respectively.

**Liquidity Divisor**  
n = This is the numeric divisor value that is applied to the transaction. It bitshifts to the right the ccc section's values. This divisor value is in base10 and moves the 1oz line a certain amount to the right. Accepted bitshift values are >>0, >>1, >>2, >>3, or a divisor of 1, 2, 4, 8.

**Associated Hash**  
H = This is the hash for integrity checks.

**Other notes**:
- When the -5 option is chosen in combination with a valid (1/2) troy oz metallic hex code, then any (1/10) troy oz metallic coins/bars can be recorded to the ledger as mandatory 5 unit increments.  
	- When the -5 switch is used instead of -1, 5 entries are created with the same exact [Entry Address], but they all have different hashes to distinguish them from one another.  
	- Also, the first [transaction amount] value recorded gets the full amount of (1/2) troy oz of any chosen (1/2) troy oz metal hex code value.  
	- The other 4 entries show the same sign as the operation chosen, but an amount of 0.000.000.000.000.000 or 0's across the board, including the extra 0's needed, the bitshift divisor applied and exact metal code.  
- The normal ledger transaction amount is displayed 0.000.000.000.000.000.  
	- This is the legal standard format for settling all transactions, including emergency divisor increases.  
- The emergency ledger transaction amount is displayed 0.000.000.000.000.000.000 to allow for a temporary view of liquidity injection.  
	- The right most octet group is ignored in regular and emergency transactions. This extra octet is to expand copper's supply during a period where liquidity expansion is absolutely required.  
	- Silver and Gold octets do not move with the shift.

### Liquidity Scaling (Copper Only Expansion)

**Scaling Factors**

| Scaling Factor | HCB8 Units per 1 Gold oz | Binary Threshold | Description |
|----------------|--------------------------|------------------|-----------|
| 1x (Normal)    | 32,768                   | 2¹⁵              | Standard operation |
| 2x             | 65,536                   | 2¹⁶              | Moderate liquidity boost |
| 4x             | 131,072                  | 2¹⁷              | Significant liquidity boost |
| 8x             | 262,144                  | 2¹⁸              | Maximum emergency liquidity |

**Key Rules**:
- Gold and Silver octet positions remain fixed.
- Only copper is affected by the divisor.
- The rightmost octet (`.ZZZ`) becomes visible when `divisor > 1`.
- Scaling requires formal declaration and step-down procedure.

---

## Hudson Ledger Denomination Paper
Filename: [Business Code]_[Entry Address]_[ACTION].hldp  
File Type (Short): hldp  
File Type (Long): Hudson Ledger Denomination Paper  
File Metadata: text/plain

### HLDP Internals
Name: Ledger Unit Record  
Specification Version: [Version Number given by N in the Hudson Ledger Record]  
Hashing Algorithm: [Algorithm Choice]  
Algorithm Strength: [Strength]

**BOOKEEPING**  
Riding: [Riding Code]  
Business: [Business Code]  
Action: [Whether the item was ADDED (+), REMOVED (-) or FRAUD/BLACKLISTED (~)]  
Record: [Entry Address]  
Year: [YYYYYYYYYYYY]YYYY  
Timecode: [System timecode based on UTC and ISO 8601]

**RECORD OF DENOMINATION**  
Unit Type: [Bar, Coin or Round]  
Country: [Country Code]  
Metal: [Metal name chosen]  
Weight: [Weight in troy oz chosen]  
Purity: [Minimum acceptable purity for the chosen financial instrument]  
Amount: [Transaction Amount]  
Divisor: [Divisor value]

**COMMENTS**  
Comment: "[Primary comment]"  
Comment 2: "[Comment 2 (only with the -5 switch)]"  
Comment 3: "[Comment 3 (only with the -5 switch)]"  
Comment 4: "[Comment 4 (only with the -5 switch)]"  
Comment 5: "[Comment 5 (only with the -5 switch)]"

**INTEGRITY**  
Hash Value: "[Associated Hash]"

**GENERATOR**  
Command: "[Full Commandline used to generate the output]"

---

## Command Line Options (Hudson Ledger Records Script)

**Command**: ./hudson_ledger_offline_tool.py

**Options**

**Parent Commandline options**  
-a/--add: Add entry(s) to ledger with (+) sign in place of ($) and generate corresponding hldp receipt.  
-r/--remove: Add entry(s) to ledger with (-) sign in place of ($) and generate corresponding hldp receipt.  
- Provide a hldp filename to check for hash entries.  
- Find the associated hash(s) match(s) in the ledger from the hldp file, copy the ledger entries to another line and remember to make the ($) sign a (-) in front of [transaction amount].  
-f/--fraud: Add entry(s) to ledger with (~) sign in place of ($) and generate corresponding hldp receipt.  
--blacklist: Add entry(s) to ledger with (~) sign in place of ($) and generate corresponding hldp receipt.  

**Required Child Commandline options**  
-1: Adds a single ledger entry and hldp for denominations (1/8) troy oz, (1/4) troy oz, (1/2) troy oz, (1) troy oz, (5) troy oz, (10) troy oz, (100) troy oz.  
-5: Adds 1 ledger entry for 5 (1/10) troy oz units  
- [Associated Hash] is unique to every entry and is represented by 5 different hashes, each is on a different line.  
- [Comment (entry number)] is used to briefly describe which each item is.  
- Comments must be enclosed in-between double (") and separated by a comma. They are listed after the command and any arguments.  
	- Command: ./hudson_ledger_offline_tool.py [any arguments and values] "Primary comment","Comment 2","Comment 3","Comment 4","Comment 5"  
- This option records 5, (1/10) troy oz bullion units as a single 1 (1/2) troy oz entry. This overrides the -v/--value option.

**Key Parameters**  
-b/--business-code: This is the business certificate code issued to the business upon registering with the government.  
-R/--riding-code: This is the code that is designated to a specific riding.  
-c/--country: This is a 3 uppercase alpha-character code used to identify your nation. These can be found in ISO 3166.  
-m/--metal: (G) for gold, (S) for silver, (C) for copper.  
-t/--type: (b) for institutional bars, (c) for minted coins, (r) for blanks or custom minted bullion rounds.  
-v/--value: 1 for (1) troy oz, 2 for (1/2) troy oz, 4 for (1/4) troy oz, 5 for (5) troy oz, 8 for (1/8) troy oz, 10 for (10) troy oz, 100 for (100) troy oz.  
--divisor: The value used to add liquidity to copper only, not silver, not gold and to unlock the non-standard sixth octet.  
- Values are: 1 for a bitshift of 0 to the right, 2 for a bitshift of 1 to the right, 4 for a bitshift of 2 to the right, 8 for a bitshift of 3 to the right.  
- This option is heavily discouraged in the Republic and all legal transactions recognized in the Republic, outside of true emergencies, default to 1 or a bitshift of 0 to the right.  
--entropy: This is an argument provided, 16 character, hexadecimal, base16 value.  
--random: This generates a completely random, 16 character, hexadecimal, base16 value. It has no arguments.

**Optional flags (Default hash algorithm is sha3, strength 512)**  
-h/--hash: This is your choice of hashing algorithm (i.e. sha1, sha2, md5, sha3)  
--strength: This is the hash's strength using a base10 numeric value "64, 128, 256, 512, 1024, etc".

**Usage**  
EXTERNAL LINK: [Secure Hashing Algorithms](https://en.wikipedia.org/wiki/Secure_Hash_Algorithms)  

**Notes**  
- The year is generated by the script itself at runtime and uses the [YYYYYYYYYYYY]YYYY format.  
- The script in the --remove option will utilize the same scraped metadata as [Business Code]_[Entry Address]_ADDED.hldp, but it will generate its own unique hash for all its entry(s) in the ledger and [Business Code]_[Entry Address]_REMOVED.hldp file.  
- If no hldp file exists by the provided argument or is not provided with the --remove option, then the script will return an error and will stop execution.  
- If using the --entropy option there will be a confirmation prompt.  
- It will check the hudson_ledger_records_[Business Code]_[YYYYYYYYYYYY]YYYY.txt file to determine if there are any duplicate [Entry Address] that exist.  
- If duplicates are found then a warning is displayed and the script exits before the confirmation prompt appears.  
- This prompt asks you to confirm committing to the ledger and creating the associated [Business Code]_[Entry Address]_[ACTION].hldp file.  
- The --fraud and --blacklist global switch options do not take --random as an option. Please use --entropy for the offending bullion unit instead.  
- If the [Action Type], [Entry Address] and [Transaction Amount] fields are all the same as the user's input from the script, then the entry will fail to be entered and produce an error.  
- This is to prevent double entries and to keep clean records for future audits.  
- Default hashing algorithm is sha3 and the default strength is 512 bits.

### Required For Primary Switches (Hudson Ledger Records Script)

Required for the --add option  
python3 hudson_ledger_offline_tool.py --add -1/-5 --country <argument> --riding-code <argument> --business-code <argument> --metal <argument> --type <argument> --value <argument> --random/--entropy <argument> --hash <argument> --strength <argument> <comment>,<(-5) switch comment 2>,<(-5) switch comment 3>,<(-5) switch comment 4>,<(-5) switch comment 5>

Required for the --add option (non-standard six octets)  
python3 hudson_ledger_offline_tool.py --add -1/-5 --country <argument> --riding-code <argument> --business-code <argument> --metal <argument> --type <argument> --value <argument> --divisor <argument> --random/--entropy <argument> --hash <argument> --strength <argument> <comment>,<(-5) switch comment 2>,<(-5) switch comment 3>,<(-5) switch comment 4>,<(-5) switch comment 5>

Required for the --remove option  
python3 hudson_ledger_offline_tool.py --remove -1/-5 [Business Code]_[Entry Address]_ADDED.hldp. <comment>,<(-5) switch comment 2>,<(-5) switch comment 3>,<(-5) switch comment 4>,<(-5) switch comment 5>

Required for the --fraud option  
python3 hudson_ledger_offline_tool.py --fraud -1/-5 --entropy <argument>  
- With the -1 switch put "Comment: [Action Type]:[Entry Address] flagged for fraud inside the Hudson Republic" inside the [Business Code]_[Entry Address]_BLACKLISTED.hldp file.
- With the -5 switch put "Comment[1-5]: [Action Type]:[Entry Address] flagged for fraud inside the Hudson Republic" inside the [Business Code]_[Entry Address]_BLACKLISTED.hldp file.

Required for the --blacklist option  
python3 hudson_ledger_offline_tool.py --blacklist -1/-5 --entropy <argument>  
- With the -1 switch put "Comment: [Action Type]:[Entry Address] blacklisted for use in the Hudson Republic" inside the [Business Code]_[Entry Address]_BLACKLISTED.hldp file.
- With the -5 switch put "Comment[1-5]: [Action Type]:[Entry Address] blacklisted for use in the Hudson Republic" inside the [Business Code]_[Entry Address]_BLACKLISTED.hldp file.

**Double-Entry Prevention (Trinity Rule)**  
No two entries may share the same combination of Action Type, Entry Address, and Transaction Amount.

---

## Disclaimer
**All tags require lowercase names and all multi-word tags require the use of underscores (_), instead of spaces ( ).**

---

**Original Author**: 

**House Signature**:

**Senate Signature**:

**Executive Office Signature**: 

**FQLN**: SCH_DENOMINATIONLEDGER_20260611
