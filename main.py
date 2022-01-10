import turtle

mimi = turtle.Turtle()
mimi.speed(10)
mimi.penup()
mimi.goto((-300, 100))
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







#mimi.goto(-500, -500)
#mimi.pendown()











turtle.done()