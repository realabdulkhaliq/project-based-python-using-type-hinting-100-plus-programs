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


# Using Lambda Function
terms = int(input("Enter the number of terms: "))
power_of_two = list(map(lambda x: 2 ** x, range(terms + 1)))
print("Power of 2:", power_of_two)


# Using List Comprehension 
power_of_two = [2 ** x for x in range(terms + 1)]
print("Power of 2:", power_of_two)

# Printing Individual Values
power_of_two = list(map(lambda x: 2 ** x, range(terms + 1)))
for i in range(terms + 1):
    print("The Value of 2 raised to the power of", i, "is", power_of_two[i])