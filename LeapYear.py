# For century years
# If a year is divisible by 100 and also divisible by 400 then leap year otherwise not a leap year.
# For non-century years
# If a year is divisible by 4 and not divisible by 100 then leap year otherwise not a leap year.

year = int(input("Enter a year: "))
if (year % 400 == 0) and (year % 100 == 0):
    print(year, "is a leap year")
elif (year % 4 == 0) and (year % 100 != 0):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")