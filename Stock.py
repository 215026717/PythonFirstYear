T = int(input())
c = []
for d in range(T):    
    N = int(input())
    o = []
    count = 1
    for i in range(N):
        s = int(input())
        o.append(s)
        p = max(o)
    for i in range(o.index(max(o))+1,len(o)):
        if p > o[i]:
            count += 1
            p = o[i]
    c.append(count)
for i in range(1,T+1):
    print("Case #%d: %d" %(i, c[i-1]))