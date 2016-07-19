def initial_sticks(string):
    try:
        if int(string) < 100:
            return True
        else:
            return False
    except ValueError:
        return False
 
