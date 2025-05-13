def NaturalNoSum(n):
    if n <= 1:
        return n
    else:
        return n + NaturalNoSum(n-1)

n = int(input("Enter a number: "))

if n < 0:
    print("Please enter a positive number")
else:
    print("The sum of the first", n, "natural numbers is:", NaturalNoSum(n))