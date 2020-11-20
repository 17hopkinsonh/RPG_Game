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
    """
this should check the users input (the passed useranswer) against
a list of the inputs that are valid, if the answer is accepted
it should change a global variable that will break out of the loop that is calling this function
takes one paramiter, the user answer, it should be noted this should only be called by the ask_user function
    """

    global accepted_answer
    allowedresponses = ["n", "l", "v"] 	# the three different responses that are allowed,
    #  they repreasent new game, load game, and view the leaderboard
    if useranswer in allowedresponses:
        accepted_answer = True 	# setting accepted answer to something will break out of the loop that calls this function
        #return <-- check if needed
    else:
        print("your input was rejected, please type n, l, or v")

def ask_user():
    """
this should loop over script that asks the user
which of three options the user wants until the user gives a valid response
at which point it should call a script based on the users choice.
the choices are betweeen starting a new game, loading a saved game, and viewing the leaderboard
takes no paramaters and returns the accecpted user answer
    """

    askstring = "Would you like to start a [n]ew game, [l]oad a new game, or [v]iew the database: "
    global accepted_answer
    while accepted_answer is None:	# loop asking the user for a response until an accepted response is given
        userchoice = input(askstring).lower()	# this will store the lowercase version of the users answer to the question stored in  the variable askstring
        # above could be inproved by not having the program repeat itself after failed inputs
        check_responce(userchoice)	#calls a function to check if the choice was valid
    return userchoice

# main
accepted_answer = None 	# this variable stores a string input from the user which will be checked against a whitelist of accepted inputs
    #  this is declared here so it can be used in multiple functions as a global variable
if __name__ == "__main__":
    ask_user() 	# for testing purposes