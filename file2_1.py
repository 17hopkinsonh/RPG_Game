"""
    Author: Hayden Hopkinson
    Date: 15/10/2020
    Description: this file will make a map of the game with difficulties for each tile, it also has a dictionary of
    the enemies stats
    version: 1.
    improvements from last version:
"""

# libraries


# functions
def tile_descriptions():
    descriptions = [
        "from where you are standing you can see that there is an untraversable ocean there.",
        "just a whole bunch of forest in that direction.",
        "you can see that there is a beach there.",
        "there's desert in that direction.",
        "the desert in that direction seems to be extreamly dry.",
        "the deserts gotten so dry theat there's a fire, its still traversable, but be carefull if you run into any monsters."
    ]
    return descriptions
def create_map():
    #this makes and returns a map of the game, with each tile having a difficulty rating,
    #with 1 being the most easy and 5 being the most difficult
    #a 0 means that that tile is not walkable
    game_map = [
        [0,0,0,0,0,0,0,0,0,0,0,0],
        [0,5,5,5,5,5,4,4,4,4,4,0],
        [0,5,5,5,5,5,4,4,4,4,4,0],
        [0,5,5,5,5,5,4,4,4,4,4,0],
        [0,5,5,5,5,5,4,4,4,4,4,0],
        [0,5,5,5,5,5,4,4,4,4,4,0],
        [0,4,4,4,4,4,4,4,4,4,4,0],
        [0,3,3,3,3,3,3,3,3,3,3,0],
        [0,3,3,3,3,3,3,3,3,3,3,0],
        [0,3,3,3,3,3,3,3,3,3,3,0],
        [0,3,3,3,3,3,3,3,3,3,3,0],
        [0,3,3,3,3,3,3,3,3,3,3,0],
        [0,1,1,1,1,1,1,1,1,1,1,0],
        [0,1,1,1,1,1,1,1,1,1,1,0],
        [0,1,1,1,1,2,2,2,2,2,1,0],
        [0,1,1,1,1,2,0,0,0,2,1,0],
        [0,1,1,1,1,2,0,0,0,2,1,0],
        [0,1,1,1,1,2,2,0,0,2,1,0],
        [0,1,1,1,1,1,2,2,2,2,1,0],
        [0,1,1,1,1,1,1,1,1,1,1,0],
        [0,1,1,1,1,1,1,1,1,1,1,0],
        [0,0,0,0,0,0,0,0,0,0,0,0]
    ]
    return game_map

def set_monsters():
    enemies = [
        {
            "null": (0, 0)
        },
        {
            "slime":     (15, 2 , 5 , 1 , 1 , 10),
            "frog":      (10, 1 , 4 , 1 , 0 , 3 ),
            "small bat": (5 , 4 , 10, 2 , 0 , 5 ),
            "bird":      (12, 1 , 4 , 2 , 1 , 4 )
        },
        {
            "large spider":   (30, 5 , 10, 3 , 10, 15),
            "fish with legs": (25, 10, 20, 1 , 5 , 10),
            "seagull":        (20, 1 , 5 , 1 , 15, 25)
        },
        {
            "skeleton":   (50, 10, 25, 5 , 20, 35),
            "zombie":     (40, 15, 20, 2 , 20, 30),
            "large bat":  (30, 20, 25, 0 , 30, 35),
            "giant worm": (60, 20, 30, 3 , 10, 50)
        },
        {
            "giant rat": (75 , 40, 45, 7 , 50, 75),
            "tiger":     (100, 50, 50, 10, 70, 80)
        },
        {
            "mimic":  (150, 60, 65 , 20, 150, 250 ),
            "dragon": (250, 30, 150, 30, 400, 1000)
        },
    ]
    # this is a list with 5 dictionaries, each representing a  different difficulty of enemies,
    # the dictionaries themselfes contain stats in this order:
    # max hp, min damage, max damage, armor, min gold dropped, max gold dropped
    return enemies
if __name__ == "__main__":
    #print(tile_descriptions()[create_map()[int(input("rows down: "))][int(input("rows accross: "))]])
    print(set_monsters()[3]["tiger"])