num = int(input("Enter a number: "))

sum = 0
temp = num
while temp > 0:
    digit = temp % 10
    cube = digit ** 3
    sum = sum + cube
    temp = temp // 10

if num == sum:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")


# The above code checks if any three digit number is an Armstrong number or not. 
# An Armstrong number is a number that is equal to the sum of its own digits raised 
# to the power of the number of digits. 
# For example, 153 is an Armstrong number because 1^3 + 5^3 + 3^3 = 153.


order = len(str(num))
sum = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** order
    temp //= 10

if num == sum:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")


# Armstrong numbers are numbers that are equal to the sum of their own digits raised to the power of the number of digits.


lower = int(input("Enter lower range: "))
upper = int(input("Enter upper range: "))


for num in range(lower, upper + 1):
    sum = 0
    temp = num
    order = len(str(num))
    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10

    if num == sum:
        print(num, end=" ")

print("are Armstrong numbers between", lower, "and", upper)

# The above code checks for Armstrong numbers in a given range.