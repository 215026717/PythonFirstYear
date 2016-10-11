x = int(input("Enter the number: "))
y = len(str(x))
for i in range(y,0,-1):
    st = x//(10**(i-1)) % 10
    pr = "*"*st
    print(st,pr)