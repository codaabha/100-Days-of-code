#Day 6 Project: Escaping the maze
#Topics: Functions& Karel, code indentation, while loop

#Yet to cover edge cases, come back to this later and work on it (debug)
def rightTurn():
    turn_left()
    turn_left()
    turn_left()
while not at_goal():
    if right_is_clear():
        rightTurn()
        move()
    elif front_is_clear():
        move()
    else: 
         turn_left()