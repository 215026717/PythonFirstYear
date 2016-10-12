import turtle
import random
s = open('settings.dat','r')
p = s.readlines()
wn = turtle.Screen() 
lisa = turtle.Turtle()
lisa.penup()
l = []
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
        lisa.goto(v[2],v[1])
        lisa.goto(v[2],v[3])
        lisa.goto(v[0],v[3])
        lisa.goto(v[0],v[1])
        '''for i in range(2):
            lisa.fd(v[2]-v[0])
            wn.title('{0},{1}'.format(lisa.xcor(),lisa.ycor()))
            lisa.right(90)
            lisa.fd(v[3]-v[1])
            wn.title('{0},{1}'.format(lisa.xcor(),lisa.ycor()))
            lisa.right(90)'''
        lisa.penup()
        
    
def randomnum():
    a = random.randint(0,2)
    if a == 0:
        return -50
    elif a == 1:
        return(0)
    else:
        return 50

pause = False
def space():
        global pause
        pause = not pause
        movement()
            

def movement():
    
    global pause
    if (not pause):
        x = randomnum()
        y = randomnum()
        
        if lisa.xcor()+x>(p[0][0]/2) or lisa.ycor()+y>(p[0][1]/2) or lisa.xcor()+x<-(p[0][0]/2) or lisa.ycor()+y<-(p[0][1]/2):
            wn.title('Turtle Hop')

        elif obstacleAvoid(x,y):
            wn.title('{0},{1}'.format(lisa.xcor()+x,lisa.ycor()+y))
        
        else:
            lisa.goto(lisa.xcor()+x,lisa.ycor()+y)
            wn.title('Turtle Hop')
            
        wn.ontimer(movement,500)

obstacle()
print(p)
movement()
wn.onkey(space,'space')


wn.listen()
wn.mainloop()