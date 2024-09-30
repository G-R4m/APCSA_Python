import turtle

turtle.penup()
turtle.goto(300,-300)
turtle.speed(200)

for i in range(1, 101):
    turtle.pendown()
    turtle.setheading(90)
    turtle.forward(i * 5)
    turtle.setheading(180)
    turtle.forward(i * 5)
    turtle.setheading(270)
    turtle.forward(i * 5)
    turtle.setheading(0)
    turtle.forward(i * 5)
