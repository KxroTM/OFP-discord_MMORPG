# maps.py
import os
import msvcrt
import emoji
import pygame
import time
from assets.event.fight import fight
from assets.event.game_state import gameoverscreen
from assets.object.spawn import spawn_mob, spawn_player
from assets.event.game_dialog import Alberic_dialog

global Player
Player = spawn_player

spawn_map = [           # 23x16
    ["🌲", "🌲", "🌲", "🌲", "🌲","🌲", "🌲", "🌲", "🌲", "  ", "  ","  ","  ", "  ", "🌲", "🌲", "🌲", "🌲", "🌲","🌲", "🌲", "🌲", "🌲"],
    ["🌲", "🌲", "🌲", "🌲", "🌲","🌲", "🌲", "🌲", "  ", "  ", "  ","  ","  ", "  ", "  ", "🌲", "🌲", "🌲", "🌲","🌲", "🌲", "🌲", "🌲"], 
    ["🌲", "🌲", "🌲","🌲", "🌲", "🌲", "  ", "  ", "  ","  ", "  ", "  ","  ", "  ","  ", "  ", "  ", "🌲", "🌲", "🌲","🌲", "🌲", "🌲"],
    ["🌲", "🌲", "🌲","🌲", "🌲", "  ", "  ", "  ","  ", "  ", "  ", "  ", "  ","  ","  ", "  ", "  ", "  ", "🌲","🌲", "🌲", "🌲", "🌲"],
    ["🌲","🌲", "🌲", "🌲", "  ", "  ", "  ", "  ","  ", "  ", "  ", "  ", "  ","  ","  ", "  ", "  ", "  ", "  ", "🌲", "🌲","🌲", "🌲"],
    ["🌲","🌲", "🌲", "🌲", "  ", "  ", "  ", "  ","  ", "  ", "  ", "  ","  ","  ", "  ","  ", "  ", "  ", "  ", "🌲", "🌲","🌲", "🌲"],
    ["🌲","🌲", "🌲", "🌲", "  ", "  ", "  ", "  ","  ", "  ", "  ", "  ", "  ","  ","  ", "  ", "  ", "  ", "  ", "🌲", "🌲","🌲", "🌲"],
    ["🌲","🌲", "🌲", "🌲", "  ", "  ", "  ", "  ","  ", "  ", "  ", "  ", "  ","  ","  ", "  ", "  ", "  ", "  ", "🌲", "🌲","🌲", "🌲"],
    ["🌲","🌲", "🌲", "🌲", "  ", "  ", "  ", "  ","  ", "  ", "  ", "  ", "  ","  ","  ", "  ", "  ", "  ", "  ", "🌲", "🌲","🌲", "🌲"],
    ["🌲","🌲", "🌲", "🌲", "  ", "  ", "  ", "  ","  ", "  ", "  ", "  ", "  ","  ","  ", "  ", "  ", "  ", "  ", "🌲", "🌲","🌲", "🌲"],
    ["🌲", "🌲","🌲", "🌲", "  ", "  ", "  ", "  ","  ", "  ", "  ", "  ","  ", "  ","  ", "  ", "  ", "  ", "  ", "🌲", "🌲","🌲", "🌲"],
    ["🌲", "🌲","🌲", "🌲", "  ", "  ", "  ", "  ","  ", "  ", "  ", "  ", "  ","  ","  ", "  ", "  ", "  ", "  ", "🌲", "🌲","🌲", "🌲"],
    ["🌲", "🌲","🌲", "🌲", "🌲", "  ", "  ", "  ","  ", "  ", "  ", "  ","  ", "  ","  ", "  ", "  ", "🌲", "🌲", "🌲","🌲", "🌲", "🌲"],
    ["🌲", "🌲", "🌲", "🌲", "🌲", "🌲", "🌲","🌲", "🌲", "🌲", "🌲", "🌲", "🌲", "🌲","🌲", "🌲","🌲", "🌲", "🌲", "🌲", "🌲", "🌲", "🌲"],
    ["🌲", "🌲", "🌲", "🌲", "🌲", "🌲", "🌲","🌲", "🌲", "🌲", "🌲", "🌲", "🌲", "🌲","🌲", "🌲","🌲", "🌲", "🌲", "🌲", "🌲", "🌲", "🌲"],
    ["🌲", "🌲", "🌲", "🌲", "🌲", "🌲", "🌲","🌲", "🌲", "🌲", "🌲", "🌲", "🌲", "🌲", "🌲","🌲","🌲", "🌲", "🌲", "🌲", "🌲", "🌲", "🌲"], 
]
collision_spawn_map = ["🌲"]


