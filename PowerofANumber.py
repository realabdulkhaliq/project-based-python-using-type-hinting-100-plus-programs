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


# Alternative method using recursion
def power(base, exp):
    if exp == 0:
        return 1
    else:
        return base * power(base, exp - 1)

# Using the recursive function
result_recursive = power(base_number, exponent)
print(f"{base_number} raised to the power of {exponent} is: {result_recursive}")


# Alternative method using Python's built-in exponentiation operator

print("=====")
print(f"{base_number} raised to the power of {exponent} using exponentiation operator is: {base_number ** exponent}")

