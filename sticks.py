def initial_sticks(string):
    try:
        if int(string) < 100 and int(string) > 10:
            return True
        else:
            return False
    except ValueError:
        return False

def player_choice(string):
    try:
        if int(string) in [1, 2, 3]:
            return True
        else: return False
    except ValueError:
        return False

def sticks_left(sticks_left, last_choice):
    return sticks_left - last_choice

def game_over(sticks_left):
    if sticks_left == 1:
        return True
    else:
        return False
