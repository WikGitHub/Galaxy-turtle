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
    for i in range(5):
        mimi.forward(10)
        mimi.left(216)

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


#moon code
mimi.penup()
mimi.goto(-450, 30)
mimi.pendown()
mimi.circle(49)
mimi.penup()
mimi.goto(-350,-7)
mimi.pendown() #inner curve
mimi.circle(-34, extent=270)










#mimi.goto(-500, -500)
#mimi.pendown()
turtle.done()