player_pos = [10, 11]
spawn_map[player_pos[0]][player_pos[1]] = " O"
monster_pos = None
monster_defait = False
tp_pos = [0, 11] 

def afficher_carte(map):
    os.system('cls' if os.name == 'nt' else 'clear')
    for row in map:
        print("".join(row))

def deplacer_joueur(direction,map,collision):
    global player_pos, monster_pos, monster_defait
    new_pos = player_pos.copy()

    if direction == "z":  # Haut
        new_pos[0] -= 1
    elif direction == "s":  # Bas
        new_pos[0] += 1
    elif direction == "q":  # Gauche
        new_pos[1] -= 1
    elif direction == "d":  # Droite
        new_pos[1] += 1

    if (0 <= new_pos[0] < len(map) and
            0 <= new_pos[1] < len(map[0]) and
            map[new_pos[0]][new_pos[1]] not in collision):
        map[player_pos[0]][player_pos[1]] = "  "
        player_pos = new_pos
        map[player_pos[0]][player_pos[1]] = " O"

        if player_pos[0] == 7 and monster_pos == None and monster_defait == False:
            monster_pos = [3, 11]
            map[monster_pos[0]][monster_pos[1]] = emoji.emojize(":troll: ")

def deplacer_monstre():
    global monster_pos
    if monster_pos:
        spawn_map[monster_pos[0]][monster_pos[1]] = "  "  

        if monster_pos[0] < player_pos[0]:  # Descendre
            monster_pos[0] += 1
        elif monster_pos[0] > player_pos[0]:  # Monter
            monster_pos[0] -= 1
        if monster_pos[1] < player_pos[1]:  # Aller à droite
            monster_pos[1] += 1
        elif monster_pos[1] > player_pos[1]:  # Aller à gauche
            monster_pos[1] -= 1

        spawn_map[monster_pos[0]][monster_pos[1]] = emoji.emojize(":troll: ")


def spawn() :
    global monster_pos
    global monster_defait
    while True:
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load("./src/audio/spawn.wav")
        pygame.mixer.music.play(-1, 3.0)
        pygame.mixer.music.set_volume(0.2)
        afficher_carte(spawn_map)
        while monster_pos != player_pos and tp_pos != player_pos:
            afficher_carte(spawn_map)
            key = msvcrt.getch().decode('utf-8')
            if key == 'm':
                exit()
            deplacer_joueur(key, spawn_map,collision_spawn_map)
            deplacer_monstre()
        if monster_pos == player_pos:
            pygame.mixer.music.stop()
            fight(spawn_player, spawn_mob)
            if spawn_player.hp <= 0:
                gameoverscreen()
                quit()
            else:
                spawn_map[monster_pos[0]][monster_pos[1]] = "  "
                monster_defait = True
                monster_pos = None
                afficher_carte(spawn_map)
                continue

        if tp_pos == player_pos:
            spawn_nextmap()
            

