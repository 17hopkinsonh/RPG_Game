"""
    Author: Hayden Hopkinson
    Date: 15/09/2020
    Description: this file should update a players information in the database
    version: 1.
    improvements from last version:
"""

# libraries
import sqlite3
import sys


# functions


def save_game(user_id, player_stats, con=sqlite3.connect("database.db")):
    stats = player_stats
    stats.append(user_id)
    print(stats)
    cursor = con.cursor()
    user_id = str(user_id)
    cursor.execute("DELETE FROM stats WHERE player_id=?", (user_id,))
    cursor.execute("INSERT INTO stats values(?,?,?,?,?,?,?)", stats)
    con.commit()
    con.close()
    print("The game has been saved, note that when you play next you will be put back to spawn")
    stop_player()

def stop_player():
    """
    after saving the game it has a chance to mess up if there are multiple players in the database, the most easy way
    to fix this is by having the game stop and the player have to restart the program and load from where they left off
    if they wish to continue playing
    """
    sys.exit()

# main

if __name__ == "__main__":
    print("")