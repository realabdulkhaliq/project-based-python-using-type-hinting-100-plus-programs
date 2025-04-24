# num = float(input("Enter any number: "))

# sq = num * num
# print("Square of given number is :", sq)

# sr = num ** 0.5
# print("Square root of given number is :", sr)

# import math
# sqroot = math.sqrt(num)
# print("Square root of given number is :", sqroot)

# square= math.pow(num, 2)
# print("Square of given number is :", square)

import math
num = float(input("Enter any number: "))
if (num > 0):
    s_root = math.sqrt(num)
    print("Square root of given number is :", s_root)
else:
    print("Square root of negative number is not possible")
