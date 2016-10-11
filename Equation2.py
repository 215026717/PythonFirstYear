# Author: Mongezi Nene
# description: Solves equation 2

a = input("Enter the value of a: ")
a = float(a)

b = input("Enter the value of b: ")
b = float(b)

c = input("Enter the value of c: ")
c = float(c)

d = input("Enter the value of d: ")
d = float(d)

r = input("Enter the value of r: ")
r = float(r)

# First term
step1 = 4 / (3 * (r + 34))

# Second term
step2 = 9 * (a + b * d)

# Third term
step3 = (3 + d * (2 + a)) / (a + b * d)

# Answer
step4 = step1 + step2 + step3

print("If a =", a, "b =", b, "c =", c, "d =", d, "and r =", r, "The answer is ", step4)