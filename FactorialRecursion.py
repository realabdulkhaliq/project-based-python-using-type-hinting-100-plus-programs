def factorial(n):
    if n < 0:
        return "Factorial does not exist for negative numbers"
    elif n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    

num = int(input("Enter a number whose factorial did you want between 0 - 998: "))
if num < 999:
    print("The factorial of", num, "is", factorial(num))
else:
    print("Please enter a number between 0 - 998. After this maximum recursion depth exceeded")