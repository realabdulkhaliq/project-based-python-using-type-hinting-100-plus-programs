num = int(input("Enter a number: "))
rn = 0
while num > 0:
    rn = (rn * 10) + (num % 10)
    num //= 10

print("Reversed number:", rn)

# This code reverses any given number.

print("=====")
while num != 0:
    digit = num % 10
    rn = rn * 10 + digit
    num //= 10

print("Reversed number using while loop:", rn)
# This code reverses any given number using a while loop.