spawn_next_map = [           # 23x16
    ["🌲", "🌲", "🌲", "🌲", "🌲","🌲", "🌲", "🌲", "🌲", "  ", "  ","  ","  ", "  ", "🌲", "🌲", "🌲", "🌲", "🌲","🌲", "🌲", "🌲", "🌲"],
    ["🌲", "🌲", "🌲", "🌲", "🌲","🌲", "🌲", "🌲", "🌲", "  ", "  ","  ","  ", "  ", "🌲", "🌲", "🌲", "🌲", "🌲","🌲", "🌲", "🌲", "🌲"],
    ["🌲", "🌲", "🌲", "🌲", "🌲","🌲", "🌲", "🌲", "🌲", "  ", "  ","  ","  ", "  ", "🌲", "🌲", "🌲", "🌲", "🌲","🌲", "🌲", "🌲", "🌲"],
    ["🌲", "🌲", "🌲", "🌲", "🌲","🌲", "🌲", "🌲", "🌲", "  ", "  ","  ","  ", "  ", "🌲", "🌲", "🌲", "🌲", "🌲","🌲", "🌲", "🌲", "🌲"],
    ["🌲", "🌲", "🌲", "🌲", "🌲","🌲", "🌲", "🌲", "🌲", "  ", "  ","  ","  ", "  ", "🌲", "🌲", "🌲", "🌲", "🌲","🌲", "🌲", "🌲", "🌲"],
    ["🌲", "🌲", "🌲", "🌲", "🌲","🌲", "🌲", "🌲", "🌲", "  ", "  ","  ","  ", "  ", "🌲", "🌲", "🌲", "🌲", "🌲","🌲", "🌲", "🌲", "🌲"],
    ["🌲", "🌲", "🌲", "🌲", "🌲","🌲", "🌲", "🌲", "🌲", "  ", "  ","  ","  ", "  ", "🌲", "🌲", "🌲", "🌲", "🌲","🌲", "🌲", "🌲", "🌲"],
    ["🌲", "🌲", "🌲", "🌲", "🌲","🌲", "🌲", "🌲", "🌲", "  ", "  ","  ","  ", "  ", "🌲", "🌲", "🌲", "🌲", "🌲","🌲", "🌲", "🌲", "🌲"],
    ["🌲", "🌲", "🌲", "🌲", "🌲","🌲", "🌲", "🌲", "🌲", "  ", "  ","  ","  ", "  ", "🌲", "🌲", "🌲", "🌲", "🌲","🌲", "🌲", "🌲", "🌲"],
    ["🌲", "🌲", "🌲", "🌲", "🌲","🌲", "🌲", "🌲", "🌲", "  ", "  ","  ","  ", "  ", "🌲", "🌲", "🌲", "🌲", "🌲","🌲", "🌲", "🌲", "🌲"],
    ["🌲", "🌲", "🌲", "🌲", "🌲","🌲", "🌲", "🌲", "🌲", "  ", "  ","  ","  ", "  ", "🌲", "🌲", "🌲", "🌲", "🌲","🌲", "🌲", "🌲", "🌲"],
    ["🌲", "🌲", "🌲", "🌲", "🌲","🌲", "🌲", "🌲", "🌲", "  ", "  ","  ","  ", "  ", "🌲", "🌲", "🌲", "🌲", "🌲","🌲", "🌲", "🌲", "🌲"],
    ["🌲", "🌲", "🌲", "🌲", "🌲","🌲", "🌲", "🌲", "🌲", "  ", "  ","  ","  ", "  ", "🌲", "🌲", "🌲", "🌲", "🌲","🌲", "🌲", "🌲", "🌲"],
    ["🌲", "🌲", "🌲", "🌲", "🌲","🌲", "🌲", "🌲", "🌲", "  ", "  ","  ","  ", "  ", "🌲", "🌲", "🌲", "🌲", "🌲","🌲", "🌲", "🌲", "🌲"],
    ["🌲", "🌲", "🌲", "🌲", "🌲","🌲", "🌲", "🌲", "🌲", "  ", "  ","  ","  ", "  ", "🌲", "🌲", "🌲", "🌲", "🌲","🌲", "🌲", "🌲", "🌲"],
    ["🌲", "🌲", "🌲", "🌲", "🌲","🌲", "🌲", "🌲", "🌲", "  ", "  ","  ","  ", "  ", "🌲", "🌲", "🌲", "🌲", "🌲","🌲", "🌲", "🌲", "🌲"],
    ["🌲", "🌲", "🌲", "🌲", "🌲","🌲", "🌲", "🌲", "🌲", "  ", "  ","  ","  ", "  ", "🌲", "🌲", "🌲", "🌲", "🌲","🌲", "🌲", "🌲", "🌲"],
]

