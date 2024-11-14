# fight.py

import pygame
from assets.classes.inventory import potion_hp, potion_force, potion_defense
import os
import time
import random

def fight(player, mob) :
    pygame.mixer.music.load("./src/audio/spawnfight.wav")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.2)
    while player.hp > 0:
        os.system('cls' if os.name == 'nt' else 'clear')

        print(f"Vous: {player.hp} HP                                     {mob.name}: {mob.hp} HP\n")
        for row in mob.image:
            print("".join(row))
        print("\n")
        print("1. Attaquer")
        print("2. Inventaire")
        print("3. Fuir \n")


        choice = input()

        while choice != "1" and choice != "2" and choice != "3":
            print("Choix invalide.")
            choice = input()


        if choice == "1":
            player.attack(mob)
            time.sleep(1)

        elif choice == "2":
            player.use_inventory(player)
            time.sleep(1)
            
        elif choice == "3":
            if player.flee(mob) == True:
                print(f"{player.name} a fuit.")
                time.sleep(1)
                break
            else:
                print(f"{player.name} n'a pas pu fuir.")
                time.sleep(1)


        if mob.hp <= 0:
            print(f"{mob.name} est \033[1mmort\033[0m.")
            time.sleep(1)
            drop_item(player)
            player.xp += mob.level
            player.level_up()
            pygame.mixer.music.stop()
            break

        if choice != "2":
            mob.attack(player)
            time.sleep(1)

    pygame.mixer.music.stop()


def drop_item(player):
    drop_rate = random.randint(1, 100)
    if drop_rate <= 30:
        rdm_item = random.randint(1, 100)
        if rdm_item <= 30:
            print(f"{player.name} a obtenu une potion de soin.")
            time.sleep(1)
            return player.inventory.add(potion_hp(name="Potion de soin 1"))
        elif rdm_item > 30 and rdm_item <= 60:
            print(f"{player.name} a obtenu une potion de force.")
            time.sleep(1)
            return player.inventory.add(potion_force(name="Potion de force 1"))
        elif rdm_item > 60 and rdm_item <= 90:
            print(f"{player.name} a obtenu une potion de défense.")
            time.sleep(1)
            return player.inventory.add(potion_defense(name="Potion de défense 1"))