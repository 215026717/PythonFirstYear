# Author: Mongezi Nene
# description: Solves equation 1
a = input("Enter the value of a: ")
a = float(a)

b = input("Enter the value of b: ")
b = float(b)

d = input("Enter the value of d: ")
d = float(d)

f = input("Enter the value of f: ")
f = float(f)

g = input("Enter the value of g: ")
g = float(g)

step1 = 24 + g
step2 = f * step1
step3 = 45 - step2
step4 = step3 / (a * b * d)

print("If a =", a, "b =", b, "d =", d, "f =", f, "and g =", g, "The answer is ", step4)