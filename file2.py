"""
    Author: Hayden Hopkinson
    Date: 15/10/2020
    Description: this either sets the stats of a new user, or loads the stats of an existing user
    version: 1.
    improvements from last version:
"""

# libraries
from pythonFiles import file1_1_3
# functions

#this will set the stats of a new player
def set_stats():
    user_stats = [75, 5, 12, 3, 10, 1]
    return user_stats
    #the stats list contains the following stats in this order:
    #max hp, min damage, max damage, armor, gold, and health potions
    #the values above are the default stats that the game will give the user

def load_stats(user_id):
    return get_stats(file1_1_3.connect_to_database(), user_id)

def get_stats(con, user_id):
    cursor = con.cursor()
    cursor.execute("""
    SELECT armor, gold
    FROM players
    WHERE rowid=:user_id""", {"rowid": user_id})
    results = cursor.fetchone()
    con.commit()
    return results
# main

if __name__ == "__main__":
    print()
