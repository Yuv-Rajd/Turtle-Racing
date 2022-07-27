import random
from turtle import Turtle,Screen

is_race_on=False
screen=Screen()
screen.setup(width=800,height=500)
user_bet=screen.textinput(title="make your bet",prompt="Which turtle will win the race? Enter the color :")
print(user_bet)
colors=["red","orange","yellow","green","blue","purple"]
y_positions=[-100,-60,-20,20,60,100]
all_turtle=[]

for turtle_index in range(0,6):
    new_turtle=Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-380,y=y_positions[turtle_index])
    all_turtle.append(new_turtle)

if user_bet:
    is_race_on=True

while is_race_on:

    for turtle in all_turtle:
        if turtle.xcor()>380:
            is_race_on=False
            winning_color=turtle.pencolor()
            if winning_color==user_bet:
                print(f"you've won! the {winning_color} turtle is the winner!")
            else:
                print(f"you've lost! the {winning_color} turtle is the winner!")
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)

screen.exitonclick()