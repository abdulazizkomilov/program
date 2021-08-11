# satr = input('So`z kiriting: ')
# for s in satr:
#	if s.isdigit():
#		print('sinish nuqtasi:', s)
#		break
#		continue
#	print(s)

from turtle import Turtle, Screen
oyna = Screen()
oyna.title('Mening oynam')

chiziq = Turtle()
chiziq.color('red')
chiziq.hideturtle()
chiziq.speed(0)
chiziq.pensize(5)
chiziq.up()
chiziq.goto(200, 200)
chiziq.down()
chiziq.goto(200, -200)
chiziq.goto(-200, -200)
chiziq.goto(-200, 200)
chiziq.goto(200, 200)

koptok = Turtle()
koptok.color('blue')
koptok.shape('circle')
koptok.shapesize(1)
koptok.up()
koptok.goto(0, 0)

stepx = 3
stepy = 2
while True:
	x, y = koptok.position()
	if x + stepx >= 200 or x + stepx <= -200:
		stepx = -stepx
	if y + stepy >= 200 or y + stepy <= -200:
		stepy = -stepy

	koptok.goto(x + stepx, y + stepy) 
oyna.mainloop()