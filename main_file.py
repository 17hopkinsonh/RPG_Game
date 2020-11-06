"""
    Author: Hayden Hopkinson
    Date: 13/10/2020
    Description: main file that calls the functions
    version: 1.
    improvements from last version: N/A
"""
# libraries
from pythonFiles import file1, file1_1, file1_1_1, file1_1_3, file1_1_4_ver2, file2, file3

# main
if __name__ == "__main__":
    file1.explain_game()
    #clear console
    first_response = file1_1.ask_user()
    #clear console

    # ask_user will return "n", "l", or "v"
    # depending on if the user wanted to start a new game, load a game, or view the leaderboard
    if first_response == 'n':
        file1_1_3.add_database(file1_1_3.connect_to_database(), file1_1_1.ask_username(), file1_1_1.ask_password())
        player_stats = file2.set_stats()
    elif first_response == "l":
        credentials = file1_1_4_ver2.ask_credentials() # ask_credentials should return the rowid of the user,
                                                       # along with username and password
        user_id = credentials[0][0] #the rowid of the user returns in two layers
        username = credentials[1]
        password = credentials[2]
        player_stats = file2.load_stats(user_id)
    elif first_response == "v":
        print("view still to be impemented")
    else:
        print("something went wrong")
    game_not_win = True
    while game_not_win:
        file3.ask_user(player_stats)



