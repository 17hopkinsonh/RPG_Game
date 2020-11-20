"""
    Author: Hayden Hopkinson
    Date: 20/11/2020
    Description: A start screen explaining to the user how the game works
    version: 1.1
    changes from last version: this version uses a list of multiple strings instead of a single string
"""

# libraries

# functions


def explain_game():
    """this will print out a explanation of the game to the user. Takes no paramiters and returns nothing"""
    messages = [
        "In this game you will be tasked with opening the magical chest,",
        "to open it you will first need to find the key,",
        "and while you search for them there will be enemy's that will try to stop you.",
        "You will need to fight these enemy's which will give you some gold and a chance of a new attack,",
        "which you will be able to use in future encounters, as you progress on you",
        "will fight stronger and stronger enemy's which will drop stat improvements for you."
    ]
    for i in messages:
        print(i)


# main
if __name__ == "__main__":
    explain_game()