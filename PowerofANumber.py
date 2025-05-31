base_number = int(input("Enter the base number: "))
exponent = int(input("Enter the exponent: "))

result = 1
# for i in range(exponent):
#     result *= base_number
# print(f"{base_number} raised to the power of {exponent} is: {result}")

# Alternative method using a while loop
while exponent > 0:
    result *= base_number
    exponent -= 1

print(f"{base_number} raised to the power of {exponent} is: {result}")
