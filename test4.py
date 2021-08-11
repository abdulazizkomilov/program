import turtle

def a(step):
	if step % 3 == 0:
		return "purple"
	elif step % 3 == 1:
		return "gray"
	else:
		return "pink"

def b(step1):
	step1.right(75)
	for side in range(12):
		step1.forward(5)
		step1.left(30)
	step1.left(40)

t = turtle.Turtle()
t.width(3)
t.speed(1)

t.penup()
t.back(200)
t.pendown()

for s in range(10):
	t.color(a(s))
	b(t)
	t.penup()
	t.forward(20)
	t.pendown()