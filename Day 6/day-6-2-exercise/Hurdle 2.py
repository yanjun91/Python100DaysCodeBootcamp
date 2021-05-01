def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def run_over_hurdle():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
while not at_goal():
    run_over_hurdle()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
