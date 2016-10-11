x = int(input())
pn = []
for d in range(x):
    n = int(input())
    prime = 0
    for g in range(1,n):
        m = 2     
        s = g + 1
        while (m != s) or s == 2:
            if s / 2 < m:
                m = 2
                while (m != (2*s+1)) or (2*s+1) == 2:
                    if (2*s+1)/2 < m:
                        prime += 1
                        break
                    elif (2*s+1) % m == 0:
                        break
                    m += 1
                break
            elif s % m == 0:
                break
            m += 1
    pn.append(prime)
for i in range(x):
    print("Case #%d: %d" %(i+1,pn[i]))