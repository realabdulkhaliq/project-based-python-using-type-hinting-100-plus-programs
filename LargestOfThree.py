num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if (num1 > num2):
    if (num1 > num3):
        print("Largest number is:", num1)
    else:
        print("Largest number is:", num3)
else:
    if (num2 > num1):
        print("Largest number is:", num2)
    else:
        print("Largest number is:", num3)


# Easy Way
if (num1 > num2 and num1 > num3):
    print("Largest number is:", num1)
elif (num2 > num1 and num2 > num3):
    print("Largest number is:", num2)
else:
    print("Largest number is:", num3)

# Using max function
largest = max(num1, num2, num3)
print("Largest number is:", largest)

# Using lambda function
largest = (lambda x, y, z: x if (x > y and x > z) else y if (y > x and y > z) else z)(num1, num2, num3)
print("Largest number is:", largest)