import turtle

wn = turtle.Screen()
turtle.bgcolor("red")
t = turtle.Turtle()
t.pensize(4)

t.right(90)
t.forward(40)
t.left(45)
t.forward(10)
t.right(90)
t.forward(40)
t.left(45)
t.forward(120)

t.penup()
t.left(90)
t.forward(40)
t.left(90)
t.forward(190)
t.pendown()

t.right(180)
t.forward(40)
t.left(45)
t.forward(10)
t.right(90)
t.forward(40)
t.left(45)
t.forward(110)

t.penup()
t.left(90)
t.forward(90)
t.left(90)
t.forward(140)
t.pendown()

t.fillcolor("black")
t.begin_fill()

t.circle(25)

t.end_fill()

t.penup()
t.left(180)
t.forward(25)
t.right(90)
t.forward(25)
t.pendown()

t.right(30)

t.fillcolor("black")
t.begin_fill()

for i in range(6):
    t.left(60)
    t.forward(60)

t.end_fill()

t.penup()
t.right(150)
t.forward(45)
t.left(90)
t.forward(65)
t.pendown()

t.right(180)
t.forward(40)
t.right(45)
t.forward(10)
t.left(90)
t.forward(40)
t.right(45)
t.forward(120)

t.penup()
t.left(180)
t.forward(200)
t.pendown()

t.right(180)
t.forward(40)
t.right(45)
t.forward(10)
t.left(90)
t.forward(40)
t.right(45)
t.forward(120)

turtle.done()