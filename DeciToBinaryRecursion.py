def DeciToBinary(n):
    """Convert a decimal number to binary using recursion."""
    if n > 1:
        DeciToBinary(n // 2)
    print(n % 2, end='')

# Get user input
num = int(input("Enter a decimal number: "))
if num < 0:
    print("Please enter a positive number")
else:
    print("The binary representation of", num, "is:" , end=' ')
    DeciToBinary(num) # Here due to positional argument error
    # print("The binary representation of", num, "is:" , DeciToBinary(num)) # error
    # print(DeciToBinary(num)) # error