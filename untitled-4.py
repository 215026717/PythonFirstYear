import turtle
alex = turtle.Turtle()
wn = turtle.Screen()
s = open('uni_pw.log','r')
strengths = []
d = {}

def func(lis,num):
    for i,v in enumerate (lis):
        if v > num:
            return (i)
    if num >= max(lis):
        return (i+1)

def graph(n):
    alex.left(90)
    alex.fd(n*10)
    alex.right(90)
    alex.fd(10)
    alex.right(90)
    alex.fd(n*10)
    alex.left(90)

def Strength(p):
    score = 0
    p = str(p)
    for i in p:
        if i not in p:
            continue        
        if p.count(i) > 1:
            for g,k in enumerate(i*p.count(i)):
                if i in '!@#$%&':
                    score += 3*2**(1-(g+1))
                elif i.isupper():
                    score += 1.5*2**(1-(g+1))
                elif i.islower():
                    score += 1*2**(1-(g+1))
                else:
                    score += 2*2**(1-(g+1)) 
            p = p.replace(i,'')
        elif i in '!@#$%&':
            score += 3        
        elif i.isupper():
            score += 1.5
        elif i.islower():
            score += 1
        else:
            score += 2
        
    return (score*len(p))

for i in s.readlines():
    i = i.replace('\n','')
    strengths.append(Strength(i))

rang = max(strengths) - min(strengths)
binsiz = rang / 10
binnum = min(strengths)
strengths.sort()
tot = 0
pnew = 0

for i in range(10):
    binnum = round(binnum + binsiz,3)
    new = func(strengths,binnum)
    d[i] = (new-pnew)
    pnew = new
    
for i in range(10):
    graph(d[i]) 

wn.mainloop()