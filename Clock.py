import turtle
import datetime
wn = turtle.Screen()
clok= turtle.Turtle()
clok.ht()
wn.register_shape("sec", ((0,0),(0,100), (-5,100), (0,105), (5,100),(0,100)))
wn.register_shape("min", ((0,0),(0,60), (-3,60), (0,63), (3,60),(0,60)))
wn.register_shape('hour', ((0,0),(0,30), (-3,30), (0,33), (3,30),(0,30)))
sc = turtle.Turtle()
mn = turtle.Turtle()
hr = turtle.Turtle()
sc.ht()
mn.ht()
hr.ht()
def time():
    wn.title('{0}:{1}:{2}'.format(datetime.datetime.now().hour,datetime.datetime.now().minute,datetime.datetime.now().second))
    wn.ontimer(time,1000)
    
def hands():

    
    sc.shape('sec')
    mn.shape('min')
    hr.shape('hour')
    
    sc.penup()
    mn.penup()
    hr.pu()
    
    
    sc.left(90)
    mn.left(90)
    hr.left(90)
    sc.rt(6*datetime.datetime.now().second)
    mn.rt(6*datetime.datetime.now().minute)
    hr.rt(30*datetime.datetime.now().hour)
    
    sc.st()
    mn.st()
    hr.st()

def sec_movement():
    sc.rt(6)
    wn.ontimer(sec_movement,1000)

def min_movement():
    mn.rt(6)
    wn.ontimer(min_movement,(60000))
def hr_movement():
    hr.rt(6)
    wn.ontimer(hr_movement,720000)

def clock():
    clok.ht()
    clok.pu()
    clok.right(90)
    clok.fd(200)
    clok.left(90)
    clok.pd()
    clok.circle(200)
    clok.pu()
    clok.home()
    for i in range(12):
        clok.fd(150)
        clok.pd()
        clok.fd(30)
        clok.pu()
        clok.fd(20)
        clok.bk(200)
        clok.right(360/12)
   
clock()    
hands()
sec_movement()
min_movement()
hr_movement()
time()

wn.mainloop()