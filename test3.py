import turtle

def shape(num):
	if num % 3 == 0:
		return "red"
	elif num % 3 == 1:
		return "green"
	else:
		return "blue"

def bead(tur):
	tur.right(75)
	for side in range(12):
		tur.forward(10)
		tur.left(30)
	tur.left(75)

t = turtle.Turtle()
t.width(2)

t.penup()
t.back(150)
t.pendown()

for n in range(10):
	t.color(shape(n))
	bead(t)
	t.forward(40)