def areRelativePrimes(a,b):
    oa = []
    ob = []
    if a >= b:
        for i in range(2,a):
            if a % i == 0:
                while a == a:
                    if (a / i) != int(a/i):
                        break
                    a /= i
                    oa.append(i)
            if b % i == 0:
                while b == b:
                    if (b / i) != int(b/i):
                        break
                    b /= i
                    ob.append(i)            
    elif b >= a:
        for i in range(2,b):
                if b % i == 0:
                    while b == b:
                        if (b / i) != int(b/i):
                            break
                        b /= i
                        oa.append(i)
                if a % i == 0:
                    while a == a:
                        if (a / i) != int(a/i):
                            break
                        a /= i
                        ob.append(i)      
    if len(oa) >= len(ob):
        for i in range(len(ob)):
            for s in range(len(oa)):
                if ob[i] == oa[s]:
                    return False
        return True
    else:
        for i in range(len(oa)):
            for s in range(len(ob)):
                if oa[i] == ob[s]:
                    return False
        return True
            

a = int(input())
b = int(input())

print(areRelativePrimes(a,b))