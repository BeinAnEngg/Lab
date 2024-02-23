def binary_to_decimal(binary):
 decimal = 0
 power = 0
 while binary != 0:
 last_digit = binary % 10
 decimal += last_digit * (2 ** power)
 binary //= 10
 power += 1
 return decimal
def octal_to_hexadecimal(octal):
 decimal = 0
 power = 0
 while octal != 0:
 last_digit = octal % 10
 decimal += last_digit * (8 ** power)
 octal //= 10
 power += 1
 hexadecimal = ""
 hex_digits = "0123456789ABCDEF"
 while decimal != 0:
 remainder = decimal % 16
 hexadecimal = hex_digits[remainder] + hexadecimal
 decimal //= 16
 return hexadecimal
# Binary to Decimal conversion
binary_number = input("Enter a binary number: ")
decimal_number = binary_to_decimal(int(binary_number))
print("Decimal equivalent:", decimal_number)
# Octal to Hexadecimal conversion
octal_number = input("Enter an octal number: ")
hexadecimal_number = octal_to_hexadecimal(int(octal_number))
print("Hexadecimal equivalent:", hexadecimal_number)