def spawn_nextmap() :
    global player_pos, tp_pos
    player_pos = [16, 11]
    spawn_next_map[player_pos[0]][player_pos[1]] = " O"
    tp_pos = [0, 11]
    while True:
        afficher_carte(spawn_next_map)
        while tp_pos != player_pos:
            afficher_carte(spawn_next_map)
            key = msvcrt.getch().decode('utf-8')
            if key == 'm':
                quit()
            deplacer_joueur(key, spawn_next_map,collision_spawn_map)

        if player_pos == tp_pos:
            village_spawn()






village_spawn_map = [           # 23x16 
    ["🌲", "🌲", "🌲", "🌲", "🌲","🌲", "🌲", "🌲", "🌲",  "🌲", "  ","  ","  ",  "🌲", "🌲", "🌲", "🌲", "🌲", "🌲","🌲", "🌲", "🌲", "🌲"],
    ["🌲", "🌲", "🌲", "🌲", "🌲","🌲", "🌲", "🌲", "🌲", "  ", "  ","  ","  ", "  ", "🌲", "🌲", "🌲", "🌲", "🌲","🌲", "🌲", "🌲", "🌲"],
    ["🌲", "🌲", "  ", "  ", "  ","  ", "  ", "  ", "  ", "  ", "  ","  ","  ", "  ", "  ", "🌲", "🌲", "🌲", "🌲","🌲", "🌲", "🌲", "🌲"],
    ["🌲", "  ", "  ", "  ", "  ","  ", "  ", "  ", "  ", "  ", "  ","  ","  ", "  ", "  ", "  ", "  ", "🌲", "🌲","🌲", "🌲", "🌲", "🌲"],
    ["  ", "  ", "  ", "  ", "  ","  ", "  ", "  ", "  ", "  ", "  ","  ","  ", "  ", "  ", "  ", "  ", "  ", "🌲","🌲", "💼", "🌲", "🌲"],
    ["  ", "  ", "  ", "  ", "  ","  ", "  ", "  ", "  ", "  ", "  ","  ","  ", "  ", "  ", "  ", "  ", "  ", "🌲","🌲", "  ", "🌲", "🌲"],
    ["  ", "  ", "  ", "  ", "  ","  ", "  ", "  ", "  ", "  ", "  ","  ","  ", "  ", "  ", "  ", "  ", "  ", "🌲","🌲", "  ", "🌲", "🌲"],
    [" ", "  ", "  ", "  ", "  ","  ", "  ", "  ", "  ", "  ", "🧙‍♂️","  ","  ", "  ", "  ", "  ", "  ", "  ", "🌲","🌲", "  ", "🌲", "🌲"],
    ["  ", "  ", "  ", "  ", "  ","  ", "  ", "  ", "  ", "  ", "  ","  ","  ", "  ", "  ", "  ", "  ", "  ", "🌲","🌲", "  ", "🌲", "🌲"],
    ["  ", "  ", "  ", "  ", "  ","  ", "  ", "  ", "  ", "  ", "  ","  ","  ", "  ", "  ", "  ", "  ", "🌲", "🌲","🌲", "  ", "🌲", "🌲"],
    ["  ", "  ", "  ", "  ", "  ","  ", "  ", "  ", "  ", "  ", "  ","  ","  ", "  ", "  ", "  ", "  ", "🌲", "🌲","🌲", "  ", "🌲", "🌲"],
    ["  ", "  ", "  ", "  ", "  ","  ", "  ", "  ", "  ", "  ", "  ","  ","  ", "  ", "  ", "  ", "  ", "🌲", "🌲","🌲", "  ", "🌲", "🌲"],
    ["  ", "  ", "  ", "  ", "  ","  ", "  ", "  ", "  ", "  ", "  ","  ","  ", "  ", "  ", "  ", "🌲", "🌲", "🌲","🌲", "  ", "🌲", "🌲"],
    ["🌲", "  ", "  ", "  ", "  ","  ", "  ", "  ", "  ", "  ", "  ","  ","  ", "  ", "  ", "  ", "🌲", "🌲", "🌲","  ", "  ", "🌲", "🌲"],
    ["🌲", "🌲", "🌲", "  ", "  ","  ", "  ", "  ", "  ", "  ", "  ","  ","  ", "  ", "  ", "  ", "🌲", "  ", "🌱","  ", "🌲", "🌲", "🌲"],
    ["🌲", "🌲", "🌲", "🌲", "  ","  ", "  ", "  ", "  ", "  ", "  ","  ","  ", "  ", "  ", "  ", "  ", "  ", "🌲","🌲", "🌲", "🌲", "🌲"],
    ["🌲", "🌲", "🌲", "🌲", "🌲","🌲", "🌲", "🌲", "🌲", "  ", "  ","  ","  ", "  ", "🌲", "🌲", "🌲", "🌲", "🌲","🌲", "🌲", "🌲", "🌲"],
]

