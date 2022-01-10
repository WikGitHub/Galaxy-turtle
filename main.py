import turtle

mimi = turtle.Turtle()
mimi.speed(10)

mimi.penup()
mimi.goto(-300, 100)
mimi.pendown()

# add colour
#def constellation(turtle, size):
#    if size <= 10:
        #return
    #else:
        #turtle.begin_fill()
        #for i in range(5):
         #   turtle.forward(size)
          #  constellation(turtle, size/3)
           # turtle.left(216)
        #turtle.end_fill()
#constellation(mimi, 360)

def star():
    mimi.fillcolor('yellow')
    mimi.begin_fill()
    for i in range(5):
        mimi.forward(10)
        mimi.left(216)
    mimi.end_fill()

#def constallation():
star()
mimi.setheading(90)
mimi.forward(100)

star()
mimi.right(130)
mimi.forward(64)

star()
mimi.left(90)
mimi.forward(64)

star()
mimi.setheading(270)
mimi.forward(100)
star()
mimi.penup()



#code for planet 
mimi.goto(400, -200)
mimi.pendown()
mimi.circle(80)
mimi.penup()

mimi.left(95)
mimi.forward(10)
mimi.left(40)
mimi.forward(10)
mimi.left(40)
mimi.forward(10)
mimi.penup()
mimi.goto(547, -242)
mimi.pendown()
mimi.circle(80, extent= 160)
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
mimi.goto(-350,-7)
mimi.pendown() #inner curve
mimi.fillcolor('black')
mimi.begin_fill()
mimi.circle(-34, extent=270)
mimi.end_fill()




#mimi.goto(-500, -500)
#mimi.pendown()
turtle.done()