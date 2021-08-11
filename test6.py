import turtle

def star(color, sides, length, angle, distance):
    galileo = turtle.Turtle()
    galileo.color(color)
    galileo.width(5) 
    galileo.speed(8)
    galileo.penup()
    galileo.left(angle)  
    galileo.forward(distance)
    galileo.pendown()  
    for side in range(sides):
        galileo.forward(length)
        galileo.left(720 / sides)
    galileo.hideturtle() 



star("red", 5, 50, 180, 200)
star("red", 5, 50, 150, 200)
star("red", 5, 50, 120, 200)
star("red", 5, 50, 90, 200)
star("red", 5, 50, 60, 200)
star("red", 5, 50, 30, 200)
star("red", 5, 50, 0, 200)

star("blue", 5, 30, 180, 150)
star("blue", 5, 30, 150, 150)
star("blue", 5, 30, 120, 150)
star("blue", 5, 30, 90, 150)
star("blue", 5, 30, 60, 150)
star("blue", 5, 30, 30, 150)
star("blue", 5, 30, 0, 150)

# for angle in [180, 135, 90, 45, 0]:
#     star("red", 5, 50, angle, 100)

# for angle in [180, 135, 90, 45, 0]:
#     star("blue", 5, 30, angle, 60)
