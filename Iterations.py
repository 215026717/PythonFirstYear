import random
r = random.randint(1,10)
print("Random variable is", r)
n = int(input("Enter number [1 - 10]: "))
it = 0
while((r % n) > 0 or n < 1):
    if n % 2 == 0:
        n -= 1
    else:
        n -= 2
    it += 1
print(it, "iterations")
print("Updated input", n)
