# Python-String-Encryption-Decryption-Tool
This Python project implements a simple encryption and decryption system using character shifting. The project contains two main functions.
encrypt() – encrypts a string using a randomly generated key
decrypt() – decrypts the encrypted string using the provided key. 
The encryption logic is inspired by classical shift (Caesar-style) cyphers, with an added alphabet-based key representation.

How Encryption Works
A random number n is generated between 1 and 10.
Each character in the input string is shifted n positions forward in the alphabet.
The number n is converted into a letter based on its position in the English alphabet:
1 → A
2 → B
3 → C
…
A word starting with that letter is used as the encryption key.
The encrypted string and the key word are returned.

EXAMPLE
Input string:
"GREAT"
Random shift generated:
n = 2
Encrypted output:
ITGCV

Key generation:
2nd alphabet letter → B
Key word → ball

Final Output:
Encrypted Text: ITGCV
Key: ball

How Decryption Works:
The encrypted string and the key word are provided as input.
The first letter of the key word determines the shift value n.
Each character is shifted n positions backward.
The original message is recovered.

Features
Randomized encryption key
Alphabet-based key representation
Separate encryption and decryption functions
Simple and readable Python logic
Suitable for beginners and academic use

Project Structure
Encryption-Decryption-Tool/
│
├── main.py        # Contains encrypt and decrypt functions
├── README.md      # Project documentation
(Update filenames if necessary.)

How to Run the Program
Prerequisites:
Python 3.x installed
Steps:
python main.py

Concepts Used
Strings and ASCII manipulation
Functions
Random number generation
Conditional logic
Basic cryptography concepts

Future Improvements:
Support for lowercase letters and symbols
Stronger encryption logic
User-defined shift limits
File encryption support
GUI implementation

License
This project is open-source and available under the MIT License.

Author:
Hanya Mursaleen
Aspiring Computer Science Student | Python Developer
