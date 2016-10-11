import turtle
import datetime
import math
play = False
wn = turtle.Screen()
wn.delay(0.5)
clok= turtle.Turtle()
#wid = (150/math.sin(math.radians(87))*math.sin(math.radians(6)))
wid = 15.0
sc = turtle.Turtle()
mn = turtle.Turtle()
hr = turtle.Turtle()
dot = turtle.Turtle()
sc.shape('circle')
sc.pu()
sc.shapesize(0.3)
sc.color('red')
clok.ht()
#wn.register_shape("sec", ((0,-15),(-0.5,5),(0,170),(0.5,5),(0,-15)))
wn.register_shape("min", ((1,10),(1,140),(-1,140),(-1,10),(1,10)))
wn.register_shape('hour', ((2,10),(2,90),(-2,90),(-2,10),(2,10)))
dot.pu()
dot.goto(0,-10)
dot.pensize(2)
dot.pd()
dot.circle(10)
dot.ht()

def time():
    if play:        
        wn.title('{0}:{1}:{2}'.format(datetime.datetime.now().hour,datetime.datetime.now().minute,datetime.datetime.now().second))
        sc.rt(6)
        sc.fd(wid)
        mn.seth(-(6*datetime.datetime.now().minute)+90)
        hr.seth((-(30*(datetime.datetime.now().hour+(datetime.datetime.now().minute/60)))+90))
     
    wn.ontimer(time,1000)
    
def switch(x,y):
    global play
    play = not play
    if play:
        sc.home()
        sc.seth((-(int(str(datetime.datetime.now().second))))*6+90)
        sc.fd(143.3049195697305)
        sc.seth(0)
        sc.rt(datetime.datetime.now().second*6)
    time()
    
clok.pu()
#clok.home()
for i in range(60):
    if i % 5 == 0:
        clok.pensize(2)
        clok.fd(143.3049195697305-10)
        clok.pd()
        clok.fd(10)

    else:
        clok.pensize(1)
        clok.fd(143.3049195697305-5)
        clok.pd()
        clok.fd(5)
    clok.pu()
    clok.bk(143.3049195697305)
    clok.rt(360/60)        

#sc.shape('sec')
mn.shape('min')
hr.shape('hour')
sc.st()
mn.st()
hr.st()
wn.onclick(switch)
wn.listen()
wn.mainloop()
