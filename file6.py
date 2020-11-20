"""
    Author: Hayden Hopkinson
    Date: 20/11/2020
    Description: this component should display the data stored in the database
    version: 1.
    improvements from last version:
"""

# libraries
import sys
from pythonFiles import file1_1_3
# functions


def ask_filter():
    print("do you want to display [a]ll stats, [c]ombat stats, or the [s]core of players: ")
    answer = check_input()
    if answer == "a":
        display_all()
    elif answer == "c":
        display_combat()
    elif answer == "s":
        display_score()
    else:
        print("something went wrong")
    end_program()


def check_input():
    possible = ["a", "c", "s"]
    accepted = False
    while not accepted:
        inp = input()
        inp = inp.lower()
        if inp in possible:
            accepted = True
            return inp
        else:
            print("invalid input, please enter a, s or c")


def display_all():
    display = ["username:", "max_hp:", "min_damage:", "max_damage:", "armor:", "gold:"]
    if ask_sort():
        query = """
        SELECT players.username, stats.max_hp, stats.min_damage, stats.max_damage, stats.armor, stats.gold
        FROM players
        INNER JOIN stats ON players.rowid = stats.player_id
        ORDER BY stats.gold DESC
        """
    else:
        query = """
        SELECT players.username, stats.max_hp, stats.min_damage, stats.max_damage, stats.armor, stats.gold
        FROM players
        INNER JOIN stats ON players.rowid = stats.player_id
        """
    results = check_database(query)
    print(display)
    for i in results:
        print(i)


def display_combat():
    display = ["username:", "max_hp:", "min_damage:", "max_damage:", "armor:"]
    query = """
    SELECT players.username, stats.max_hp, stats.min_damage, stats.max_damage, stats.armor, stats.gold
    FROM players
    INNER JOIN stats ON players.rowid = stats.player_id
    """
    results = check_database(query)
    print(display)
    for i in results:
        print(i)


def display_score():
    display = ["username:", "gold:"]
    query = """
            SELECT players.username, stats.gold
            FROM players
            INNER JOIN stats ON players.rowid = stats.player_id
            ORDER BY stats.gold DESC
            """
    results = check_database(query)
    print(display)
    for i in results:
        print(i)


def ask_sort():
    sort_type = None
    while sort_type is None:
        sort_type = input("would you like your data to be filtered by [1] score or [2] time created: ")
        sort_type = int(sort_type)
        accepted = [1, 2]
        if sort_type in accepted:
            if sort_type == 1:
                return True
            else:
                return False
        else:
            print("invalid input")
            sort_type = None


def check_database(query, con=file1_1_3.connect_to_database()):
    cursor = con.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    con.commit()
    con.close()
    return results


def end_program():
    """ after the stats are displayed if the program continues it will error because of how it has been built,
    so instead this function is called witch will end the process"""
    sys.exit()
# main


if __name__ == "__main__":
    ask_filter()