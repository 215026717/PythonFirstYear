B = int(input(""))
o = []
for x in range(1,B+1):
    C = int(input(""))
    T = int(input(""))
    N = 0
    bal = []
    for i in range(T):
        dep_with = int(input(""))
        if dep_with < 0 and C + dep_with < 0:
            bal.append(dep_with)
            continue
        C += dep_with
        N += 1
        print(bal)
    for i in range(len(bal)):
        if C + max(bal) < 0:
            break
        C += max(bal)
        bal.remove(max(bal))
        N+=1
    o.append(N)
    o.append(C)
m = -2
k = -1
for i in range(B):
    m += 2
    k += 2
    print("Case #%d: %d %d"%(i+1,o[m],o[k]))