"""
    Author: Hayden Hopkinson
    Date: 13/10/2020
    Description: takes the username and password from the previos components and adds them to the database
    version: 1.
    improvements from last version: N/A
"""

# libraries
import sqlite3
# functions


def connect_to_database():
    con = None
    database_file = "database.db"

    try:
        con = sqlite3.connect(database_file)
    except sqlite3.Error as e:
        print(e)
    return con


def create_database_credentials(con):
    cursor = con.cursor()
    cursor.execute("""
    CREATE TABLE players(
    username DATATYPE text,
    password DATATYPE text
        )""")
    con.commit()
    con.close()


def create_database_stats(con):
    cursor = con.cursor()
    cursor.execute("""
    CREATE TABLE stats(
    max_hp DATATYPE integer,
    min_damage DATATYPE integer,
    max_damage DATATYPE integer,
    armor DATATYPE integer,
    gold DATATYPE integer,
    health_potion DATATYPE integer,
    player_id DATATYPE integer
        )
    """)
    con.commit()
    con.close()


def add_credential_database(con, username, password):
    cursor = con.cursor()
    values = [(username, password)]
    cursor.executemany("INSERT INTO players values(?,?)", values)
    cursor.execute("SELECT rowid FROM players")
    length = cursor.fetchall()
    add_stats_database(con, int(length[-1][0]))
    con.commit()
    con.close()
    return int(length[-1][0])


def add_stats_database(con, rowid):
    cursor = con.cursor()
    stats = [(75, 5, 12, 1, 0, 1, rowid)]
    # player stats are max hp, min damage, max damage, armor, gold, health potions available
    cursor.executemany("INSERT INTO stats values(?,?,?,?,?,?,?)", stats)

def print_credential_database(con):
    cursor = con.cursor()
    cursor.execute("SELECT rowid,* FROM players")
    results = cursor.fetchall()
    con.commit()
    for i in results:
        print(i)

def print_stats_database(con):
    cursor = con.cursor()
    cursor.execute("SELECT * FROM stats")
    results = cursor.fetchall()
    con.commit()
    for i in results:
        print(i)

def get_user_stats(con):
    cursor = con.cursor
    cursor.execute("""
    SELECT max_hp
    FROM stats""")

# main

if __name__ == "__main__":
    #print_credential_database(connect_to_database())
    #print_stats_database(connect_to_database())
    create_database_credentials(connect_to_database())
    create_database_stats(connect_to_database())