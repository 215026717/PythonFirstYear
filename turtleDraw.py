__author__ = 'mandla'
import turtle                               #import the python module turtle
def loadCodes(d):                           #defines a function (loadCodes)
    d[0]='black'
    d[1]='darkblue'
    d[2]='lightblue'
    d[3]='khaki'
    d[4]='greenyellow'
    d[5]='white'

wn=turtle.Screen()                          #executes a module that allows the turtle to be displayed in th screen
wn.bgcolor('pink')                          #makes the background colour pink 
alex=turtle.Turtle()                        #gives the turtle a name (alex)
alex.shape('turtle')                        #makes the turtle take the shap of an actual turtle
alex.speed(10)                              #makes the move faster
alex.pensize(4)                             #makes the pen thicker
scan = open('scalenum.txt','r')             #accesses a file
lines=scan.readlines()                      #puts the values of the file in a list

d={}                                        #makes d an empty dictionary
loadCodes(d)                                #calls the function (loadCodes) with the dictionary (d) as its parameter

alex.right(90)
for line in lines:                          #for loop
    tokens=line.split()                     #puts all the numbers in the string (line) in a list (tokens)
    for token in tokens:                    #for loop
        num= int(token)                     #converts the value of the string (token) to a integer
        alex.color(d[num])                  #changes the colour depending on the value of the num, which accesses the dictionary (d)
        alex.forward(4)                     #the turtle (alex) moves one forward 
    alex.penup()                            #the turtle can move but won't write/draw anything
    alex.goto(alex.xcor()-4,0)              #the turtle move from its current destination to where it was horizontally (0) and moves it one down vertically (alex.ycor()-1)
    alex.pendown()                          #the turtle can write/draw again

alex.hideturtle()                           #makes the turtle disappear when it is done
wn.exitonclick()                            #allows the use to close the window