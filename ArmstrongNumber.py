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