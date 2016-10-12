n = open('num.txt','r')
t = []
for i in n.readlines():
    b = int(i)
    t.append(b)
range1 = (max(t) - min(t))/ 5
a = min(t)
print("{0}{1:>15}".format('Old number range','New value'))
for i in range(5):
    print("[{0:.5} - {1:.5}){2:>15}".format(a,a+range1,i+1))
    a += range1