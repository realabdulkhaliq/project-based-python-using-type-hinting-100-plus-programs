import calendar

year = int(input("Enter year: "))
month = int(input("Enter month number: "))

yearcalendar = calendar.calendar(year)
print(yearcalendar)


mycalendar = calendar.month(year, month)
print(mycalendar)