num = int(input("Enter a number whose table did you want to print: "))

# For loop to print the table of the number
for i in range(1, 11):
    print(num, "x", i, "=", num * i)

# While loop to print the table of the number
i = 1
while (i > 11):
    print(num, "x", i, "=", num * i)
    i += 1