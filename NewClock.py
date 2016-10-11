import turtle
import datetime
play = False
wn = turtle.Screen()
wn.delay(0.5)
clok= turtle.Turtle()
sc = turtle.Turtle()
mn = turtle.Turtle()
hr = turtle.Turtle()
dot = turtle.Turtle()
#clok.ht()
wn.register_shape("sec", ((0,-15),(-0.5,5),(0,170),(0.5,5),(0,-15)))
wn.register_shape("min", ((0,0),(-1.5,5),(0,170),(1.5,5),(0,0)))
wn.register_shape('hour', ((0,0),(-1.5,5),(0,100),(1.5,5),(0,0)))
dot.shape('circle')
dot.shapesize(0.2)

def time():
    if play:        
        wn.title('{0}:{1}:{2}'.format(datetime.datetime.now().hour,datetime.datetime.now().minute,datetime.datetime.now().second))
        sc.seth((-(float(str(datetime.datetime.now().time())[6:])))*6+90)
        mn.seth((-(6*datetime.datetime.now().minute+(datetime.datetime.now().second/10)))+90)
        hr.seth((-(30*(datetime.datetime.now().hour+(datetime.datetime.now().minute/60)))+90))
     
    wn.ontimer(time,10)
    
def switch(x,y):
    global play
    play = not play
    time()
    
clok.pu()
clok.right(90)
clok.fd(200)
clok.left(90)
clok.pd()
clok.circle(200)
clok.pu()
clok.home()
for i in range(60):
    if i == (3*5) or i == 9*5:
        if i == 3*5:
            clok.fd(195)                    
            clok.write(6,False,'center',('Arial',30,'normal'))
            clok.bk(195)
            clok.rt(360/60) 
        else:
            clok.fd(165)            
            clok.write(12,False,'center',('Arial',30,'normal'))
            clok.bk(165)
            clok.rt(360/60)
            
    elif i%5 == 0:
        clok.fd(150)
        clok.pd()
        clok.fd(30)
        clok.pu()
        clok.bk(180)
        clok.rt(360/60) 
    else:
        clok.fd(175)
        clok.pd()
        clok.fd(5)
        clok.pu()
        clok.bk(180)
        clok.rt(360/60) 

sc.shape('sec')
mn.shape('min')
hr.shape('hour')  
sc.st()
mn.st()
hr.st()
wn.onclick(switch)
wn.listen()
wn.mainloop()