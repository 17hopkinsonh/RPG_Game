"""
    Author: Hayden Hopkinson
    Date: 30/10/2020
    Description: this component should take the difficulty of the tile a user just moved to
    and check randomly to see if the user should fight an enemy or not
    version: 1.
    improvements from last version:
"""

# libraries
import random
from pythonFiles import file2_1

# functions

def random_encounter(tile_difficulty):
    random_chance = random.randint(0,10)
    list_of_enemies = list(file2_1.set_monsters()[tile_difficulty].keys())
    if len(file2_1.set_monsters()[tile_difficulty]) > random_chance:
        print("you are fighting the " + str(list_of_enemies[random_chance]))
        return str(list_of_enemies[random_chance])


# main


if __name__ == "__main__":

    loop = True
    i = 0
    test_for = 50
    while loop:
        if i > test_for:
            loop = False
        else:
            print(random_encounter(random.randint(1,5)))
            i = i + 1
