from typing import Tuple
import random

def fight_monster(health: int, number_of_monsters: int) -> Tuple[int, int]:
    """Fight a monster and potentionally lose health

    :param health: The current health of the player.
    :param number_of_monsters: The number of monsters in the world.
    :return: A tuple containing the new health and the new number of monsters in the world.
    """
    print(f"[[ Fight monster called with {health} health and {number_of_monsters} monsters ]]")
    monsters = {
        "🐏": 0,
        "🦂": 5,
        "🕷️": 5,
        "🐉": 20,
        "👽": 10 ## VOEG HIER EEN EXTRA MONSTER TOE 🧛‍♂️, 🤡, 💩, 🐬, 🐸, 🦄 ...
    }
    monster, damage = random.choice(list(monsters.items()))
    print(f"🪄: You're fighting {monster} and it damages you {damage} HP")

    return health - damage, number_of_monsters - 1

# def drink_potion(health: int, number_of_potions: int) -> Tuple[int, int]:
#     """Drink a potion to regain health.
#
#     :param health: The current health of the player.
#     :param number_of_potions: The number of potions the player has.
#     :return: A tuple containing the new health and the new number of potions.
#     """
#     print(f"[[ Drink potion called with {health} health and {number_of_potions} potions ]]")
#     if number_of_potions == XXX:
#         print("🪄: You are out of potions")
#         return health, number_of_potions
#     else:
#         potion_hp = 3
#         new_number_of_potions = number_of_potions - XXX
#         new_health = health + potion_hp
#         print(f"🪄: HP went up with {potion_hp}")
#         return XXX, XXX
#
# def cast_spell(number_of_monsters: int) -> int:
#     """Cast a spell in order to half or double the number of monsters in the world
#
#     :param number_of_monsters: The number of monsters in the world.
#     :return: the new number of monsters in the world.
#     """
#     print(f"[[ Cast spell called with {number_of_monsters} monsters ]]")
#     if random.random() < 0.5:
#         print(F"🪄: ☄️ IT WORKS! ☄️ MONSTERS HALVED")
#         XXX
#     else:
#         print(f"🪄: 😰️ UHOH YOU SCREWED UP! 😰️. MONSTERS DOUBLED")
#         XXX

def calculate_score(health: int, number_of_potions: int) -> int:
    """Calculate the score of the game.

    :param health: The health of the player
    :param number_of_potions: The number of potions the player has
    :return: the calculated score of the user
    """
    print(f"[[ Calculate score called with {health} health and {number_of_potions} potions ]]")
    return health + (number_of_potions * 3)