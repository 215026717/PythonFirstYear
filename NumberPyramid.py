lines = int(input("Enter :"))
last = lines * lines
order = len(str(last))
d = (lines * (order + 1))
m = 0
n = 0
f = order
for i in range(1,lines+1):
    d -= (order + 1)
    a = " " * d
    if m < 9 and lines > 3:
        s = " "
        print(s + a, end="")  
    else:
        print(a, end="")
    for j in range((i*i) - (i-1)*(i-1)):
        m += 1        
        if len(str(m-1)) != len(str(m)) and m != 0:
            f -= 1
        if (m == i * i):
            print(m)  
        else:
            print(m, end=" " * f)