from sticks import initial_sticks

def test_initial_amount_of_sticks():
    number_of_sticks = 55
    number_of_sticks2 = 'g'
    number_of_sticks3 = 500

    assert initial_sticks(number_of_sticks) == True
    assert initial_sticks(number_of_sticks2) == False
    assert initial_sticks(number_of_sticks3) == False


def test_player_one_choice():
    number1 =
