def getMode(d):
    mv = 0
    mk = 0
    for k in d:
        if d[k] > mv:
            mk = k
            mv = d[k]
    return mk

file = open('num.txt','r')
lines = file.readlines()
d = {}
for line in lines:
    n = int(line)
    d[n] = d.get(n,0)+1
print('The mode is {0}'.format(getMode(d)))

s = 'ThiS is String with Upper and lower case Letters'
d = {}
for c in s:
    c.lower