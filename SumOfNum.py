# This code calculates the sum of the first n natural numbers.
num = int(input("Enter a natural number: "))
sum = 0

if num < 0:
    print("Please enter a natural number")
else:
    for i in range(1, num + 1):
        sum += i

    print("The sum of the first", num, "natural numbers is:", sum)

if num < 0:
    print("Please enter a natural number")
else:
    while num > 0:
        sum += num
        num -= 1
    print("The sum of natural numbers is:", sum)


lower = int(input("Enter lower range: "))
upper = int(input("Enter upper range: "))

sum = 0

for i in range(lower, upper + 1):
    sum += i
print("The sum of natural numbers between", lower, "and", upper, "is:", sum)