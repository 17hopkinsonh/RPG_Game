"""
    Author: Hayden Hopkinson
    Date: 27/10/2020
    Description: this should ask the user if they want to move, save, or trade
    version: 1.
    improvements from last version:
"""

# libraries
from pythonFiles import file3_1, file3_2, file2_1, file4
# functions

def ask_user(player_stats):
    global player_position
    user_in = input("do you want to [s]ave, [m]ove, or [t]rade: ")
    user_in = user_in.lower()
    if user_in == "s" or user_in == "save":
        print("save not yet implemented")
    elif user_in == "m" or user_in == "move":
        player_position = file3_1.routine((player_position[0], player_position[1]))
        player_x = player_position[0]
        player_y = player_position[1]
        enemy = None
        difficulty = file2_1.create_map()[player_y][player_x]
        enemy = file3_2.random_encounter(difficulty)
        if enemy is not None:
            file4.battle(player_stats, file2_1.set_monsters()[difficulty][enemy], enemy)
    elif user_in == "t" or user_in == "trade":
        print("you cant find anyone to trade with")
    else:
        print("please enter a valid input")

# main
player_position = (3, 19) # this is the location the players should start from
if __name__ == "__main__":
    loop = True
    while loop:
        ask_user()