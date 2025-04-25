num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if (num1**2 == num2):
    print("Second Number is the square of first number")
elif (num2*num2 == num1):
    print("First Number is the square of second number")
else:
    print("Neither number is the square of the other")