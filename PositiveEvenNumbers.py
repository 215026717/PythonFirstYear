# Author: Mongezi Nene
# description: Program that reads in an integer and checks whether it is a positive, even number.

num = input("Enter integer here : ") 
num = int(num)
num1 = num / 2
if num1 == int(num1) and num > 0:
    print(num, "is a positive, even number")
else:
    print(num, "is not a positive, even number")