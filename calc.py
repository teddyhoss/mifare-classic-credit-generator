import sys

# ANSI color codes
RESET = "\033[0m"
CYAN = "\033[96m"
YELLOW = "\033[93m"

def decimal_to_hex_and_swap(decimal_num):
    hex_value = hex(decimal_num)[2:].zfill(4).upper()
    swapped_hex = hex_value[2:] + hex_value[:2]
    return hex_value, swapped_hex

def calculate_checksum(decimal_num):
    checksum = 65535 - decimal_num
    checksum_hex = hex(checksum)[2:].zfill(4).upper()
    checksum_hex_swapped = checksum_hex[2:] + checksum_hex[:2]
    return checksum, checksum_hex, checksum_hex_swapped

def colorize(text, color):
    return f"{color}{text}{RESET}"

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <decimal_number>")
        sys.exit(1)
    
    try:
        num = int(sys.argv[1])
        if num < 0 or num > 65535:
            raise ValueError("The number must be between 0 and 65535")
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

    original_hex, swapped_hex = decimal_to_hex_and_swap(num)
    checksum, checksum_hex, checksum_hex_swapped = calculate_checksum(num)

    print(f"Number: {num}")
    print(f"Hexadecimal: {original_hex}")
    print(f"Inverted hexadecimal: {colorize(swapped_hex, CYAN)}")
    print(f"Checksum: {checksum}")
    print(f"Hexadecimal checksum: {checksum_hex}")
    print(f"Inverted hexadecimal checksum: {colorize(checksum_hex_swapped, YELLOW)}")