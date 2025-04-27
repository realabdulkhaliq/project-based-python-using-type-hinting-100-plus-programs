import cmath
a = int(input("Enter a non zero first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

d = (b**2) - (4*a*c)
sqrt_d = cmath.sqrt(d)

sol1 = (-b + sqrt_d) / (2*a)
sol2 = (-b - sqrt_d) / (2*a)
print("The solution are {0} and {1}".format(sol1, sol2)) 