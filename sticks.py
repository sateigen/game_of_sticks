import random
import sys

def check_initial_sticks(user_in):
    try:
        if int(user_in) <= 100 and int(user_in) >= 10:
            return True
        else:
            return False
    except ValueError:
        return False


def check_player_choice(user_in):
    try:
        if int(user_in) in [1, 2, 3]:
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



def get_user_choice(user_in):
    while True:
        if check_player_choice(user_in):
            return int(user_in)
        elif not check_player_choice(user_in):
            print("That was not a valid choice.")
            return False
            continue


def reset_board(board):
    if not is_game_over(board):
        print("There are {} sticks left on the board.".format(board))



def player_vs_player():
    board = starting_player_vs_player()
    while True:
        player1_choice = get_user_choice(input("Player 1: How many sticks would you like to take away? (1, 2, 3)\n\t>"))
        board -= player1_choice
        reset_board(board)
        if is_game_over(board):
            print("You won! You left your partner with the last stick.")
            play_again()
            break
        player2_choice = get_user_choice(input("Player 2: How many sticks would you like to take away? (1, 2, 3)\n\t>"))
        board -= player2_choice
        reset_board(board)
        if is_game_over(board):
            print("You won! You left your partner with the last stick.")
            play_again()
            break

# AI part

def set_up_list_ai():
    my_list = list(range(2, 101))
    for number in my_list:
        my_list[number-2] = (number, [1, 2, 3])

    return my_list



def get_computer_choice(sticks_left):
    my_list = set_up_list_ai()
    my_tuple = my_list[sticks_left-2]
    random.shuffle(my_tuple[1])
    shuffled_list = my_tuple[1]
    return shuffled_list[0]


def keep_track_of_guesses(sticks_left, list_of_choices, computer_choice):
    list_of_choices.append(sticks_left)
    list_of_choices.append(computer_choice)
    print("I take {} sticks.".format(computer_choice))
    return list_of_choices


def update_choice_list(list_of_choices, choice_list):
    sticks = [x for x in list_of_choices[::2]]
    choice = [x for x in list_of_choices[1::2]]
    for x in sticks:
        update_tuple = choice_list[x-2]
        add_choice = choice.pop(0)
        update_tuple[1].append(add_choice)
    return choice_list


def play_ai_vs_player():
    board = starting_player_vs_player()
    list_of_choices = []
    while True:
        player1_choice = get_user_choice(input("Player 1: How many sticks would you like to take away? (1, 2, 3)\n\t>"))
        board -= player1_choice
        reset_board(board)
        if is_game_over(board):
            print("You won!")
            play_again()
            break
        computer_choice = get_computer_choice(board)
        keep_track_of_guesses(board, list_of_choices, computer_choice)
        board -= computer_choice
        reset_board(board)
        if is_game_over(board):
            print("I won!")
            update_choice_list(list_of_choices, set_up_list_ai())
            play_again()
            break

def play_again():
    again = input("Do you want to play again? Y/n\n\t>")
    if again.lower() == 'y':
        main()
    else:
        sys.exit()

def main():
    against = input("Do you want to play against a [P]artner, or the [C]omputer?")
    if against.lower() == 'p':
        player_vs_player()
    else:
        play_ai_vs_player()


if __name__ == '__main__':
    main()