collision_village_spawn_map = ["🌲","🧙‍♂️","🌱","💼"]

def village_spawn() :
    global player_pos, tp_pos, tp_pos2
    player_pos = [15, 11]
    tp_pos = [[0, 4], [0, 5],[0,6],[0,7],[0,8],[0,9],[0,10],[0,11],[0,12]]
    tp_pos2 = [[10, 0], [11, 0], [12, 0]]
    village_spawn_map[player_pos[0]][player_pos[1]] = " O"
    while True:
        afficher_carte(village_spawn_map)
        while True:
            afficher_carte(village_spawn_map)
            key = msvcrt.getch().decode('utf-8')
            if key == 'm':
                exit()
            deplacer_joueur(key, village_spawn_map,collision_village_spawn_map)

            if (village_spawn_map[player_pos[0]-1][player_pos[1]] == "🧙‍♂️" or village_spawn_map[player_pos[0]+1][player_pos[1]] == "🧙‍♂️" or village_spawn_map[player_pos[0]][player_pos[1]-1] == "🧙‍♂️" or village_spawn_map[player_pos[0]][player_pos[1]+1] == "🧙‍♂️") and key == "e":
                Alberic_dialog("village_spawn_map")
                pygame.mixer.music.stop()
                pygame.mixer.music.load("./src/audio/spawn.wav")
                pygame.mixer.music.play(-1, 3.0)
                pygame.mixer.music.set_volume(0.2)
                os.system('cls' if os.name == 'nt' else 'clear')
            
            if village_spawn_map[player_pos[0]][player_pos[1]+1]=="🌱" and key == "e":
                if Player == spawn_player:
                    print("Vous n'avez pas d'objet pour couper cette arbuste, revenez plus tard")
                    time.sleep(1)
                elif "" in Player.inventory.items :
                    village_spawn_map[18,13] = "  "
                    print("Vous avez coupé l'arbuste")
                    time.sleep(1)
                else:
                    print("Vous n'avez pas d'objet pour couper cette arbuste")
                    time.sleep(1)
            
            if player_pos in tp_pos:
                print("Vous avez trouvé un passage secret vers la map suivante") 
                time.sleep(1)               
            if  player_pos in tp_pos2:
                print("Vous avez trouvé un passage secret") 
                time.sleep(1)               