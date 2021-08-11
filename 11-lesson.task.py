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

blok = Turtle()
blok.color('green')
blok.hideturtle()
blok.speed(0)
blok.pensize(4)
blok.up()
blok.goto(-170, -170)
blok.down()
blok.goto(-100, -170)
blok.goto(-100, -195)
blok.goto(-170, -195)
blok.goto(-170, -170)

koptok = Turtle()
koptok.color('blue')
koptok.shape('circle')
koptok.shapesize(1)
koptok.up()
koptok.goto(0, 0)

stepx = 5
stepy = 4
while True:
	x, y = koptok.position()
	if x + stepx >= 200 or x + stepx <= -200:
		stepx = -stepx
	if y + stepy >= 200 or y + stepy <= -200:
		stepy = -stepy
	if x + stepx <= -100 and y == -170:
		break
	if x + stepy <= -100 and -170 > y > -195:
		break

	koptok.goto(x + stepx, y + stepy)

# koptok = Turtle()
# koptok.color('blue')
# koptok.shape('circle')
# koptok.shapesize(1)
# koptok.up()
# koptok.goto(2, -2)

# stepx = 4
# stepy = 3
# while True:
# 	x, y = koptok.position()
# 	if x + stepx >= 200 or x + stepx <= -200:
# 		stepx = -stepx
# 	if y + stepy >= 200 or y + stepy <= -200:
# 		stepy = -stepy
# 	if x + stepx <= -100 and y == -170:
# 		break
# 	if x + stepy <= -100 and -170 > y > -195:
# 		break

# 	koptok.goto(x + stepx, y + stepy) 
oyna.mainloop()