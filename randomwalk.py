import turtle
import random
from turtle import Turtle,Screen
tortoise=Turtle()
screen=Screen()
colors=["red","green","blue","brown","pink","violet","yellow"]
directions=[0,90,180,270]
tortoise.pensize(15)
tortoise.speed("fast")
def random_walk():
    n=int(input("Enter the number of directions: "))
    for i in range(n):
        tortoise.color(random.choice(colors))
        tortoise.forward(30)
        tortoise.setheading(random.choice(directions))
    screen.exitonclick()
while(True):
    choice=input("Do you want to continue drawing the random walk: ")
    if(choice=="yes"):
        random_walk()
    else:
        print("Thank you for using our application!")
        break
