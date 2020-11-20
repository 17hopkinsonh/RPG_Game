"""
    Author: Hayden Hopkinson
    Date: 29/10/2020
    Description:
    version: 1.
    improvements from last version:
"""

# libraries
from pythonFiles import file2_1ver2

# functions

def routine(player_position, game_map = file2_1ver2.create_map()):
    sight(player_position, game_map)
    return ask_movement(player_position, game_map)


def sight(player_position, game_map):
    print("to the [n]orth you see " + file2_1ver2.tile_descriptions()[game_map[player_position[1] - 1][player_position[0]]])
    print("to the [e]ast you see " + file2_1ver2.tile_descriptions()[game_map[player_position[1]][player_position[0] + 1]])
    print("to the [s]outh you see " + file2_1ver2.tile_descriptions()[game_map[player_position[1] + 1][player_position[0]]])
    print("to the [w]est you see " + file2_1ver2.tile_descriptions()[game_map[player_position[1]][player_position[0] - 1]])

def ask_movement(player_position, game_map):
    print("what direction would you like to move?")
    new_pos = None
    while new_pos is None:
        direction = input("[n]orth, [e]ast, [s]outh, or [w]est: ")
        direction = direction.lower()
        if direction == "n" or direction == "north":
            new_pos = movement(player_position,1,0,game_map)
        elif direction == "e" or direction == "east":
            new_pos = movement(player_position,0,-1,game_map)
        elif direction == "s" or direction == "south":
            new_pos = movement(player_position,-1,0,game_map)
        elif direction == "w" or direction == "west":
            new_pos = movement(player_position,0,1, game_map)
        else:
            print("invalid movement direction")
    return new_pos

def movement(player_position, x, y, game_map):
    if game_map[player_position[1] - x][player_position[0] - y] == 0:
        print("you cant move there")
    else:
        return [player_position[0] - y, player_position[1] - x]

# this is extreamly buggy, and so i chose to remake it in the two components above
"""def move(player_x, player_y):
    player_position = (player_x, player_y)
    print(player_position)
    if player_position is None:
        player_position = file3.set_location()
    game_map = file2_1.create_map()
    print("to the [n]orth you see " + file2_1.tile_descriptions()[game_map[player_position[1]][player_position[0] + 1]])
    print("to the [e]ast you see " + file2_1.tile_descriptions()[game_map[player_position[1] + 1][player_position[0]]])
    print("to the [s]outh you see " + file2_1.tile_descriptions()[game_map[player_position[1]][player_position[0] - 1]])
    print("to the [w]est you see " + file2_1.tile_descriptions()[game_map[player_position[1] - 1][player_position[0]]])
    player_in = input("what direction do you want to move? ")
    player_in = player_in.lower()
    if player_in == "n" or player_in == "north":
        if game_map[player_position[1]][player_position[0] + 1] == 0:
            print("you cant move in that direction as there is an ocean")
        else:
            player_position = file3.set_location(player_position[0], player_position[1] + 1)
    elif player_in == "e" or player_in == "east":
        if game_map[player_position[1] + 1][player_position[0]] == 0:
            print("you cant move in that direction as there is an ocean")
        else:
            player_position = file3.set_location(player_position[0] + 1, player_position[1])
    elif player_in == "s" or player_in == "south":
        if game_map[player_position[1]][player_position[0] - 1] == 0:
            print("you cant move in that direction as there is an ocean")
        else:
            player_position = file3.set_location(player_position[0] , player_position[1] - 1)
    elif player_in == "w" or player_in == "west":
        if game_map[player_position[1] - 1][player_position[0]] == 0:
            print("you cant move in that direction as there is an ocean")
        else:
            player_position = file3.set_location(player_position[0] - 1, player_position[1])
    print(player_position)
    return player_position"""

# main
win = False
if __name__ == "__main__":
    print()