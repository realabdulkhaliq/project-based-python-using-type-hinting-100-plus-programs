def calcHCF(x,y):
    """Calculate the HCF of two numbers."""
    if x > y:
        smaller = y
    else:
        smaller = x

    for i in range(1, smaller + 1):
        if (x % i == 0) and (y % i == 0):
            hcf = i

    return hcf

# Get input from the user
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

print("The HCF of", x, "and", y, "is", calcHCF(x, y))