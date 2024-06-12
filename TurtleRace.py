import random
from turtle import Turtle,Screen
width,height=400,400
color_list=["red","green","pink","yellow","black","brown","blue","orange","aquamarine1","gray"]
print("Turtle Race")
print("*************************")
def no_of_turtle():
    count=0
    while True:
        count=input("How many turtles you want in race(2-10): ")
        if count.isdigit():
            count=int(count)
        else:
            print("Please enter a numeric value between 2 to 10.")
            continue
        if count>10 or count<2:
            print("Input is not in given range... Try again!!")
        else:
            return count
turtles=no_of_turtle()
print(turtles)
s1=Screen()
s1.setup(400,400)
turtle_list=[]
x_spacing=width//(turtles+1)
for i in range(1,turtles+1):
    new_turtle=Turtle()
    new_turtle.shape("turtle")
    new_turtle.left(90)
    new_turtle.color(color_list[i-1])
    new_turtle.penup()
    new_turtle.goto(-width//2+(i*x_spacing),-height//2+10)
    turtle_list.append(new_turtle)
def race():
    is_race_on=True
    while is_race_on:
        for t in turtle_list:
            distance=random.randrange(1,20)
            t.forward(distance)
            x,y=t.pos()
            if y>=height//2-20:
                print(f"The winner is {t.pencolor()} turtle")
                is_race_on=False
race()
s1.exitonclick()