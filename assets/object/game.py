# maps.py
import os
import msvcrt
import emoji
import pygame
import random
import time
from assets.event.fight import fight
from assets.event.game_state import gameoverscreen
from assets.object.spawn import spawn_mob, spawn_player
from assets.event.game_dialog import Alberic_dialog, Alberic_player_intro
from assets.object.items import Carte
from assets.play.controls import Controls
from assets.play.utils import move_in_pause_menu

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

def afficher_carte(map):
    os.system('cls' if os.name == 'nt' else 'clear')
    for row in map:
        print("".join(row))

def deplacer_joueur(direction,map,collision):
    global player_pos, monster_pos, monster_defait
    new_pos = player_pos.copy()

    if direction == Controls["up"]:  # Haut
        new_pos[0] -= 1
    elif direction == Controls["down"]:  # Bas
        new_pos[0] += 1
    elif direction == Controls["left"]:  # Gauche
        new_pos[1] -= 1
    elif direction == Controls["right"]:  # Droite
        new_pos[1] += 1

    if (0 <= new_pos[0] < len(map) and
            0 <= new_pos[1] < len(map[0]) and
            map[new_pos[0]][new_pos[1]] not in collision):
        map[player_pos[0]][player_pos[1]] = "  "
        player_pos = new_pos
        map[player_pos[0]][player_pos[1]] = " O"

        if player_pos[0] == 7 and monster_pos == None and monster_defait == False:
            monster_pos = [3, 11]
            map[monster_pos[0]][monster_pos[1]] = emoji.emojize("🧟 ")

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

        spawn_map[monster_pos[0]][monster_pos[1]] = emoji.emojize("🧟 ")

def deplacer_Alberic():
    global Alberic_pos
    if Alberic_pos:
        village_spawn_map[Alberic_pos[0]][Alberic_pos[1]] = "  "  

        # gestion des diagonales
        if Alberic_pos[0] < player_pos[0] and Alberic_pos[1] < player_pos[1]:  # si le joueur est en bas à droite de Alberic
            Alberic_pos[0] += 1
            village_spawn_map[Alberic_pos[0]][Alberic_pos[1]] = "🧙"
            return
        elif Alberic_pos[0] < player_pos[0] and Alberic_pos[1] > player_pos[1]:  # si le joueur est en bas à gauche de Alberic
            Alberic_pos[0] += 1
            village_spawn_map[Alberic_pos[0]][Alberic_pos[1]] = "🧙"
            return
        elif Alberic_pos[0] > player_pos[0] and Alberic_pos[1] < player_pos[1]:  # si le joueur est en haut à droite de Alberic
            Alberic_pos[0] -= 1
            village_spawn_map[Alberic_pos[0]][Alberic_pos[1]] = "🧙"
            return
        elif Alberic_pos[0] > player_pos[0] and Alberic_pos[1] > player_pos[1]:  # si le joueur est en haut à gauche de Alberic
            Alberic_pos[0] -= 1
            village_spawn_map[Alberic_pos[0]][Alberic_pos[1]] = "🧙"
            return

        if Alberic_pos[0] < player_pos[0]:  # si le joueur est en dessous de Alberic
            Alberic_pos[0] += 1
        elif Alberic_pos[0] > player_pos[0]:  # si le joueur est au dessus de Alberic
            Alberic_pos[0] -= 1
        if Alberic_pos[1] < player_pos[1]:  # si le joueur est à droite
            Alberic_pos[1] += 1
        elif Alberic_pos[1] > player_pos[1]:  # si le joueur est à gauche
            Alberic_pos[1] -= 1
        

        

        village_spawn_map[Alberic_pos[0]][Alberic_pos[1]] = "🧙"

def rdm_fight(taux_spawn): # A CHANGER LES MOBS
    rdm = random.randint(1, taux_spawn) 
    if rdm == 1:
        mob = random.randint(1, 4)
        if mob == 1:
            fight(spawn_player, spawn_mob)
            if spawn_player.hp <= 0:
                gameoverscreen()
                quit()
        elif mob == 2:
            fight(spawn_player, spawn_mob)
            if spawn_player.hp <= 0:
                gameoverscreen()
                quit()
        elif mob == 3:
            fight(spawn_player, spawn_mob)
            if spawn_player.hp <= 0:
                gameoverscreen()
                quit()
        elif mob == 4:
            fight(spawn_player, spawn_mob)
            if spawn_player.hp <= 0:
                gameoverscreen()
                quit()
    


