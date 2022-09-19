import turtle

# draw horizontal lines
y=-200
while y <= 300:
    turtle.penup()
    turtle.goto(-200,y)
    turtle.pendown()
    turtle.goto(300, y)
    y += 100

# draw vertical lines
x=-200
while x <= 300:
    turtle.penup()
    turtle.goto(x, -200)
    turtle.pendown()
    turtle.goto(x, 300)
    x += 100
