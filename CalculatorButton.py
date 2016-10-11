x = int(input("First number: "))
y = int(input("Second number: "))
z = int(input("Answer: "))
if x + y == x * y:
    print("Plus or Times")
elif x + y == z and x + y != x * y:
    print("Plus only")
elif x * y == z and x + y != x * y:
    print("Times only")
else:
    print("Neither Plus nor Times")
print("%d+%d=%d"%(x,y,(x+y)))
print("%dx%d=%d"%(x,y,(x*y)))