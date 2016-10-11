def order(lis):
    of = [lis[0]]
    test = []
    lar = 0
    for i,v in enumerate(lis):
        if of.count(v) > 1 and min(of) > v:
            for x in range(of.count(v)):
                test.append(order(lis[(lis.index(v,x)):]))
            for x,t in enumerate(test):
                if len(t) > lar:
                    lar = len(t)
                    s = x
            of.extend(test[s])
            #print(test,"a")
        if min(of) > v:
            of.append(v)
    return of
    
T = int(input())
c = []
for d in range(T):  
    max1 = 0
    df = []    
    N = int(input())
    o = []
    count = 1
    for i in range(N):
        s = int(input())
        o.append(s)
        p = max(o)
    df.append([o[0]])
    for i,v in enumerate (o):
        if o.count(v) > 1 and min(df[0]) > v:
            for x in range(o.count(v)):
                df.append(order(o[(o.index(v,x))-1:]))
            break
        if df < [[v]]:
            df.append(order(o[i:]))
        elif min(df[0]) > v:
            df[0].append(v)
    for i in df:
        if len(i) > max1:
            max1 = len(i)
    #print(df)
    c.append(max1)
for i in range(1,T+1):
    print("Case #%d: %d" %(i, c[i-1]))