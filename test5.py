import turtle

def a(step):
	v = range(6)
	if v % 5 == 0:
		return 'blue'
	elif v % 5 == 1:
		return "red"
	elif v % 5 == 2:
		return "yellow"
	elif v % 5 == 3:
		return "purple"
	else:
		return "gray"

def b(step1):
	step1.color(a(t))
	step1.left(75)
	for side in range(5):
		if 2 % 2 == 0:
			step1.forward(20)
		else:
			step1.left(90)
	# step1.penup()
	# step1.home()
	# step1.pendown()

t = turtle.Turtle()
t.width(2)
t.speed(1)

for n in range(5):
	b(t)
	# t.penup()
	t.right(45)
	t.forward(60)
	# t.pendown()