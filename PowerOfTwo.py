# This code calculates the power of 2 for a given range of numbers.
lower = int(input("Enter lower range: "))
upper = int(input("Enter upper range: "))

for i in range(lower, upper + 1):
    if i > 0:
        print( 2 ** i, end=" ")
    else:
        print("Power of 2 is not possible for negative numbers")
        break

if lower > 0 and upper > 0:
    for i in range(lower, upper + 1):
        print( 2 ** i, end=" ")
else:
    print("Power of 2 is not possible for negative numbers")


