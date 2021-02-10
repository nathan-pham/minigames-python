from window import window
import turtle
import game

# Event Listeners
def paddle_up(player):
    y = player.ycor()  + 20
    if y >= 250:
        y = 250
    player.sety(y)

def paddle_down(player):
    y = player.ycor() - 20
    if y <= -250:
        y = -250
    player.sety(y)

# Player 1
player_1 = game.Paddle(-350, 0)
player_1.listen("w", paddle_up)
player_1.listen("s", paddle_down)

# Player 2
player_2 = game.Paddle(350, 0)
player_2.listen("Up", paddle_up)
player_2.listen("Down", paddle_down)

# Ball
ball = game.Ball(0, 0)

# Scores
scores = {
    "player_1": 0,
    "player_2": 0
}

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)

# Main game loop
while True:
    window.update()
    ball.collision([player_1, player_2])

    player_point = ball.boundary()
    if player_point in scores:
        scores[player_point] += 1
    
    score_1 = scores["player_1"]
    score_2 = scores["player_2"]
    pen.clear()
    pen.write(f"Player 1: { score_1 }  Player 2: { score_2 }", align="center", font=("Courier", 24, "normal"))

    ball.update()