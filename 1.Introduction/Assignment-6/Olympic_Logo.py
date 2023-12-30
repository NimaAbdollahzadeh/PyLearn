import turtle

turtle.title("Nima's very first turtle program!")
Screen = turtle.Screen()
t = turtle.Turtle()
t.pensize(10)
t.speed(5)

t.color("blue")
t.penup()
t.goto(-110, -25)
t.pendown()
t.circle(60)

t.color("black")
t.penup()
t.goto(0, -25)
t.pendown()
t.circle(60)
 
t.color("red")
t.penup()
t.goto(110, -25)
t.pendown()
t.circle(60)
 
t.color("yellow")
t.penup()
t.goto(-55, -75)
t.pendown()
t.circle(60)
 
t.color("green")
t.penup()
t.goto(55, -75)
t.pendown()
t.circle(60)

Screen.exitonclick()