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

