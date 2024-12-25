from turtle import *
import time
import random

COLORS = ['Blue','Red','Green','Orange','Yellow','Black']
WIDTH, HEIGHT = 500, 500


def init_screen():
    screen = Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtle Racing")


def get_number_of_racer():
    racers = 0
    while True:
        racers = input("Enter the number of racers (2-6): ")
        if racers.isdigit():
            racers = int(racers)
        else:
            print("Input is nut numeric.. Try again!")
            continue

        if 2 <= racers <= 6:
            return racers
        else:
            print("Number not in range 2-6. Try Again!")


def create_turtles(colors):
    turtles = []
    spacingx = WIDTH // (len(colors) +1) 
    for i, color in enumerate(colors):
        racer = Turtle()
        racer.color(color)
        racer.shape("turtle")
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH // 2 + (i + 1) * spacingx, -HEIGHT // 2 + 20)
        racer.pendown()
        turtles.append(racer)

    return turtles


def race(colors):
    turtles = create_turtles(colors)
    
    while True:
        for racer in turtles:
            move = random.randrange(1, 20)
            racer.forward(move)

            x, y = racer.pos()
            if y >= HEIGHT // 2 - 10:
               return colors[turtles.index(racer)]
                


number_of_racers = get_number_of_racer()
init_screen()
random.shuffle(COLORS)
colors = COLORS[:number_of_racers]


winner_turtle = race(colors)
print(f"{winner_turtle} Turtle Won")
time.sleep(5)



