"""
    Author: Hayden Hopkinson
    Date: 15/09/2020
    Description: this file is reponsible for letting the player win by first picking up a key,
    and then using it to unlock a mysterius door
    version: 1.
    improvements from last version:
"""

# libraries
from pythonFiles import file5
# functions


def check_position(x, y, user_id, player_stats):
    global has_key
    if x == 4 and y == 3 and not has_key:
        has_key = True
        print("you found a key, wonder what it goes to?")
    elif x == 2 and y == 2:
        if has_key:
            print("You use the mysterius key you found previusly to unlock the door...")
            print("to be continued")
            file5.save_game(user_id, player_stats)
        else:
            print("You can see a door in the ground, but you will need a key to open it")

# main
has_key = False
if __name__ == "__main__":
    print("")