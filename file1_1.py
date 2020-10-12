"""
    Author: Hayden Hopkinson
    Date: 15/09/2020
    Description: asks the user if they want to start a new game, load a game, or view the leaderboards
    version: 1.0
    improvements from last version: N/A
"""

# libraries

# functions

def check_responce(useranswer):
    # this should check the users input (the passed useranswer) against
    # a list of the inputs that are valid, if the answer is accepted
    # it should change a global variable that will break a loop that is calling this function
    global acceptedanswer
    allowedresponses = ["n", "l", "v"]
    if useranswer in allowedresponses:
        acceptedanswer = True
        return
    else:
        print("The input was rejected, please type n, l, or v")

def ask_user():
    # this should loop over script that asks the user
    # which of three options the user wants until the user gives a valid response
    # at which point it should call a script based on the users choice.
    # the choices are betweeen starting a new game, loading a saved game, and viewing the leaderboard
    global acceptedanswer
    askstring = "Would you like to start a [n]ew game, [l]oad a new game, or [v]iew the database "
    while not acceptedanswer:
        userchoice = input(askstring).lower()
        # above could be inproved by not having the program repeat itself after failed inputs
        check_responce(userchoice) #calls a function
    if userchoice == "n":
        print("calling new game script")
    elif userchoice == "l":
        print("calling load game script")
    elif userchoice == "v":
        print("calling leaderboard script")
    else:
        print("something went wrong")

# main
if __name__ == "__main__":
    accepted_answer = False
    ask_user()