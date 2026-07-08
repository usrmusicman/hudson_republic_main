# Math Examples For The Hudson Transaction Ledger

## Decimal input example:

Example: 150.30 silver oz at a scaling factor of 1x (32,768 HCB8 for 1 oz gold) and a bitshift tax rate of >>4.


**First convert the 150.30 silver oz to HCB8**

**Convert the base10 silver oz amount to HCB8**
150.30 * 2^8 = 150.30 * 256 = 38,476.80 HCB8

**Round the HCB8 value up to the nearest whole number, due to this being an expense to be fulfilled.**
38,476.80 HCB8 = 38,477 HCB8

**Next convert this value to binary**
38,477 - (32,768 * 1) = 1 (1) gold troy oz and a 5,709 difference.
5,709 - 4,096 = 1 (1/8) gold troy oz and a 1,613 difference.
1,613 - 1,024 = 2 (1) silver troy oz and a 589 difference.
589 - 512 = 1 (1) silver troy oz and a 77 difference.
77 - 64 = 1 (1/8) silver troy oz and a 13 difference.
13 - 8 = 1 (1) copper troy oz and a 5 difference.
5 - 4 = 4 (1/8) copper troy oz and a 1 difference.
1 - 1 = 1 (1/8) copper troy oz and a 0 difference.

**Pure binary representation (6 octets in memory for math calculations)**
1.001.011.001.001.101.000

**Time to calculate the taxes of (>>4). The vertical pipe (|) shows the cutoff point**
1.001.011.001.00|1.101 or 100101100100

**Now lets pad the front of the number with 0s befined by a bitsshift of >>4.**

**Pure binary representation (6 octets in memory for math calculations)**
0.000.100.101.100.100.110

**Finally add the unadjusted amount and the taxation amount together**

**Pure binary hybrid representation (6 octets in memory for math calculations)**
1.001.011.001.001.101.000 + 0.000.100.101.100.100.110 = 1.001.111.110.110.001.110

**Double check that only the 0 leftmost binary bits in the sixth octet are accounted for. The vertical pipe (|) shows the cutoff point**
1.001.111.110.110.001.|110

**Finally, convert back to a decimal / binary hybrid representation for recording the adjusted amount on the ledger.**

**(6 octets in memory for math calculations)**
1.001.111.110.110.001.000

**(5 octets for display and ledger recording at 1x scaling)**
1.001.111.110.110.001




## Decimal / Binary hybrid input (The ledger recorded format) example:

Example: 15.110.010.001.011.100.110 at a scaling factor of 4x (131,072 HCB8 for 1 oz gold) and a bitshift tax rate of >>4.


**First convert the decimal (1) gold troy oz field to binary**

15 / 8 = 1 with a 7 remainder
7 / 4 = 1 with a 3 remainder
3 / 2 = 1 with a 1 remainder
1 / 1 = 1

1111 is the binary representation.

**Pure binary representation**
1,111.110.010.001.011.100.110

**Next apply the bitshift taxation >>4. The vertical pipe (|) shows the cutoff point**
1,111.110.010.001.011.10|0.110 or 111111001000101110

**Now lets pad the front of the number with 0s befined by a bitsshift of >>4.**
0,000.111.111.001.000.101.110

**Finally add the unadjusted amount and the taxation amount together**

**Pure binary representation**
1,111.110.010.001.011.100.110 + 0,000.111.111.001.000.101.110 = 10,000.110.001.010.100.010.100

**Double check that only the 2 leftmost binary bits in the sixth octet are accounted for. The vertical pipe (|) shows the cutoff point**
10,000.110.001.010.100.010.10|0

**Finally, convert back to a decimal / binary hybrid representation for recording the adjusted amount on the ledger.**
16.110.001.010.100.010.100




## Decimal / Octal hybrid input example:

Example: 0.2.4.3.1.6.7 at a scaling factor of 2x (65,536 HCB8 for 1 oz gold) and a bitshift tax rate of >>3.


**First convert the decimal (1) gold troy oz field to binary

0 = 0 nothing to be done.

0 is the binary representation.

**Next convert the octal portion to binary.**

Octal: 0.2.4.3.1.6.7 to binary: 0.010.100.011.001.110.111

**Pure binary representation**
0.010.100.011.001.110.111

**Next apply the bitshift taxation >>4. The vertical pipe (|) shows the cutoff point**
0.010.100.011.001.110.|111 or 0010100011001110

**Now lets pad the front of the number with 0s befined by a bitsshift of >>3.**
0.000.010.100.011.001.110

**Finally add the unadjusted amount and the taxation amount together**

**Pure binary representation**
0.010.100.011.001.110.111 + 0.000.010.100.011.001.110 = 10,000.110.001.010.100.010.100

**Double check that only the leftmost binary bit in the sixth octet are accounted for. The vertical pipe (|) shows the cutoff point**
0.010.110.111.101.000.1|01

**Finally, convert back to a decimal / binary hybrid representation for recording the adjusted amount on the ledger.**
0.010.110.111.101.000.100




## HCB8 input example:

Example: 1,200,850 HCB8 units at a scaling factor of 8x (262,144 HCB8 for 1 oz gold) and a bitshift tax rate of >>5.

**If you have to find the whole (1) gold troy oz amount first.**
1,200,850 / 262,144 = 4.58

4 (1) gold troy oz of the batt.

**Convert the HCB8 value to binary**
1,200,850 - (262,144 * 4) = 4 (1) gold troy oz and a 152,274 difference.
152,274 - 131,072 = 4 (1/8) gold troy oz and a 21,202 difference.
21,202 - 16,384 = 4 (1) silver troy oz and a 4,818 difference.
4,818 - 4,096 = 1 (1) silver troy oz and a 722 difference.
722 - 512 = 1 (1/8) silver troy oz and a 210 difference.
210 - 128 = 16 (1) copper troy oz and a 82 difference.
82 - 64 = 8 (1) copper troy oz and a 18 difference.
18 - 16 = 2 (1) copper troy oz and a 2 difference
2 - 2 = 2 (1/8) copper troy oz and a 0 difference.

**Pure binary representation**
100.100.101.001.011.010.010

**Time to calculate the taxes of (>>5). The vertical pipe (|) shows the cutoff point**
100.100.101.001.011.0|10.010 or 100.100.101.001.011.0

**Now lets pad the front of the number with 0s befined by a bitsshift of >>5.**
000.001.001.001.010.010.110

**Finally add the unadjusted amount and the taxation amount together**

**Pure binary representation**
100.100.101.001.011.010.010 + 000.001.001.001.010.010.110

**Double check that only the 3 leftmost binary bits in the sixth octet are accounted for. The vertical pipe (|) shows the cutoff point**
100.101.110.010.101.101.000|

**Finally, convert back to a decimal / binary hybrid representation for recording the adjusted amount on the ledger.**
4.101.110.010.101.101.000

