import turtle

START_X = -300
FINISH_X = 280
COLORS = ["red", "green", "blue", "yellow"]

def setup_screen():
    # Creates the white game window
    screen = turtle.Screen()
    screen.setup(700, 400)
    screen.bgcolor("white")
    screen.title("Pagong Karera")
    return screen

def draw_track():
    # Draws the start line, the finish line, and the lane numbers 1-4
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.speed(0)
    for x in [START_X, FINISH_X]:
        pen.penup()
        pen.goto(x, 120)
        pen.pendown()
        pen.goto(x, -120)
        pen.penup()
    for i in range(4):
        pen.goto(START_X - 25, 67 - i * 50)
        pen.write(i + 1, font=("Arial", 14, "bold"))

def reset_turtles(turtles):
    # Puts all turtles on the start line 
    for i in range(4):
        turtles[i].hideturtle()
        turtles[i].speed(0)
        turtles[i].goto(START_X, 75 - i * 50)
        turtles[i].speed(3)
        turtles[i].showturtle()

def create_turtles():
    # Creates the 4 colored turtles and places them on the start line
    turtles = []
    for color in COLORS:
        t = turtle.Turtle("turtle")
        t.color(color)
        t.penup()
        turtles.append(t)
    reset_turtles(turtles)
    return turtles