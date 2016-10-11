import math
def simil(i, l):
    a = dic[i][0] / dic[l][0]
    if a > 1:
        a = a ** (-1)
    b = dic[i][1] / dic[l][1]
    if b > 1:
        b = b ** (-1)    
    c = dic[i][2] / dic[l][2]
    if c > 1:
        c = c ** (-1)
    p = dic[i][3] / dic[l][3]
    if p > 1:
        p = p ** (-1)
    e = dic[i][4] / dic[l][4]
    if e > 1:
        e = e ** (-1)
    q = dic[i][5] / dic[l][5]
    if q > 1:
        q = q ** (-1)  
    f = dic[i][6] / dic[l][6]
    if f > 1:
        f = f ** (-1)   
    g = a + b + c + p + e + f + q
    return g
    

W = int(input())
N = int(input())
c = 0
o = []
for b in range(1,W+1):
    highest = 0    
    rang = []  
    dic = {} 
    for i in range(1,N+1):
        shop = input()
        rang.append((shop[4]))
        dic[shop[4]] = []
        for s in range(6,len(shop)):
            if shop[s] == ' ':
                dic[shop[4]].append(c)
                c = 0
            elif type(int(shop[s])) == int:
                c = c * 10 + int(shop[s])
        dic[shop[4]].append(c)
        c = 0
    
    fac = (math.factorial(len(rang))) / (2*math.factorial(len(rang) - 2))
    i = N-1    
    l = i
    for x in range(int(fac)):
        l = l - 1
        sim = simil((rang[i]), (rang[l]))
        if sim > highest:
            highest = sim
            z = int(rang[i])
            v = int(rang[l])
        if l == 0:
            i -= 1
            l = i
    o.append(v)
    o.append(z)
    o.sort()
a = -2
b = -1
for m in range(W):
    a += 2
    b += 2
    print("Case #%d: Shop%d Shop%d" %(m+1,o[a],o[b]))