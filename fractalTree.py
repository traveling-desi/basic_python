### Create a fractal tree using a depth first rendering


import turtle
import random


def tree(Len, t, colors):
	if Len < 5:
		return
	t.color(colors[random.randrange(0,len(colors))])	
	t.forward(Len)
	t.right(20)
	tree(Len - 15, t ,colors)
	t.left(40)
	tree(Len - 15, t, colors)
	t.right(20)
	t.backward(Len)


def main(Len):
	myTurtle = turtle.Turtle()
	myScreen = turtle.Screen()
	myTurtle.left(90)
	myTurtle.up()
	myTurtle.backward(100)
	myTurtle.down()
	colors = ["red", "green", "blue", "black", "yellow", "orange", "brown", "purple"]
	tree(Len, myTurtle, colors)

main(75)
