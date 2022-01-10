import turtle

mimi = turtle.Turtle()
mimi.speed(10)
mimi.getscreen().bgcolor('black')

mimi.penup()
mimi.goto(-300, 100)
mimi.pendown()

def star():
    mimi.color('yellow')
    mimi.fillcolor('yellow')
    mimi.begin_fill()
    for i in range(5):
        mimi.forward(10)
        mimi.left(216)
    mimi.end_fill()
    mimi.color('black')

#def constallation():
star()
mimi.color('white')
mimi.setheading(90)
mimi.forward(100)
mimi.color('black')

star()
mimi.color('white')
mimi.right(130)
mimi.forward(64)
mimi.color('black')

star()
mimi.color('white')
mimi.left(90)
mimi.forward(64)
mimi.color('black')

star()
mimi.color('white')
mimi.setheading(270)
mimi.forward(100)
mimi.color('black')
star()
mimi.penup()



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
mimi.goto(100, 100)
mimi.pendown()
star()
mimi.penup()
mimi.goto(80, -300)
mimi.pendown()
star()
mimi.penup()
mimi.goto(-600, 400)
mimi.pendown()
star()
mimi.penup()
mimi.goto(-350, -210)
mimi.pendown()
star()
mimi.penup()
mimi.goto(200, 300)
mimi.pendown()
star()
mimi.penup()
mimi.goto(500, 200)
mimi.pendown()
star()
mimi.penup()
mimi.goto(430, -400)
mimi.pendown()
star()
mimi.penup()
mimi.goto(180, -400)
mimi.pendown()
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




#mimi.goto(-500, -500)
#mimi.pendown()
turtle.done()