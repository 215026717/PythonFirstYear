import turtle
turtle.setup(500,500) 
wn = turtle.Screen() 
lisa = turtle.Turtle()
lisa.penup()
def Screen():
    if lisa.xcor()>250 or lisa.ycor()>250 or lisa.xcor()<-250 or lisa.ycor()<-250:
        wn.title('Turtle Hopped off Screen')
    else:
        wn.title('Turtle Hop')
    return(lisa.xcor()>250 or lisa.ycor()>250 or lisa.xcor()<-250 or lisa.ycor()<-250)

def right():
    lisa.goto(lisa.xcor()+50,lisa.ycor())
    if Screen():
        lisa.goto(lisa.xcor()-50,lisa.ycor())

def up():
    lisa.goto(lisa.xcor(),lisa.ycor()+50)
    if Screen():
        lisa.goto(lisa.xcor(),lisa.ycor()-50)
    
def down():
    lisa.goto(lisa.xcor(),lisa.ycor()-50)
    if Screen():
        lisa.goto(lisa.xcor(),lisa.ycor()+50)

def left():
    lisa.goto(lisa.xcor()-50,lisa.ycor())
    if Screen():
        lisa.goto(lisa.xcor()+50,lisa.ycor())
    
wn.onkey(right,'Right')
wn.onkey(left,'Left')
wn.onkey(up,'Up')
wn.onkey(down,'Down')

wn.listen()
wn.mainloop()