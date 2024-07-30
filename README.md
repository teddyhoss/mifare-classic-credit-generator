# Mifare Classic 1K Credit Generator

This Python script generates the necessary values to modify the credit in sector 2 of Mifare Classic 1K cards.

## How It Works

The credit in Mifare Classic 1K cards is usually stored in sector 2 and is expressed in cents. The script calculates and formats the values needed to modify this credit.

The structure of sector 2 is as follows:

1. First row (32 digits):
   - First 4 digits: Inverted current credit
   - 4 digits: 0000
   - 4 digits: Inverted checksum (calculated as 65535 - credit)
   - 4 digits: FFFF
   - 4 digits: Inverted current credit
   - 4 digits: 0000
   - 8 digits: Not important for credit modification

2. Second row (32 digits):
   - Has the same structure as the first row, but represents the previous credit
   - Must differ from the current credit by 1 coin (5 cents, 10 cents, 20 cents, 50 cents, 1 euro, 2 euros)

The script converts the user-input credit to hexadecimal and then inverts this value to obtain the data to be inserted into the card. It automatically calculates the checksum and generates both normal and inverted values.

## Usage

To use the script, run the following command:

python3 calc.py [Credit]

Where [Credit] is the desired credit value in cents.

The script will generate output with the calculated values. It's important to use the inverted value, which will be highlighted in color in the output.

## Important Note

Ensure that the difference between the current credit and the previous credit is always equal to one of the standard coins (5 cents, 10 cents, 20 cents, 50 cents, 1 euro, 2 euros). Different differences may cause the card to malfunction.

## Disclaimer

This script is provided for educational and research purposes only. Improper or unauthorized use to modify credit on Mifare Classic 1K cards may be illegal. The user is responsible for using this tool in compliance with all applicable laws and regulations.
