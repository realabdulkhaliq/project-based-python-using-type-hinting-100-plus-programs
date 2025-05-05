num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 % num2 == 0:
    print(num1, "is divisible by", num2)
elif num2 % num1 == 0:
    print(num2, "is divisible by", num1)
else:
    print(num1, "is not divisible by", num2)


numlist = [ 33, 39, 77, 65, 90, 100, 135, 150, 230, 270, 300 ]
num = int(input("Enter a number: "))

result = list(filter(lambda x: x % num == 0, numlist))
print("The numbers divisible by", num, "are:", result)