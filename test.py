import turtle
import random

turtle.tracer(1,0)
SIZE_X=800
SIZE_Y=500
turtle.setup(SIZE_X, SIZE_Y) 

turtle.penup()

CIRCLE_SIZE = 20
START_LENGTH = 1

pos_list = []
stamp_list = []
food_pos = []
food_stamps = []

circle = turtle.clone()
circle.shape("circle")
turtle.hideturtle()


for i in range(START_LENGTH):
    x_pos=circle.pos()[0]
    y_pos=circle.pos()[1]
    x_pos+=CIRCLE_SIZE

    my_pos=(x_pos,y_pos)
    circle.goto(x_pos,y_pos)
    pos_list.append(my_pos)
    new_stamp=circle.stamp()
    stamp_list.append(new_stamp)
    
UP_ARROW="Up"
LEFT_ARROW="Left"
DOWN_ARROW="Down"
RIGHT_ARROW="Right"
TIME_STEP=100

UP=0
LEFT=1
DOWN=2
RIGHT=3


direction= UP
UP_EDGE=250
DOWN_EDGE=-250
RIGHT_EDGE=400
LEFT_EDGE=-400


def up():
    global direction
    direction=UP
    print("you pressed the up key!")
    
           

def down():
    global direction
    direction=DOWN
    print("you pressed the down key!")



def left():
    global direction
    direction=LEFT
    print("you pressed the left key!")



def right():
    global direction
    direction=RIGHT
    print("you pressed the right key!")


turtle.onkeypress(up, UP_ARROW)
turtle.onkeypress(down, DOWN_ARROW)
turtle.onkeypress(left, LEFT_ARROW)
turtle.onkeypress(right, RIGHT_ARROW)
turtle.listen()

def move_circle():
    my_pos=circle.pos()
    x_pos=my_pos[0]
    y_pos=my_pos[1]


    if direction==RIGHT:
        circle.goto(x_pos+CIRCLE_SIZE, y_pos)
        print("you moved RIGHT!")
    elif direction==LEFT:
        circle.goto(x_pos-CIRCLE_SIZE, y_pos)
        print("you moved LEFT!")


    
    elif direction==UP:
        circle.goto(x_pos, y_pos+CIRCLE_SIZE)
        print("you moved UP!")
    else:
        circle.goto(x_pos, y_pos-CIRCLE_SIZE)
        print("you moved DOWN!")


    new_pos=circle.pos()
    new_x_pos=new_pos[0]
    new_y_pos=new_pos[1]
