"""
    Author: Hayden Hopkinson
    Date: 13/10/2020
    Description:takes the username and password from the previos components and adds them to the database
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

def create_database(con):
    cursor = con.cursor()
    cursor.execute("""
        CREATE TABLE players(
        username DATATYPE text,
        password DATATYPE text,
        armor DATATYPE integer,
        gold DATATYPE integer
        )
    """)
def add_database(con, username, password):
    cursor = con.cursor()
    values = [(username, password, 0, 0)]
    cursor.executemany("INSERT INTO players values(?,?,?,?)", values)
    con.commit()
    con.close()

def print_database(con):
    cursor = con.cursor()
    cursor.execute("SELECT rowid,* FROM players")
    results = cursor.fetchall()
    con.commit()
    for i in results:
        print(i)

# main

if __name__ == "__main__":
    print_database(connect_to_database())
