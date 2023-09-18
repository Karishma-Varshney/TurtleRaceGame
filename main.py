from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title='make your bet', prompt='which turtle will win the race? enter a choice: ')
colors = ['red', 'orange', 'purple', 'blue', 'pink', 'yellow']
y_pos = [-100, -50, 0, 50, 100, 150]
all_turtle = []

for i in range(0, 6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(x=-230, y=y_pos[i])
    all_turtle.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for i in all_turtle:
        if i.xcor() > 230:
            is_race_on = False
            winner = i.pencolor()
            if winner == user_bet:
                print(f"You've won! The {winner} turtle is the winner!")
            else:
                print(f"You've lost! The {winner} turtle is the winner!")

        # Make each turtle move a random amount.
        rand_distance = random.randint(0, 10)
        i.forward(rand_distance)


screen.exitonclick()