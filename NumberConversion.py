decimal = int(input("Enter a decimal number: "))

binary = bin(decimal)
octal = oct(decimal)
hexadecimal = hex(decimal)

print("Decimal:", decimal, "in binary is", binary[2:])
print("Decimal:", decimal, "in octal is", octal[2:])
print("Decimal:", decimal, "in hexadecimal is", hexadecimal[2:])

print("Decimal:", decimal, "in binary is", format(decimal, 'b'))
print("Decimal:", decimal, "in octal is", format(decimal, 'o'))
print("Decimal:", decimal, "in hexadecimal is", format(decimal, 'x'))
print("Decimal:", decimal, "in binary is", format(decimal, 'X'))

binary_to_decimal = int(input("Enter a binary number: "), 2)
print("decimal is", binary_to_decimal)

octal_to_decimal = int(input("Enter an octal number: "), 8)
print("Decimal is", octal_to_decimal)

hexadecimal_to_decimal = int(input("Enter a hexadecimal number: "), 16)
print("Decimal is", hexadecimal_to_decimal)


# binary_str = input("Enter a binary number: ")
# decimal_num = int(binary_str, 2)
# print(f"Decimal value: of {binary_str} is {decimal_num}")

# # Manual conversion
# binary_str = input("Enter a binary number: ")
# decimal_num = 0

# for i, digit in enumerate(reversed(binary_str)):
#     if digit == '1':
#         decimal_num += 2 ** i

# print(f"Decimal value: {decimal_num}")

