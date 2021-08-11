import turtle
t = turtle.Turtle()
t.color("white")
t.hideturtle()
t.width(3)
def shape(t, color):
	t.color(color)
	for side in ['red', 'blue', 'green']:
		t.color(side)
		for side in range(74):
			t.forward(1)
			t.right(5)

shape(t, "red")