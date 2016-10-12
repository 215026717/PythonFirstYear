import turtle
import random
import math
c = 0
s = open('settings.dat','r')
p = s.readlines()
wn = turtle.Screen() 
lisa = turtle.Turtle()
lisa.penup()
wn.bgcolor('lightgreen')
for (i,v) in enumerate(p):
    v = v.replace('\t',' ')
    v = v.replace('\n',' ')
    p[i] = v.split(' ')

p[0][0]=int(p[0][0])
p[0][1]=int(p[0][1])
turtle.setup(p[0][0],p[0][1]) 

def obstacleAvoid(x,y):
    return (p[1][0]<(lisa.xcor()+x)<p[1][2] and p[1][3]<(lisa.ycor()+y)<p[1][1]) or (p[2][0]<(lisa.xcor()+x)<p[2][2] and p[2][3]<(lisa.ycor()+y)<p[2][1]) or (p[3][0]<(lisa.xcor()+x)<p[3][2] and p[3][3]<(lisa.ycor()+y)<p[3][1]) or (p[4][0]<(lisa.xcor()+x)<p[4][2] and p[4][3]<(lisa.ycor()+y)<p[4][1])

def obstacle():
    for (i,v) in enumerate(p[1:]):
        for d,c in enumerate(v[:4]):
            v[d] = int(c)
        lisa.goto(v[0],v[1])
        lisa.pendown()
        lisa.begin_fill()
        lisa.goto(v[2],v[1])
        lisa.goto(v[2],v[3])
        lisa.goto(v[0],v[3])
        lisa.goto(v[0],v[1])
        lisa.end_fill()
        lisa.penup()
    
def randomnum():
    return(random.randint(0,1))
    

pause = False
def space():
        global pause
        pause = not pause
        movement()
            

def movement():
    global c
    global pause
    if (not pause):
        num1 = randomnum()
        a = random.randint(0,180)
        if num1 == 1:
            c = lisa.heading() - a
            #lisa.right(a)
        else:
            c = lisa.heading() + a
            #lisa.left(a)
        b = c *(math.pi/180)
        x = math.cos(b) * 50
        y = math.sin(b) * 50
        if lisa.xcor()+x>(p[0][0]/2) or lisa.ycor()+y>(p[0][1]/2) or lisa.xcor()+x<-(p[0][0]/2) or lisa.ycor()+y<-(p[0][1]/2):
            wn.title('{0},{1}'.format(lisa.xcor()+x,lisa.ycor()+y))
            
        elif obstacleAvoid(x,y):
            wn.title('{0},{1} angle'.format(c,a))
        else:
            if num1 == 1:
                lisa.right(a)
            else:
                lisa.left(a)                               
            lisa.fd(50)
            wn.title('{0},{1} angle'.format(c,a))
            
        wn.ontimer(movement,100)

obstacle()
lisa.goto(p[3][0],p[3][1])
lisa.shape('turtle')
lisa.color('purple')
movement()
wn.onkey(space,'space')


wn.listen()
wn.mainloop()