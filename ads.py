import turtle

deniz = turtle.Turtle()
wn = turtle.Screen()
colors = ["blue", "red", "yellow", "green", "orange", "purple", "black", "brown", "blue", "red", "yellow", "green",
          "orange", "purple", "black", "brown", "blue", "red", "yellow", "green", "orange", "purple", "black", "brown",
          "blue", "red", "yellow", "green", "orange", "purple", "black", "brown", "blue", "red", "yellow", "green",
          "orange", "purple", "black", "brown", "blue", "red", "yellow", "green", "orange", "purple", "black", "brown",
          "blue", "red", "yellow", "green", "orange", "purple", "black", "brown", "blue", "red", "yellow", "green",
          "orange", "purple", "black", "brown", "blue", "red", "yellow", "green", "orange", "purple", "black", "brown",
          "blue", "red", "yellow", "green", "orange", "purple", "black", "brown", "blue", "red", "yellow", "green",
          "orange", "purple", "black", "brown", "blue", "red", "yellow", "green", "orange", "purple", "black", "brown",
          "blue", "red", "yellow", "green", "orange", "purple", "black", "brown", "blue", "red", "yellow", "green",
          "orange", "purple", "black", "brown", "blue", "red", "yellow", "green", "orange", "purple", "black", "brown",
          "blue", "red", "yellow", "green", "orange", "purple", "black", "brown", "blue", "red", "yellow", "green",
          "orange", "purple", "black", "brown", "blue", "red", "yellow", "green", "orange", "purple", "black", "brown",
          "blue", "red", "yellow", "green", "orange", "purple", "black", "brown", "blue", "red", "yellow", "green",
          "orange", "purple", "black", "brown", "blue", "red", "yellow", "green", "orange", "purple", "black", "brown",
          "blue", "red", "yellow", "green", "orange", "purple", "black", "brown", "blue", "red", "yellow", "green",
          "orange", "purple", "black", "brown", "blue", "red", "yellow", "green", "orange", "purple", "black", "brown",
          "blue", "red", "yellow", "green", "orange", "purple", "black", "brown", "blue", "red", "yellow", "green",
          "orange", "purple", "black", "brown", "blue", "red", "yellow", "green", "orange", "purple", "black", "brown",
          "blue", "red", "yellow", "green", "orange", "purple", "black", "brown", "blue", "red", "yellow", "green",
          "orange", "purple", "black", "brown", "blue", "red", "yellow", "green", "orange", "purple", "black", "brown",
          "blue", "red", "yellow", "green", "orange", "purple", "black", "brown", "blue", "red", "yellow", "green",
          "orange", "purple", "black", "brown", "blue", "red", "yellow", "green", "orange", "purple", "black", "brown",
          "blue", "red", "yellow", "green", "orange", "purple", "black", "brown", "blue", "red", "yellow", "green",
          "orange", "purple", "black", "brown", "blue", "red", "yellow", "green", "orange", "purple", "black", "brown",
          "blue", "red", "yellow", "green", "orange", "purple", "black", "brown", "blue", "red", "yellow", "green",
          "orange", "purple", "black", "brown", "blue", "red", "yellow", "green", "orange", "purple", "black", "brown",
          "blue", "red", "yellow", "green", "orange", "purple", "black", "brown"]
for i in range(200):
    deniz.pensize(i / 2)
    deniz.up()
    deniz.forward(i / 42)
    deniz.left(3)
    deniz.pendown()
    deniz.forward(1)
    wn.bgcolor(colors[i + 2])
    deniz.color(colors[i])

wn.exitonclick()
