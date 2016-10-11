# Author: Mongezi Nene

num = input("Enter integer here : ")
num = int(num)
num1 = num / 4
num2 = num / 9
if num1 == int(num1) and num2 == int(num2):
    print(num, "is divisible by 4 and 9")
elif num1 == int(num1) or num2 == int(num2):
    print(num, "is divisible by 4 or 9")
else:
    print(num, "is not divisible by 4 or 9")