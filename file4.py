"""
    Author: Hayden Hopkinson
    Date: 3/10/2020
    Description: this will be the main battle system that will loop over itself while in a battle
    until one of the battlers runs out of health
    version: 1.
    improvements from last version:
"""

# libraries
import random, time
from pythonFiles import file4_1, file9
# functions


def player_turn(enemy_health, enemy_name, player_stats, enemy_armor):
    print("""What do you wish to do with your turn?
You can choose to attack, or heal yourself if you have any health potions remaining""")
    print("you have {} health potion(s) remaining".format(player_stats[5]))
    global loop
    loop = True
    while loop:
        player_move = input("do you [a]ttack, or [h]eal: ")
        player_move = player_move.lower()
        if player_move == "a" or player_move == "attack":
            player_damage = random.randint(player_stats[1], player_stats[2])**2 // enemy_armor
            if random.randint(1,15) == 1:
                player_damage = player_damage * 2
                print("Lucky you! you got a crit")
            enemy_health = enemy_health - player_damage
            print("you hit the {} dealing {} damage to it, leaving it with {} health".format(enemy_name, player_damage, enemy_health))
            loop = False
            return True, enemy_health
        elif (player_move == "h" or player_move == "heal") and player_stats[5] > 0:
            heal_amount = random.randint(player_stats[1], player_stats[2]) * 3
            loop = False
            return False, heal_amount
        else:
            print("You dont have any health potions, or you entered an invalid response")


def battle(player_stats, enemy_stats, enemy_name, difficulty):
    current_player_health = player_stats[0]
    current_enemy_health = enemy_stats[0]
    is_player_turn = random.randint(0, 1)
    if not is_player_turn:
        current_player_health = enemy_attacks(current_player_health, enemy_name, enemy_stats, player_stats[3])
        is_player_turn = True
    while current_enemy_health > 0 and current_player_health > 0:
        print("""
current player health: {}
current enemy health: {}
        """.format(current_player_health, current_enemy_health))
        if is_player_turn:
            time.sleep(1)
            what_player_did = player_turn(current_enemy_health, enemy_name, player_stats, enemy_stats[3])
            if what_player_did[0]:
                current_enemy_health = what_player_did[1]
            elif not what_player_did[0]:
                current_player_health = current_player_health + what_player_did[1]
                print("You healed for {} bringing your total health to {}".format(what_player_did[1], current_player_health))
                player_stats[5] = player_stats[5] - 1
            is_player_turn = False
        else:
            time.sleep(1)
            current_player_health = enemy_attacks(current_player_health, enemy_name, enemy_stats, player_stats[3])
            is_player_turn = True
        file9.clear()
    if current_enemy_health < 1:
        return file4_1.loot_drops(difficulty, player_stats, enemy_stats[5], enemy_stats[4])
    else:
        return file4_1.player_loss(difficulty, player_stats, enemy_name)


def enemy_attacks(player_health, enemy_name, enemy_stats, player_armor):
    enemy_damage = random.randint(enemy_stats[1], enemy_stats[2])**2 // player_armor
    player_health = player_health - enemy_damage
    print("the {} hits you dealing {} damage, bringing you to {} health".format(enemy_name, enemy_damage, player_health))
    return player_health


# main
loop = True
if __name__ == "__main__":
    battle([100, 20, 50, 10, 50, 3], (100, 10, 15, 10, 1, 50), "test enemy", 5)

# player stats are max hp, min damage, max damage, armor, gold, health potions available
# enemy stats are max hp, min damage, max damage, armor, min gold dropped, max gold dropped