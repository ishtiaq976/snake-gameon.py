import turtle
import random
import time

delay = 0.1
score = 0
highestscore = 0

# Snake bodies
bodies = []

# Getting a screen
s = turtle.Screen()
s.title("Snake Game")
s.bgcolor("gray")
s.setup(width=600, height=600)

# Create snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.fillcolor("blue")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("yellow")
food.fillcolor("green")
food.penup()
food.goto(0, 100)

# Scoreboard
sb = turtle.Turtle()
sb.speed(0)
sb.color("white")
sb.penup()
sb.hideturtle()
sb.goto(-250, 260)
sb.write("Score: 0 | High Score: 0", font=("Arial", 14, "bold"))

# Movement functions
def moveup():
    if head.direction != "down":
        head.direction = "up"

def movedown():
    if head.direction != "up":
        head.direction = "down"

def moveleft():
    if head.direction != "right":
        head.direction = "left"

def moveright():
    if head.direction != "left":
        head.direction = "right"

def movestop():
    head.direction = "stop"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# Event handling key mapping
s.listen()
s.onkey(moveup, "Up")
s.onkey(movedown, "Down")
s.onkey(moveleft, "Left")
s.onkey(moveright, "Right")
s.onkey(movestop, "space")

# Main loop
while True:
    s.update()

    # Check collision with border
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        # Hide and clear bodies
        for body in bodies:
            body.hideturtle()
        bodies.clear()

        # Reset score and delay
        score = 0
        delay = 0.1

        # Update scoreboard
        sb.clear()
        sb.write(f"Score: {score} | High Score: {highestscore}", font=("Arial", 14, "bold"))

    # Check collision with food
    if head.distance(food) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        food.goto(x, y)

        # Add new body
        body = turtle.Turtle()
        body.speed(0)
        body.shape("square")
        body.color("red")
        body.fillcolor("black")
        body.penup()
        bodies.append(body)

        # Increase score
        score += 10
        delay -= 0.001

        # Update highest score
        if score > highestscore:
            highestscore = score

        sb.clear()
        sb.write(f"Score: {score} | High Score: {highestscore}", font=("Arial", 14, "bold"))

    # Move the body segments
    for index in range(len(bodies)-1, 0, -1):
        x = bodies[index-1].xcor()
        y = bodies[index-1].ycor()
        bodies[index].goto(x, y)

    if len(bodies) > 0:
        x = head.xcor()
        y = head.ycor()
        bodies[0].goto(x, y)

    move()

    # Check collision with body
    for body in bodies:
        if body.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            for body in bodies:
                body.hideturtle()
            bodies.clear()
            score = 0
            delay = 0.1
            sb.clear()
            sb.write(f"Score: {score} | High Score: {highestscore}", font=("Arial", 14, "bold"))

    time.sleep(delay)


#this is my snake game  project (ishtiaq ahmad , F24613)
