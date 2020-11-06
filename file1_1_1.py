"""
    Author: Hayden Hopkinson
    Date: 17/09/2020
    Description: This will ask the user for their username, call a function from a different
    file to check it, then ask the user for their password, again calls a check from the other
    file, and finnaly will
    script
    version: 1.
    improvements from last version:
"""

# libraries
from pythonFiles import file1_1_2
# functions
def ask_username():
    accepted_username = None
    while accepted_username is None:
        test_username = input("Please enter your username: ")
        if file1_1_2.check_username(test_username):
            accepted_username = test_username
            return accepted_username

def ask_password():
    accepted_password = None
    while accepted_password is None:
        test_password = input("""Please enter your password,
it must have a capital and lowercase letter,
and be at least 5 in length: """)
        if file1_1_2.check_password(test_password):
            accepted_password = test_password
            return accepted_password
        else:
            print("there was an error in your password, please try again")



# main

if __name__ == "__main__":
    ask_username()