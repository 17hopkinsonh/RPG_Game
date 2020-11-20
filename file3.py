"""
    Author: Hayden Hopkinson
    Date: 27/10/2020
    Description: this should ask the user if they want to move, save, or trade
    version: 1.
    improvements from last version:
"""

# libraries
from pythonFiles import file3_1, file3_2, file2_1ver2, file4, file5, file7, file9
# functions


def ask_user(player_stats, user_id):
    global player_position
    user_in = input("do you want to [s]ave, [m]ove, or [t]rade: ")
    user_in = user_in.lower()
    if user_in == "s" or user_in == "save":
        file5.save_game(user_id, player_stats)
        return player_stats
    elif user_in == "m" or user_in == "move":
        player_position = file3_1.routine((player_position[0], player_position[1]))
        player_x = player_position[0]
        player_y = player_position[1]
        file7.check_position(player_x, player_y, user_id, player_stats)
        enemy = None
        difficulty = file2_1ver2.create_map()[player_y][player_x]
        enemy = file3_2.random_encounter(difficulty)
        file9.clear()
        if enemy is not None:
            return file4.battle(player_stats, file2_1ver2.set_monsters()[difficulty][enemy], enemy, difficulty)
        else:
            return player_stats
    elif user_in == "t" or user_in == "trade":
        print("you cant find anyone to trade with")
        return player_stats
    else:
        print("please enter a valid input")
        return player_stats



# main
player_position = (3, 19) # this is the location the players should start from
if __name__ == "__main__":
    loop = True
    while loop:
        ask_user()