import turtle
import math
import random

#----------------------------#

turtle.speed(0)
turtle.penup()

p1_points = 0
p2_points = 0

t = turtle.Turtle()
wn = turtle.Screen()

dr1 = -200
dr2 = 200

ball_image = "ball.gif"
paddle_image = "paddle.gif"

#----------------------------#

wn.register_shape(paddle_image)
wn.register_shape(ball_image)

p1 = turtle.Turtle()
p1.penup()
p1.shape(paddle_image)
turtle.penup()

p2 = turtle.Turtle()
p2.penup()
p2.shape(paddle_image)
turtle.penup()

b = turtle.Turtle()
b.penup()
b.shape(ball_image)

sc = turtle.Turtle()
sc.color("white")
sc.penup()

p1.goto(-200,0)
p2.goto(200,0)
b.goto(0,0)
sc.goto(0,200)

#----------------------------#

def move_up1():
    p1.goto(p1.xcor(),p1.ycor()+15)

def move_down1():
    p1.goto(p1.xcor(),p1.ycor()-15)

def move_up2():
    p2.goto(p2.xcor(),p2.ycor()+15)

def move_down2():
    p2.goto(p2.xcor(),p2.ycor()-15)

def draw_p1_score():
    global dr1
    sc.goto(dr1,200)
    sc.pendown()
    sc.write("o")
    sc.penup()
    dr1 += 25
    sc.goto(0,200)

def draw_p2_score():
    global dr2
    sc.goto(dr2,200)
    sc.pendown()
    sc.write("o")
    sc.penup()
    dr2 -= 25
    sc.goto(0,200)

#----------------------------#

wn.bgcolor("black")

wn.onkeypress(move_up1, "w")
wn.onkeypress(move_down1, "s")
wn.onkeypress(move_up2, "Up")
wn.onkeypress(move_down2, "Down")

#----------------------------#

turtle.listen()

while p1_points != 5 or p2_points != 5:
    random_direction = random.randint(0,360)
    b.setheading(random_direction)
    while b.xcor() <= 240 or b.xcor() >= -240 or b.ycor() <= 240 or b.ycor() >= -240:
        b.forward(2)
        if b.xcor() > 240:
            '''
            b.speed(0)
            random_direction += 130
            b.setheading(random_direction)
            b.speed(1)
            '''
            p1_points += 1
            draw_p1_score()
            b.speed(0)
            b.goto(0,0)
            b.speed(1)
            random_direction = random.randint(0,360)
            b.setheading(random_direction)
        elif b.xcor() < -240:
            '''
            b.speed(0)
            random_direction += 130
            b.setheading(random_direction)
            b.speed(1)
            '''
            p2_points += 1
            draw_p2_score()
            b.speed(0)
            b.goto(0,0)
            b.speed(1)
            random_direction = random.randint(0,360)
            b.setheading(random_direction)
        elif b.ycor() > 240:
            b.speed(0)
            random_direction += 130
            b.setheading(random_direction)
            b.speed(1)
        elif b.ycor() < -240:
            b.speed(0)
            random_direction += 130
            b.setheading(random_direction)
            b.speed(1)

turtle.listen()
wn.mainloop()