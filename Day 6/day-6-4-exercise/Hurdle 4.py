def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump_over_hurdle():
    turn_left() # turn at bottom of hurdle
    while not right_is_clear():
        move() # move until the top of hurdle
    turn_right()
    move()
    turn_right() 
    while front_is_clear():
        move() # move until the bottom of hurdle
    turn_left()
    
while not at_goal():
    if front_is_clear():
        move()
    elif wall_in_front():
        jump_over_hurdle()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
