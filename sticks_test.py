from sticks import *

def test_initial_amount_of_sticks_is_number_between_ten_and_one_hundred():
    number_of_sticks = '55'
    number_of_sticks2 = 'g'
    number_of_sticks3 = '500'

    assert initial_sticks(number_of_sticks) == True
    assert initial_sticks(number_of_sticks2) == False
    assert initial_sticks(number_of_sticks3) == False


def test_player_choice_is_between_one_and_three():
    number1 = '2'
    number2 = '5'
    number3 = 's'

    assert player_choice(number1) == True
    assert player_choice(number2) == False
    assert player_choice(number3) == False

def test_number_of_sticks_left():
    number_of_sticks = 100
    user_in = 2

    assert sticks_left(number_of_sticks, user_in) == 98

def test_is_game_over_when_one_stick_left():
    sticks_left1 = 1
    sticks_left2 = 3

    assert game_over(sticks_left1) == True
    assert game_over(sticks_left2) == False
