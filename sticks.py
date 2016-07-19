def check_initial_sticks(string):
    try:
        if int(string) <= 100 and int(string) >= 10:
            return True
        else:
            return False
    except ValueError:
        return False

def check_player_choice(string):
    try:
        if int(string) in [1, 2, 3]:
            return True
        else: return False
    except ValueError:
        return False

def reset_sticks(sticks_left, last_choice):
    return sticks_left - last_choice

def is_game_over(sticks_left):
    if sticks_left <= 1:
        return True
    else:
        return False


def starting_player_vs_player():
    print("How many sticks would you like your game to start with?")
    while True:
        starting_sticks = input("Choose a number between 10 and 100.\n\t>")
        if check_initial_sticks(starting_sticks):
            return int(starting_sticks)
        elif not check_initial_sticks(starting_sticks):
            print("That was not a valid choice.")
            continue

def get_user_choice(user_in):
    while True:
        if check_player_choice(user_in):
            return int(user_in)
        elif not check_player_choice(user_in):
            print("That was not a valid choice.")
            continue

def reset_board(board):
    if not is_game_over(board):
        print("There are {} sticks left on the board.".format(board))
    elif is_game_over(board):
        print("You lost")


def player_vs_player():
    board = starting_player_vs_player()
    while True:
        player1_choice = get_user_choice(input("Player 1: How many sticks would you like to take away? (1, 2, 3)\n\t>"))
        board -= player1_choice
        reset_board(board)
        if is_game_over(board):
            break
        player2_choice = get_user_choice(input("Player 2: How many sticks would you like to take away? (1, 2, 3)\n\t>"))
        board -= player2_choice
        reset_board(board)
        if is_game_over(board):
            break

def main():
    # if user wants to play against human:
        player_vs_player
