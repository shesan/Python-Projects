#Pong game. Made by self.
import turtle

#window dimensions
width = 800
height = 600

#player dimensions
p_height = 5
p_width = 1

#speed of player and ball
move_speed = 10
ball_speed = 1

#score tracker
score_1 = 0
score_2 = 0

#
win = turtle.Screen()
win.title("PONG CLASSIC")
win.bgcolor("black")
win.setup(width=width, height=height)
win.tracer(0)

#
box = turtle.Turtle()
box.setpos(-(width/2), (height/2))
box.hideturtle()
box.color("White")
box.speed(0)
box.forward(width)
box.right(90)
box.forward(height)
box.right(90)
box.forward(width)
box.right(90)
box.forward(height)

#Player1 set up
player_1 = turtle.Turtle()
player_1.shape("square")
player_1.shapesize(p_height, p_width)
player_1.color("blue")
player_1.speed(0)
player_1.penup()
player_1.goto(-((width/2)-50), 0)

#Player2 set up
player_2 = turtle.Turtle()
player_2.shape("square")
player_2.shapesize(p_height, p_width)
player_2.color("red")
player_2.speed(0)
player_2.penup()
player_2.goto((width/2)-50, 0)

#Ball set up
ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.penup()    #We can remove this if we want to see the path
ball.speed(0)   #Increase to increase difficulty
ball.goto(0,0)
ball.dx, ball.dy = ball_speed, ball_speed

#Score set up
score = turtle.Turtle()
score.color("white")
score.speed(0)
score.penup()
score.hideturtle()
score.goto(0, (height/2 - 50))
score.write("Player 1: 0    Player 2: 0", align="center", font=('Arial', 24, "normal"))

#Functions
def move_1_up():
    y = player_1.ycor()
    y += move_speed
    if(y > (height/2) - (p_height * 10)):
        player_1.sety((height/2) - (p_height * 10))
    else:
        player_1.sety(y)

def move_1_down():
    y = player_1.ycor()
    y -= move_speed
    if(y < -(height/2) + (p_height * 10)):
        player_1.sety(-(height/2) + (p_height * 10))
    else:
        player_1.sety(y)

def move_2_up():
    y = player_2.ycor()
    y += move_speed
    if(y > (height/2) - (p_height * 10)):
        player_2.sety((height/2) - (p_height * 10))
    else:
        player_2.sety(y)

def move_2_down():
    y = player_2.ycor()
    y -= move_speed
    if(y < -(height/2) + (p_height * 10)):
        player_2.sety(-(height/2) + (p_height * 10))
    else:
        player_2.sety(y)

#Keypress
win.listen()
win.onkeypress(move_1_up, "w")
win.onkeypress(move_1_down, "s")
win.onkeypress(move_2_up, "Up")
win.onkeypress(move_2_down, "Down")

#Main
while True:
    win.update()

    #Ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Top and bottom wall
    if abs(ball.ycor()) > height/2:
        ball.dy*= -1
    
    #Right wall
    if ball.xcor() > width/2:
        ball.dx *= -1       
        ball.setpos(0,0)
        score_1 += 1
        score.clear()
        score.write("Player 1: {}    Player 2: {}".format(score_1, score_2), align="center", font=('Arial', 24, "normal"))

    #Left wall
    if ball.xcor() < -(width/2):    
        ball.dx *= -1       
        ball.setpos(0,0)
        score_2 += 1
        score.clear()
        score.write("Player 1: {}    Player 2: {}".format(score_1, score_2), align="center", font=('Arial', 24, "normal"))

    #Collisions between player and ball Player 1
    if ((ball.xcor() == player_1.xcor() + p_width*10) and ((player_1.ycor() + p_height*10) > ball.ycor() >= player_1.ycor() - p_height*10)):
        ball.dx *= -1
    
    #Collisions between player and ball Player 2
    if ((ball.xcor() == player_2.xcor() - p_width*10) and ((player_2.ycor() + p_height*10) > ball.ycor() >= player_2.ycor() - p_height*10)):
        ball.dx *= -1
