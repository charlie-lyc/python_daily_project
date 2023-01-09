from library import turn_right, keep_moving, turnaround_left, turnaround_right, hurdle 

right_count = 0
left_count = 0
while True:
    if at_goal():
        done()
    if right_is_clear():
        if right_count == 4:
            turn_left()
            right_count = 0
        else:
            turn_right()
            right_count += 1
            left_count = 0
    else:
        if left_count == 4:
            turn_right()
            left_count = 0
        else:
            turn_left()
            left_count += 1
            right_count = 0
    if front_is_clear():
        move()