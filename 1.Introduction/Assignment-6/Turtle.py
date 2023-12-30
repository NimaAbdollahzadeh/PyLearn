import turtle
import math

turtle.title("Polygan")
Screen = turtle.Screen()
t = turtle.Turtle()
t.pensize(1)
t.speed(2)
t.color("black")
t.screen.bgcolor("white")
t.shape("turtle")

r0 = 20
t.lt(150)
for i in range(3, 13):
    points = [
        (r0 * (i-1) * math.cos(k*2*math.pi/i),
        r0 * (i-1) * math.sin(k*2*math.pi/i))
        for k in range(1, i+1)
    ]

    t.penup()
    t.goto(*points[-1])
    t.pendown()
    for tx, ty in points:
        t.goto(tx, ty)

Screen.exitonclick()