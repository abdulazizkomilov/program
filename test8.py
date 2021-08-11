import turtle 
import random
t = turtle.Turtle()

a = ["happy", "sad", "angry"]
c = random.choice(a)

def roll(tur):
	if c == "happy":
		return "yellow"
	if c == "sad":
		return "blue"
	if c == "angre":
		return "red"
	else:
		return "green"

for side in range(5):
	t.color(roll(a))
	t.forward(100)
	t.right(144)