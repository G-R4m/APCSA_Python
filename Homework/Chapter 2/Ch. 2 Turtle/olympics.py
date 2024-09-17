import turtle

turtle.pensize(5)

turtle.pencolor('black')
turtle.circle(40)
turtle.penup()

turtle.pencolor('red')
turtle.forward(100)
turtle.pendown()
turtle.circle(40)
turtle.penup()

turtle.pencolor('blue')
turtle.setheading(180)
turtle.forward(200)
turtle.pendown()
turtle.setheading(0)
turtle.circle(40)
turtle.penup()

turtle.pencolor('yellow')
turtle.forward(50)
turtle.setheading(270)
turtle.forward(35)
turtle.setheading(0)
turtle.pendown()
turtle.circle(40)
turtle.penup()

turtle.pencolor('green')
turtle.forward(100)
turtle.pendown()
turtle.circle(40)

turtle.hideturtle()