def spawn() :
    global monster_pos, monster_defait, player_pos, tp_pos
    tp_pos = [[0,9],[0,10],[0, 11],[0,12],[0,13]]
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("./src/audio/spawn.wav")
    pygame.mixer.music.play(-1, 3.0)
    pygame.mixer.music.set_volume(0.2)
    while True:
        afficher_carte(spawn_map)
        key = msvcrt.getch().decode('utf-8')
        if key == Controls["exit"]:
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
                pygame.mixer.music.load("./src/audio/spawn.wav")
                pygame.mixer.music.play(-1, 3.0)
                pygame.mixer.music.set_volume(0.2)

        if player_pos in tp_pos:
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
    tp_pos = [[0,9],[0,10],[0, 11],[0,12],[0,13]]
    while True:
        afficher_carte(spawn_next_map)
        afficher_carte(spawn_next_map)
        key = msvcrt.getch().decode('utf-8')
        if key == Controls["exit"]:
            quit()
        deplacer_joueur(key, spawn_next_map,collision_spawn_map)

        if player_pos in tp_pos:
            village_spawn()

village_spawn_map = [           # 23x16 
    ["🌲", "🌲", "🌲", "🌲", "🌲","🌲", "🌲", "🌲", "🌲",  "🌲", "  ","  ","  ",  "🌲", "🌲", "🌲", "🌲", "🌲", "🌲","🌲", "🌲", "🌲", "🌲"],
    ["🌲", "🌲", "🌲", "🌲", "🌲","🌲", "🌲", "🌲", "🌲", "  ", "  ","  ","  ", "  ", "🌲", "🌲", "🌲", "🌲", "🌲","🌲", "🌲", "🌲", "🌲"],
    ["🌲", "🌲", "  ", "  ", "  ","  ", "  ", "  ", "  ", "  ", "  ","  ","  ", "  ", "  ", "🌲", "🌲", "🌲", "🌲","🌲", "🌲", "🌲", "🌲"],
    ["🌲", "  ", "  ", "  ", "  ","  ", "  ", "  ", "  ", "  ", "  ","  ","  ", "  ", "  ", "  ", "  ", "🌲", "🌲","🌲", "🌲", "🌲", "🌲"],
    ["  ", "  ", "  ", "  ", "  ","  ", "  ", "  ", "  ", "  ", "  ","  ","  ", "  ", "  ", "  ", "  ", "  ", "🌲","🌲", "💼", "🌲", "🌲"],
    ["  ", "  ", "  ", "  ", "  ","  ", "  ", "  ", "  ", "  ", "  ","  ","  ", "  ", "  ", "  ", "  ", "  ", "🌲","🌲", "  ", "🌲", "🌲"],
    ["  ", "  ", "  ", "  ", "  ","  ", "  ", "  ", "  ", "  ", "  ","  ","  ", "  ", "  ", "  ", "  ", "  ", "🌲","🌲", "  ", "🌲", "🌲"],
    ["  ", "  ", "  ", "  ", "  ","  ", "  ", "  ", "  ", "  ", "  ","  ","  ", "  ", "  ", "  ", "  ", "  ", "🌲","🌲", "  ", "🌲", "🌲"],
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

collision_village_spawn_map = ["🌲","🧙","🌱","💼","📜"]

def village_spawn() :
    global player_pos, tp_pos, tp_pos2, Alberic_pos, Player
    player_pos = [15, 11]
    Alberic_pos = [7, 10]
    Player = spawn_player
    tp_pos = [[4,0], [5,0],[6,0],[7,0],[8,0],[9,0],[10,0],[11,0],[12,0]]
    tp_pos2 = [[0,10], [0,11], [0,12]]
    village_spawn_map[Alberic_pos[0]][Alberic_pos[1]] = "🧙"
    village_spawn_map[player_pos[0]][player_pos[1]] = " O"
    tombe_pos = [5,17]
    village_spawn_map[tombe_pos[0]][tombe_pos[1]] = "📜"
    while True:
        afficher_carte(village_spawn_map)
        while True:
            afficher_carte(village_spawn_map)
            key = msvcrt.getch().decode('utf-8')
            if key == Controls["exit"]:
                move_in_pause_menu()
            if key == Controls["map"]:
                Player.inventory.use(Carte)
                afficher_carte(village_spawn_map)
            if key == Controls["inventory"]:
                Player.inventory.show()
                afficher_carte(village_spawn_map)

            deplacer_joueur(key, village_spawn_map,collision_village_spawn_map)

            if (village_spawn_map[Alberic_pos[0]-1][Alberic_pos[1]] == village_spawn_map[player_pos[0]][player_pos[1]] or village_spawn_map[Alberic_pos[0]+1][Alberic_pos[1]] == village_spawn_map[player_pos[0]][player_pos[1]] or village_spawn_map[Alberic_pos[0]][Alberic_pos[1]-1] == village_spawn_map[player_pos[0]][player_pos[1]] or village_spawn_map[Alberic_pos[0]][Alberic_pos[1]+1] == village_spawn_map[player_pos[0]][player_pos[1]]) and key == Controls["interact"]:
                if Player == spawn_player:
                    Alberic_dialog("village_spawn_map")
                    pygame.mixer.music.load("./src/audio/spawn.wav")
                    pygame.mixer.music.play(-1, 3.0)
                    pygame.mixer.music.set_volume(0.2)
                    for i in range(4):
                        afficher_carte(village_spawn_map)
                        key = msvcrt.getch().decode('utf-8')
                        if key == Controls["exit"]:
                            move_in_pause_menu()
                        deplacer_joueur(key, village_spawn_map,collision_village_spawn_map)
                    while (village_spawn_map[Alberic_pos[0]-1][Alberic_pos[1]] != village_spawn_map[player_pos[0]][player_pos[1]] and village_spawn_map[Alberic_pos[0]+1][Alberic_pos[1]] != village_spawn_map[player_pos[0]][player_pos[1]] and village_spawn_map[Alberic_pos[0]][Alberic_pos[1]-1] != village_spawn_map[player_pos[0]][player_pos[1]] and village_spawn_map[Alberic_pos[0]][Alberic_pos[1]+1] != village_spawn_map[player_pos[0]][player_pos[1]]):
                        deplacer_Alberic()
                        afficher_carte(village_spawn_map)
                        time.sleep(1)
                    Player = Alberic_player_intro()
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load("./src/audio/spawn.wav")
                    pygame.mixer.music.play(-1, 3.0)
                    pygame.mixer.music.set_volume(0.2)
                else:
                    Alberic_dialog("village_spawn_map2")
                    pygame.mixer.music.load("./src/audio/spawn.wav")
                    pygame.mixer.music.play(-1, 3.0)
                    pygame.mixer.music.set_volume(0.2)
            
            if village_spawn_map[player_pos[0]][player_pos[1]+1]=="🌱" and key == Controls["interact"]:
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

            if village_spawn_map[player_pos[0]-1][player_pos[1]]=="💼" and key == Controls["interact"]:
                print("Vous avez trouvé une carte")
                time.sleep(1)

            if (village_spawn_map[tombe_pos[0]-1][tombe_pos[1]]==village_spawn_map[player_pos[0]][player_pos[1]]or village_spawn_map[tombe_pos[0]+1][tombe_pos[1]]==village_spawn_map[player_pos[0]][player_pos[1]]or village_spawn_map[tombe_pos[0]][tombe_pos[1]-1]==village_spawn_map[player_pos[0]][player_pos[1]]) and key == Controls["interact"]:
                print("Il y a un panneau devant vous, voulez vous le lire ? (y/n)")
                if input() == "y":
                    print("") # LORE A RACONTER ICI AVEC CONDITION CONTINUER DE LIRE 
                    time.sleep(1)


            if player_pos in tp_pos:
                if Player == spawn_player:
                    afficher_carte(village_spawn_map)
                    print("Il est encore trop tôt pour partir")   
                    time.sleep(1)
                    village_spawn_map[player_pos[0]][player_pos[1]] = "  "
                    player_pos = [player_pos[0], player_pos[1]+1]
                    village_spawn_map[player_pos[0]][player_pos[1]] = " O"
                    afficher_carte(village_spawn_map)       
            if  player_pos in tp_pos2:
                if Player == spawn_player:
                    afficher_carte(village_spawn_map)
                    print("Il est encore trop tôt pour partir")           
                    time.sleep(1)
                    village_spawn_map[player_pos[0]][player_pos[1]] = "  "
                    player_pos = [player_pos[0]+1,player_pos[1]]
                    village_spawn_map[player_pos[0]][player_pos[1]] = " O"
                    afficher_carte(village_spawn_map)