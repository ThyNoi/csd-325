# Eric Sengvanhpheng
# June 12, 2026
# Advanced Python Module 2.2

import random

print("You encounter an enemy")

# attack function with passed variables
def attacking_main(enemy_health, player_attack):
    print (f"The enemy has {enemy_health} health")
    enemy_health -= random.randint(player_attack, player_attack + 10)
    print(f"Attacked the enemy and now they have {enemy_health} health")
    return enemy_health

# variables
enemy_health = 100
player_attack = 10

# get return, updates variable and call function
enemy_health = attacking_main(enemy_health, player_attack)
print()
print(f"Enemy health outside function: {enemy_health}")

