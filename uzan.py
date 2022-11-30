
import turtle

wn = turtle.Screen()
ayca = turtle.Turtle()
ayca.shape("turtle")
ayca.color("blue")
wn.bgcolor("lightgreen")
for loop in range(12):
    ayca.up()
    ayca.forward(10)
    ayca.left(30)
    ayca.forward(140)
    ayca.pendown()
    ayca.forward(10)
    ayca.penup()
    ayca.forward(20)
    ayca.stamp()
    ayca.penup()
    ayca.goto(0,0)
wn.exitonclick()



