import math
import turtle
wn = turtle.Screen()
wn.title('Exam Prep Question 8')
wn.bgcolor('lightgreen')
t = turtle.Turtle()
t.color('black','black')

l_str = []
d = {}
t.penup()
t.goto(-270,-270)
t.pendown()
Bin = 10


def strength(pw):
    lc = 'abcdefghijklmnopqrstuvwxyz'
    uc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    ch = '!@#$%&'
    dgt = '0123456789'
    tot = 0
    for e in pw:
        if e in dgt:
            tot+=2
        elif e in lc:
            tot+=1
        elif e in uc:
            tot+=1.5
        elif e in ch:
            tot+=3
    return(tot)

def read_file():
    n = open('uni_pw.log','r')
    r = n.readlines()

    for e in r:
        l_str.append(strength(e))
    return l_str.sort()
read_file()

def Count_pw():
    n = open('uni_pw.log','r')
    r = n.read()
    freq = {}
    for i in r.split():
        freq[i] = freq.get(i,0)+1
    w = sorted(freq.keys())
    
    for j in range(len(w)):
        print(w[j],':',freq[w[j]])
    
    


def Create_Dict():
    global d
    rng = (max(l_str)-min(l_str))/Bin
    min_val = min(l_str)+rng
    max_val = max(l_str)    
    prev = min(l_str)
    print(l_str)
    for i in range(Bin):
        Sum = 0
        for j in sorted(l_str):
            if j <= min_val and j > prev:
                Sum+=1
                d[i] = Sum
            elif Sum == 0:
                d[i] = Sum
        prev = round(min_val,2)
        min_val = round((min_val+rng),2)
        print(min_val)
    d[0] = d[0] + l_str.count(min(l_str))
    return d

Create_Dict()

def graph():
    t.begin_fill()
    for i,v in sorted(d.items()):
        t.lt(90)
        t.forward(v*10)
        t.rt(90)
        t.forward(10)
        t.lt(90)
        t.backward(v*10)
        t.lt(-90)
    t.end_fill()
    
graph()
t.hideturtle()
wn.mainloop()