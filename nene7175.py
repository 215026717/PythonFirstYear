# Author: Mongezi Nene
# description: A program that gives the day and month Easter Sunday occurs for a given year

# input the year
year = int(input("Enter a year: "))
# formulae used to calculate the and month that Easter Sunday occurs for that year

a = year % 19
b = int(year / 100)
c = year % 100
d = int(b / 4)
e = b % 4
f = int((b + 8) / 25)
g = int((b - f + 1) / 3)
h = (19 * a + b - d - g + 15) % 30
i = int(c / 4)
k = c % 4
l = (32 + 2 * e + 2 * i - h - k) % 7
m = int((a + 11 * h + 22 * l) / 451)
month = int((h + l - 7 * m + 114) / 31)
day = ((h + l - 7 * m + 114) % 31) + 1
# output the day and month of Easter Sunday for given year

if month == 4:
    print(day, "April", year)# output if month is April
else:
    print(day, "March", year)# output if month is March