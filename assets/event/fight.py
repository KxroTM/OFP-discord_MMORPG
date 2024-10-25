# fight.py

import pygame

import os
import time

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


        if choice == "1":
            player.attack(mob)
            time.sleep(1)

        elif choice == "2":
            player.use_inventory()
            time.sleep(1)
            
        elif choice == "3":
            if player.flee(mob) == True:
                print(f"{player.name} ran away.")
                time.sleep(1)
                break
            else:
                print(f"{player.name} failed to run away.")
                time.sleep(1)
        else:
            print("Invalid choice.")
            continue

        if mob.hp <= 0:
            print(f"{mob.name} is dead.")
            time.sleep(1)

            pygame.mixer.music.stop()
            break

        mob.attack(player)
        time.sleep(1)

    pygame.mixer.music.stop()
