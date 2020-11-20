"""
    Author: Hayden Hopkinson
    Date: 15/09/2020
    Description:
    version: 1.
    improvements from last version:
"""

# libraries
import random
# functions


def loot_drops(difficulty, current_player_stats, max_gold, min_gold):
    """
    the function that will increase the users stats when the player wins a battle,
    the values taken are an int of the tiles difficulty and a list of the players stats
    this returns the updated player stats
    """

    # did the enemy drop max damage?
    if random.randint(1,7) <= difficulty:
        max_dropped = random.randint(1, difficulty) * 5 * difficulty
        current_player_stats[2] = current_player_stats[2] + max_dropped
        print("the enemy dropped " + str(max_dropped) + " extra max damage")
        print("bringing your max damage to " + str(current_player_stats[2]))

    # did the enemy drop max health?

    if random.randint(1,7) <= difficulty:
        health_dropped = (random.randint(1, difficulty) + difficulty)**2
        current_player_stats[0] = current_player_stats[0] + health_dropped
        print("the enemy dropped " + str(health_dropped) + " extra max health")
        print("bringing your max health to " + str(current_player_stats[0]))

    # did the enemy drop armor?
    if random.randint(1, 7) <= difficulty:
        armor_dropped = random.randint(1, difficulty)
        current_player_stats[3] = current_player_stats[3] + armor_dropped
        print("the enemy dropped " + str(armor_dropped) + " extra armor points")
        print("bringing your armor to " + str(current_player_stats[3]))

    # did the enemy drop health potions
    if random.randint(1,7) <= difficulty:
        potions_dropped = difficulty
        current_player_stats[5] = current_player_stats[5] + potions_dropped
        print("the enemy dropped " + str(potions_dropped) + " health potions")
        print("you now have " + str(current_player_stats[5]) + " health potion(s)")

    # how much gold did the enemy drop?
    gold_dropped = random.randint(min_gold, max_gold)
    print("the enemy had", gold_dropped, " gold on him, you add it to your old pile of", current_player_stats[4], "gold")
    current_player_stats[4] = current_player_stats[4] + gold_dropped
    return current_player_stats


def player_loss(difficulty, current_player_stats, enemy_name):
    gold_dropped = (current_player_stats[4]//7) * difficulty
    print("you were defeated by the", enemy_name, ". You dropped", gold_dropped, " while running away from it")
    current_player_stats[4] = current_player_stats[4] - gold_dropped
    return current_player_stats

# main

if __name__ == "__main__":
    print("")