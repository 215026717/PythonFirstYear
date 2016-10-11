import math 
n = int(input("Enter number here: "))
for i in range(n * 2):
    s = i + 1
    if (s) % 2 == 1:
        id = math.sqrt(s)
        print("Square root of", (s), "is", id)
