import turtle

def turtle_up():
    turtle.setheading(90)
    turtle.forward(50)
    turtle.stamp()

def turtle_left():
    turtle.setheading(180)
    turtle.forward(50)
    turtle.stamp()
    
def turtle_down():
    turtle.setheading(270)
    turtle.forward(50)
    turtle.stamp()
    
def turtle_right():
    turtle.setheading(0)
    turtle.forward(50)
    turtle.stamp()

def reset():
    turtle.reset()

turtle.shape('turtle')
turtle.stamp()

turtle.onkey(turtle_up, 'w')
turtle.onkey(turtle_left, 'a')
turtle.onkey(turtle_down, 's')
turtle.onkey(turtle_right, 'd')
turtle.onkey(reset, 'Escape')
turtle.listen()
