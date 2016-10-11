x = int(input())
pn = []
for d in range(x):
    n = int(input())
    prime = 0
    for i in range(1,n):
        m = 2     
        s = i + 1
        while (m != s) or s == 2:
            if s / 2 < m:
                print(s)
                prime += 1
                break
            elif s % m == 0:
                break
            m += 1
    pn.append(prime)
for i in range(x):
    print("Case #%d: %d" %(i+1,pn[i]))