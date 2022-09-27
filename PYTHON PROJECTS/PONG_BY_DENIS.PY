# This is my first game in python from a tutorial
# By @TokyoEdTech
#Part 1 : getting started

from tkinter import W
import turtle
import winsound
# We first create  window named wn

wn = turtle.Screen()
wn.title("Pong by Denis Kalala") # Games title
wn.bgcolor("black") ;'''we are changing the background color'''
wn.setup(width=800,height=600) #we specifying the size of the window
wn.tracer(0) #this stops the window from updating and we have to manually update it ( we did this to speed up the game)

#Score
Score_a = 0
Score_b = 0


# Paddle A
paddle_a =turtle.Turtle()
paddle_a.speed(0) # we set the speed of how it looks on the screen (not speed of movement)
paddle_a.shape("square") # we choose a shape for how the paddle looks like (default is always 20px by 20px)
paddle_a.color("white") # color of the actual paddle 
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup() #we dont want lines being drawn (turtles draw lines as  the move up)
paddle_a.goto(-350,0)

# Paddle B
paddle_b =turtle.Turtle()
paddle_b.speed(0) 
paddle_b.shape("square") 
paddle_b.color("white") 
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup() 
paddle_b.goto(350,0) # we want it on the right side so we make it +350

# Ball
ball =turtle.Turtle()
ball.speed(0) 
ball.shape("square") 
ball.color("white") 
ball.penup() 
ball.goto(0,0)  #ball is located at the center
ball.dx = 0.09    # we assigning the balls movement horizontally (it moves by 2px)
ball.dy = -0.09    # we assigning the balls movement vertically
                            #because they both equal 2 it will move diagnoly at a constant rate

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0 Player B: 0",align="center",font=("courier",24,"normal"))

# We will use a funtion to make the paddles move directed by the keyboard
#paddle A movements
def paddle_a_up():
    y = paddle_a.ycor()           #we assigning the y coordinate to y
    y+=20
    paddle_a.sety(y)   

def paddle_a_down():
    y = paddle_a.ycor()           
    y-=20
    paddle_a.sety(y)   

#paddle B movements
def paddle_b_up():
    y = paddle_b.ycor()          
    y+=20
    paddle_b.sety(y) 

def paddle_b_down():
    y = paddle_b.ycor()          
    y-=20
    paddle_b.sety(y) 

# we have defined the funtion but are yet to assign anything to it
#key board binding
#Paddle A
wn.listen()
wn.onkeypress(paddle_a_up,"w")

wn.listen()
wn.onkeypress(paddle_a_down,"s")

#Paddle B
wn.listen()
wn.onkeypress(paddle_b_up,"Up")

wn.listen()
wn.onkeypress(paddle_b_down,"Down")
# sound
def play():
    winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)

#main game loop (this is where the bulk of the instructions and gameplay usually happen)
while True:
    wn.update() #we used 4 spaces never mix indentation and spacing (we are updating through the loop)
   # sound
    def play():
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
 

    #Move the ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)
    
    #Border cheking

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *=-1
        play()

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *=-1
        play()
    
    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *=-1
        Score_a+=1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(Score_a,Score_b),align="center",font=("courier",24,"normal"))


    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *=-1
        Score_b+=1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(Score_a,Score_b),align="center",font=("courier",24,"normal"))

    # paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor()<350 )and (ball.ycor()<paddle_b.ycor() + 40 and ball.ycor()>paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx*=-1
        play()

    if (ball.xcor() < -340 and ball.xcor()>-350 )and (ball.ycor()<paddle_a.ycor() + 40 and ball.ycor()>paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx*=-1
        play()
