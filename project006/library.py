def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def keep_moving():
    while True:
        if at_goal():
            done()
        if wall_in_front():
            break
        move()

def turnaround_left():
    turn_left()
    move()
    turn_left()

def turnaround_right():
    turn_right()
    move()
    turn_right()

def hurdle():
    turn_left()
    while wall_on_right():
        move() 
    turnaround_right()
    while front_is_clear():
        move() 
    turn_left()
