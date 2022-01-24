import turtle

mimi = turtle.Turtle()
mimi.speed(10)
mimi.getscreen().bgcolor('black')

mimi.penup()
mimi.goto(-300, 100)
mimi.pendown()

def star():
    mimi.pendown()
    mimi.color('yellow')
    mimi.fillcolor('yellow')
    mimi.begin_fill()
    for i in range(5):
        mimi.forward(10)
        mimi.left(216)
    mimi.end_fill()
    mimi.color('black')
    mimi.penup()


def shapes(xval, yval):
    mimi.penup()
    #quadrant 1 (+,+)
    for i in range(0,11):
        xFrom = 0 + xval
        yFrom =((10-i) * 1.50) +yval
        xTo = (i * 1.50)+ xval
        yTo = 0 +yval
        mimi.goto(xFrom,yFrom)
        mimi.pendown()
        mimi.goto(xTo,yTo)
        mimi.penup()

    for i in range(0,11):
        xFrom = 0 + xval
        yFrom = -((10-i) * 1.5) +yval
        xTo = (i * 1.5 )+ xval
        yTo = -0 +yval
        mimi.goto(xFrom,yFrom)
        mimi.pendown()
        mimi.goto(xTo,yTo)
        mimi.penup()

    for i in range(0,11):
        xFrom = -0 + xval
        yFrom =-((10-i) * 1.50) +yval
        xTo = -(i * 1.50)+ xval
        yTo = -0 +yval
        mimi.goto(xFrom,yFrom)
        mimi.pendown()
        mimi.goto(xTo,yTo)
        mimi.penup()

    for i in range(0,11):
        xFrom = - 0 + xval
        yFrom =  ((10-i) * 1.5) +yval
        xTo = - (i * 1.5 )+ xval
        yTo =  0 +yval
        mimi.goto(xFrom,yFrom)
        mimi.pendown()
        mimi.goto(xTo,yTo)
        mimi.penup()

#def constallation():
star()
mimi.pendown()
mimi.color('white')
mimi.setheading(90)
mimi.forward(100)
mimi.color('black')

star()
mimi.pendown()
mimi.color('white')
mimi.right(130)
mimi.forward(64)
mimi.color('black')

star()
mimi.pendown()
mimi.color('white')
mimi.left(90)
mimi.forward(64)
mimi.color('black')

star()
mimi.pendown()
mimi.color('white')
mimi.setheading(270)
mimi.forward(100)
mimi.color('black')
star()
#end of constellation


#code for planet 
mimi.fillcolor('purple')
mimi.begin_fill()
mimi.goto(400, -200)
mimi.pendown()
mimi.circle(80)
mimi.end_fill()
mimi.penup()
mimi.left(95)
mimi.forward(10)
mimi.left(40)
mimi.forward(10)
mimi.left(40)
mimi.forward(10)
mimi.penup()
mimi.goto(549, -160)
mimi.color('yellow')
mimi.pendown()
mimi.circle(80, extent= -141)
mimi.color('black')
mimi.penup()

#code for little stars

mimi.color("white")
shapes(100, 100)

mimi.pendown()
shapes(80, -300)

mimi.goto(-600, 400)
mimi.color("yellow")
star()
mimi.goto(-350, -210)
star()
mimi.goto(200, 300)
star()
mimi.goto(500, 200)
star()
mimi.goto(430, -400)
star()
mimi.goto(180, -400)
star()


#moon code
mimi.penup()
mimi.goto(-450, 30)
mimi.pendown()
mimi.fillcolor('white')
mimi.begin_fill()
mimi.circle(49)
mimi.end_fill()
mimi.penup()
mimi.goto(-360,83)
#mimi.color('white')
mimi.pendown() #inner curve
mimi.fillcolor('black')
mimi.begin_fill()
mimi.circle(-43, extent=360)
mimi.end_fill()

#rocket
screen = turtle.Screen()
screen.tracer(0)
#screen.addshape("Vp3M.gif")   

mimi = turtle.Turtle()
mimi.speed(0)
#mimi.shape("Vp3M.gif")         

mimi.penup()
mimi.goto(-350, 0)


for i in range(50):
    if i <40 :
        screen.update()
        mimi.forward(5)
    else:
        screen.update
        mimi.backward(5)
        i+=1






#mimi.goto(-500, -500)
#mimi.pendown()
turtle.done()