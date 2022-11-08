def move_up(key):
    state = True
    while state:
        if key == "key up":
            return "snake moves up"
        state = False
    return "wrong key"

def move_down(key):
    state = True
    while state:
        if key == "key down":
            return "snake moves down"
        state = False
    return "wrong key"
    
def move_left(key):
    state = True
    while state:
        if key == "key left":
            return "snake moves left"
        state = False
    return "wrong key"

def move_right(key):
    state = True
    while state:
        if key == "key right":
            return "snake moves right"
        state = False
    return "wrong key"
    