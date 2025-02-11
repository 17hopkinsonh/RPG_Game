"""
    Author: Hayden Hopkinson
    Date: 18/09/2020
    Description: this file will check the provided username and password to see if they meet the requirements
    version: 1.
    improvements from last version:
"""

# libraries
import string # the string library will let me use lists with each type of character without having to make them myself
# functions
def check_username(username):
    accepted_characters = []
    for i in username:
        if i in string.ascii_letters or i in string.digits:
            accepted_characters.append(i)
        else:
            print("character {} is not an accepted character".format(i))
            return
    if len(accepted_characters) > 2:
        return ask_if_name_good("".join(accepted_characters))
    else:
        print("your username needs to only contain letters and numbers, and be at least 3 characters")
def ask_if_name_good(username):
    player_input = input("Is the username {} ok? (Y/N) ".format(username))
    player_input = player_input.lower()
    if (player_input == "y") or (player_input == "yes"):
        return True
    else:
        return False
def check_password(password):
    if (len(password) > 4) and (password.lower() != password) and (password.upper() != password):
        return True
    else:
        return False
# main
if __name__ == "__main__":
    print(ask_if_name_good("Bob"))