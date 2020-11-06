"""
    Author: Hayden Hopkinson
    Date: 22/10/2020
    Description: this component should check a username and password provided against the database to find the user
    version: 2
    improvements from last version: this no longer encounters a bug if the user starts by entering the wrong credentials
"""

# libraries
from pythonFiles import file1_1_3
# functions

def ask_credentials():
    user_username = input("Please enter your username: ")
    user_password = input("Please enter your password: ")
    return check_credentials(user_username, user_password)

def check_credentials(username, password):
    if not check_database_credentials(file1_1_3.connect_to_database(), username, password):
        print("The username or password you entered was incorrect, please try again ")
        return ask_credentials()
    else:
        global user_id
        return user_id, username, password

def check_database_credentials(con, username, password):
    global user_id
    cursor = con.cursor()
    cursor.execute("""SELECT rowid
                   FROM players
                   WHERE username=:name AND password=:pass""", {"name": username, "pass": password})
    results = cursor.fetchone()
    user_id = results
    con.commit()
    if results is None:
        return False
    else:
        return True
# main
user_id = None
if __name__ == "__main__":
    print(ask_credentials())