num = int(input("Enter a number whose factorial did you want: "))

fact = 1

if num < 0:
    print("Factorial does not exist for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1, num + 1):
        fact = fact * i
    print("The factorial of", num, "is", fact)


num = int(input("Enter a number whose factorial did you want: "))
def factorial(n):
    if n < 0:
        return "Factorial does not exist for negative numbers"
    elif n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    
# factorial(n)
print("The factorial of", num, "is", factorial(num))