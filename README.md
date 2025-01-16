# Vigenère Cipher Analysis

## Overiew:
This repository contains my implementation of a Python program designed to analyze ciphertext encrypted using the Vigenère Cipher.
The goal is to determine the correct key length by performing statistical analysis, specifically using the Index of Coincidence (IC) method.

## Objective:
The program performs the following tasks:
1. Accepts a ciphertext and possible key length guesses as inputs.
2. Computes the IC for each key length guess by dividing the ciphertext into groups based on the guessed key length.
3. Calculates the IC for each group and identifies the key length guess most likely to be correct (i.e., closest to the IC value for the English language).

## Features:
1. Calculates the frequency of letters in the ciphertext groups.
2. Uses the IC formula to analyze whether the guessed key length is correct.
3. Outputs the IC value for each guessed key length and determines the most likely key length.
   
## Program Methodology
Input: Ciphertext and guessed key lengths.
Output: IC values for each key length and the most probable correct key length.
The program uses the Index of coincidence (IC) formula for calcualtion.
For more information on the Index of Coincidence (IC) and its applications in cryptography, you can visit [Index of Coincidence ](https://pages.mtu.edu/~shene/NSF-4/Tutorial/VIG/Vig-IOC.html). This link provides the IC formula and the English value of IC, both of which are useful for understanding and implementing the calculations in my code.


## Testing:
The program was tested on a sample plaintext of at least 1000 words, encrypted with the Vigenère Cipher using a specific key. It computed IC values for three key length guesses (4, 5, and 6).

## Note:
The code, pseudocode, and testing process in this repository are based on my own work. Redistribution, use, or modification of the content in this repository is prohibited without explicit permission.

## License:
The contents of this repository are my own work completed during my university coursework. Redistribution, use, or modification without explicit written permission is prohibited.
