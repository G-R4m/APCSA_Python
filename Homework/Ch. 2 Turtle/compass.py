import turtle
turtle.forward(100)
turtle.penup()
turtle.forward(5)
turtle.setheading(270)
turtle.forward(5)
turtle.write('East')
turtle.setheading(90)
turtle.forward(5)
turtle.setheading(180)
turtle.forward(5)
turtle.pendown()

turtle.forward(200)
turtle.penup()
turtle.forward(20)
turtle.setheading(270)
turtle.forward(5)
turtle.write('West')
turtle.setheading(90)
turtle.forward(5)
turtle.setheading(0)
turtle.forward(20)
turtle.pendown()

turtle.forward(100)
turtle.setheading(270)
turtle.forward(100)
turtle.penup()
turtle.forward(12)
turtle.setheading(180)
turtle.forward(8)
turtle.write('South')
turtle.setheading(0)
turtle.forward(8)
turtle.setheading(90)
turtle.forward(12)
turtle.pendown()

turtle.forward(200)
turtle.penup()
turtle.forward(3)
turtle.setheading(180)
turtle.forward(8)
turtle.write('North')
turtle.setheading(0)
turtle.forward(8)
turtle.setheading(270)
turtle.forward(3)
turtle.pendown()
turtle.forward(100)

turtle.setheading(180)
turtle.forward(25)
turtle.setheading(270)
turtle.circle(25)


turtle.hideturtle()

input('press any key to exit')