# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# Import turtle package
import turtle

# Creating a turtle object(pen)
pen = turtle.Turtle()

# Defining a method to draw curve
def curve():
	for i in range(200):

		# Defining step by step curve motion
		pen.right(1)
		pen.forward(1)

# Defining method to draw a full heart
def heart():

	# Set the fill color to red
	pen.fillcolor('red')

	# Start filling the color
	pen.begin_fill()

	# Draw the left line
	pen.left(140)
	pen.forward(113)

	# Draw the left curve
	curve()
	pen.left(120)

	# Draw the right curve
	curve()

	# Draw the right line
	pen.forward(112)

	# Ending the filling of the color
	pen.end_fill()

# Defining method to write text
def txt():

	pen.up()
	pen.setpos(-68, 95)
	pen.down()
	pen.color('lightgreen')
	pen.write("İSA_<3_GÜLÇİN", font=(
	"Verdana", 12, "bold"))

heart()
txt()
pen.ht()
turtle.exitonclick()