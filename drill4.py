import turtle

cnt = 6
x = 0
y = 0

while cnt > 0:
    y = y + 100
    turtle.forward(500)
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    cnt = cnt - 1

turtle.penup()
turtle.home()
turtle.pendown()
turtle.left(90)

cnt = 6
x = 0
y = 0

while cnt > 0:
    x = x + 100
    turtle.forward(500)
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    cnt = cnt - 1
    


