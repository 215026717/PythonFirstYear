# Writing pascals triangle
n = int(input())
print(end=' '*(n-1))
print(1)
if n > 1:
    print(end=' '*(n-2))
    print(1, 1)
    o = [1,1]
for i in range(n-2):
    new = [1]
    for d in range(len(o)-1):
        new.append((o[d]+o[d+1]))
    new.append(1)
    o = new
    print(end=(' '*(n-(3+i))))
    print(1,end=' ')
    for d in range(1,len(o)):
        if d == (len(o)-1):
            print(o[d])
        else:
            print(o[d],end=' ')
