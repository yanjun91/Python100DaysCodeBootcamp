def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
while front_is_clear():
    move() # move to a wall to initialize it
    
turn_left() # make sure there is a wall in right side  

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()

################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
