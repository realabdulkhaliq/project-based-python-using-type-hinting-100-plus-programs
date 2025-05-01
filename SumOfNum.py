# This code calculates the sum of the first n natural numbers.
num = int(input("Enter a natural number: "))
sum = 0

if num < 0:
    print("Please enter a natural number")
else:
    for i in range(1, num + 1):
        sum += i

    print("The sum of the first", num, "natural numbers is:", sum)


