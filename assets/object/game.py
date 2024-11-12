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
from assets.object.maps import caelid, route_1 , ravenshire

global Player
Player = spawn_player


def gamestart():
    global spawn_player
    spawn_player.coord = [10, 11]
    spawn()

def afficher_carte(map):
    os.system('cls' if os.name == 'nt' else 'clear')
    for row in map:
        print("".join(row))

def deplacer_joueur(direction,map):
    global spawn_player, monster_pos, monster_defait
    new_pos = spawn_player.coord.copy()

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
            map[new_pos[0]][new_pos[1]] not in map.collision):
        map[spawn_player.coord[0]][spawn_player.coord[1]] = "  "
        spawn_player.coord = new_pos
        map[spawn_player.coord[0]][spawn_player.coord[1]] = " O"

        if map == caelid.map:
            if spawn_player.coord[0] == 7 and monster_pos == None and monster_defait == False:
                monster_pos = [3, 11]
                map[monster_pos[0]][monster_pos[1]] = emoji.emojize("🧟 ")

def deplacer_monstre():
    global monster_pos
    if monster_pos:
        caelid.map[monster_pos[0]][monster_pos[1]] = "  "  

        if monster_pos[0] < spawn_player.coord[0]:  # Descendre
            monster_pos[0] += 1
        elif monster_pos[0] > spawn_player.coord[0]:  # Monter
            monster_pos[0] -= 1
        if monster_pos[1] < spawn_player.coord[1]:  # Aller à droite
            monster_pos[1] += 1
        elif monster_pos[1] > spawn_player.coord[1]:  # Aller à gauche
            monster_pos[1] -= 1

        caelid.map[monster_pos[0]][monster_pos[1]] = emoji.emojize("🧟 ")

def deplacer_Alberic():
    global Alberic_pos
    if Alberic_pos:
        ravenshire.map[Alberic_pos[0]][Alberic_pos[1]] = "  "  

        # gestion des diagonales
        if Alberic_pos[0] < spawn_player.coord[0] and Alberic_pos[1] < spawn_player.coord[1]:  # si le joueur est en bas à droite de Alberic
            Alberic_pos[0] += 1
            ravenshire.map[Alberic_pos[0]][Alberic_pos[1]] = "🧙"
            return
        elif Alberic_pos[0] < spawn_player.coord[0] and Alberic_pos[1] > spawn_player.coord[1]:  # si le joueur est en bas à gauche de Alberic
            Alberic_pos[0] += 1
            ravenshire.map[Alberic_pos[0]][Alberic_pos[1]] = "🧙"
            return
        elif Alberic_pos[0] > spawn_player.coord[0] and Alberic_pos[1] < spawn_player.coord[1]:  # si le joueur est en haut à droite de Alberic
            Alberic_pos[0] -= 1
            ravenshire.map[Alberic_pos[0]][Alberic_pos[1]] = "🧙"
            return
        elif Alberic_pos[0] > spawn_player.coord[0] and Alberic_pos[1] > spawn_player.coord[1]:  # si le joueur est en haut à gauche de Alberic
            Alberic_pos[0] -= 1
            ravenshire.map[Alberic_pos[0]][Alberic_pos[1]] = "🧙"
            return

        if Alberic_pos[0] < spawn_player.coord[0]:  # si le joueur est en dessous de Alberic
            Alberic_pos[0] += 1
        elif Alberic_pos[0] > spawn_player.coord[0]:  # si le joueur est au dessus de Alberic
            Alberic_pos[0] -= 1
        if Alberic_pos[1] < spawn_player.coord[1]:  # si le joueur est à droite
            Alberic_pos[1] += 1
        elif Alberic_pos[1] > spawn_player.coord[1]:  # si le joueur est à gauche
            Alberic_pos[1] -= 1
        
        ravenshire.map[Alberic_pos[0]][Alberic_pos[1]] = "🧙"

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
    global monster_pos, monster_defait, tp_pos
    caelid.map[spawn_player.coord[0]][spawn_player.coord[1]] = " O"
    monster_pos = None
    monster_defait = False
    tp_pos = [[0,9],[0,10],[0, 11],[0,12],[0,13]]
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("./src/audio/spawn.wav")
    pygame.mixer.music.play(-1, 3.0)
    pygame.mixer.music.set_volume(0.2)
    while True:
        afficher_carte(caelid.map)
        key = msvcrt.getch().decode('utf-8')
        if key == Controls["exit"]:
            move_in_pause_menu()
        if key == Controls["map"]:
            Player.inventory.use(Carte)
            afficher_carte(caelid.map)
        if key == Controls["inventory"]:
            Player.inventory.show()
            afficher_carte(caelid.map)
        deplacer_joueur(key, caelid.map)
        deplacer_monstre()
        if monster_pos == spawn_player.coord:
            pygame.mixer.music.stop()
            fight(spawn_player, spawn_mob)
            if spawn_player.hp <= 0:
                gameoverscreen()
                quit()
            else:
                caelid.map[monster_pos[0]][monster_pos[1]] = "  "
                monster_defait = True
                monster_pos = None
                afficher_carte(caelid.map)
                pygame.mixer.music.load("./src/audio/spawn.wav")
                pygame.mixer.music.play(-1, 3.0)
                pygame.mixer.music.set_volume(0.2)

        if spawn_player.coord in tp_pos:
            caelid.map[spawn_player.coord[0]][spawn_player.coord[1]] = "  "
            spawn_player.coord = [15, spawn_player.coord[1]]
            spawn_nextmap()           

def spawn_nextmap() :
    global spawn_player, tp_pos
    route_1.map[spawn_player.coord[0]][spawn_player.coord[1]] = " O"
    tp_pos = [[0,9],[0,10],[0, 11],[0,12],[0,13]]
    last_map_pos = [[16,9],[16,10],[16, 11],[16,12],[16,13]]
    collision_spawn_map = ["🌲"]
    while True:
        afficher_carte(route_1.map)
        key = msvcrt.getch().decode('utf-8')
        if key == Controls["exit"]:
            move_in_pause_menu()
        if key == Controls["map"]:
            Player.inventory.use(Carte)
            afficher_carte(route_1.map)
        if key == Controls["inventory"]:
            Player.inventory.show()
            afficher_carte(route_1.map)
        deplacer_joueur(key, route_1.map)

        if spawn_player.coord in tp_pos:
            route_1.map[spawn_player.coord[0]][spawn_player.coord[1]] = "  "
            spawn_player.coord = [15,spawn_player.coord[1]]
            village_spawn()
        
        if spawn_player.coord in last_map_pos:
            route_1.map[spawn_player.coord[0]][spawn_player.coord[1]] = "  "
            spawn_player.coord = [1,spawn_player.coord[1]]
            spawn()

def village_spawn(spawn=False) :
    global spawn_player, tp_pos, tp_pos2, Alberic_pos, Player
    if spawn == True:
        spawn_player.coord = [15, 11]
    Alberic_pos = [7, 10]
    Player = spawn_player
    tp_pos = [[4,0], [5,0],[6,0],[7,0],[8,0],[9,0],[10,0],[11,0],[12,0]]
    tp_pos2 = [[0,10], [0,11], [0,12]]
    last_map_pos = [[16, 9], [16, 11], [16, 12], [16, 13], [16, 10]]
    ravenshire.map[Alberic_pos[0]][Alberic_pos[1]] = "🧙"
    ravenshire.map[spawn_player.coord[0]][spawn_player.coord[1]] = " O"
    tombe_pos = [5,17]
    ravenshire.map[tombe_pos[0]][tombe_pos[1]] = "📜"
    while True:
        afficher_carte(ravenshire.map)
        while True:
            afficher_carte(ravenshire.map)
            key = msvcrt.getch().decode('utf-8')
            if key == Controls["exit"]:
                move_in_pause_menu()
            if key == Controls["map"]:
                Player.inventory.use(Carte)
                afficher_carte(ravenshire.map)
            if key == Controls["inventory"]:
                Player.inventory.show()
                afficher_carte(ravenshire.map)

            deplacer_joueur(key, ravenshire.map)

            if (ravenshire.map[Alberic_pos[0]-1][Alberic_pos[1]] == ravenshire.map[spawn_player.coord[0]][spawn_player.coord[1]] or ravenshire.map[Alberic_pos[0]+1][Alberic_pos[1]] == ravenshire.map[spawn_player.coord[0]][spawn_player.coord[1]] or ravenshire.map[Alberic_pos[0]][Alberic_pos[1]-1] == ravenshire.map[spawn_player.coord[0]][spawn_player.coord[1]] or ravenshire.map[Alberic_pos[0]][Alberic_pos[1]+1] == ravenshire.map[spawn_player.coord[0]][spawn_player.coord[1]]) and key == Controls["interact"]:
                if Player == spawn_player:
                    Alberic_dialog("ravenshire")
                    pygame.mixer.music.load("./src/audio/spawn.wav")
                    pygame.mixer.music.play(-1, 3.0)
                    pygame.mixer.music.set_volume(0.2)
                    for i in range(4):
                        afficher_carte(ravenshire.map)
                        key = msvcrt.getch().decode('utf-8')
                        if key == Controls["exit"]:
                            move_in_pause_menu()
                        deplacer_joueur(key, ravenshire.map)
                    while (ravenshire.map[Alberic_pos[0]-1][Alberic_pos[1]] != ravenshire.map[spawn_player.coord[0]][spawn_player.coord[1]] and ravenshire.map[Alberic_pos[0]+1][Alberic_pos[1]] != ravenshire.map[spawn_player.coord[0]][spawn_player.coord[1]] and ravenshire.map[Alberic_pos[0]][Alberic_pos[1]-1] != ravenshire.map[spawn_player.coord[0]][spawn_player.coord[1]] and ravenshire.map[Alberic_pos[0]][Alberic_pos[1]+1] != ravenshire.map[spawn_player.coord[0]][spawn_player.coord[1]]):
                        deplacer_Alberic()
                        afficher_carte(ravenshire.map)
                        time.sleep(1)
                    Player = Alberic_player_intro()
                    Player.coord = spawn_player.coord
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load("./src/audio/spawn.wav")
                    pygame.mixer.music.play(-1, 3.0)
                    pygame.mixer.music.set_volume(0.2)
                else:
                    Alberic_dialog("ravenshire2")
                    pygame.mixer.music.load("./src/audio/spawn.wav")
                    pygame.mixer.music.play(-1, 3.0)
                    pygame.mixer.music.set_volume(0.2)
            
            if ravenshire.map[spawn_player.coord[0]][spawn_player.coord[1]+1]=="🌱" and key == Controls["interact"]:
                if Player == spawn_player:
                    print("Vous n'avez pas d'objet pour couper cette arbuste, revenez plus tard")
                    time.sleep(1)
                elif "" in Player.inventory.items :
                    ravenshire.map[18,13] = "  "
                    print("Vous avez coupé l'arbuste")
                    time.sleep(1)
                else:
                    print("Vous n'avez pas d'objet pour couper cette arbuste")
                    time.sleep(1)

            if ravenshire.map[spawn_player.coord[0]-1][spawn_player.coord[1]]=="💼" and key == Controls["interact"]:
                print("Vous avez trouvé une carte")
                time.sleep(1)

            if (ravenshire.map[tombe_pos[0]-1][tombe_pos[1]]==ravenshire.map[spawn_player.coord[0]][spawn_player.coord[1]]or ravenshire.map[tombe_pos[0]+1][tombe_pos[1]]==ravenshire.map[spawn_player.coord[0]][spawn_player.coord[1]]or ravenshire.map[tombe_pos[0]][tombe_pos[1]-1]==ravenshire.map[spawn_player.coord[0]][spawn_player.coord[1]]) and key == Controls["interact"]:
                print("Il y a un panneau devant vous, voulez vous le lire ? (y/n)")
                if input() == "y":
                    print("") # LORE A RACONTER ICI AVEC CONDITION CONTINUER DE LIRE 
                    time.sleep(1)


            if spawn_player.coord in tp_pos:
                if Player == spawn_player:
                    afficher_carte(ravenshire.map)
                    print("Il est encore trop tôt pour partir")   
                    time.sleep(1)
                    ravenshire.map[spawn_player.coord[0]][spawn_player.coord[1]] = "  "
                    spawn_player.coord = [spawn_player.coord[0], spawn_player.coord[1]+1]
                    ravenshire.map[spawn_player.coord[0]][spawn_player.coord[1]] = " O"
                    afficher_carte(ravenshire.map)       
            if  spawn_player.coord in tp_pos2:
                if Player == spawn_player:
                    afficher_carte(ravenshire.map)
                    print("Il est encore trop tôt pour partir")           
                    time.sleep(1)
                    ravenshire.map[spawn_player.coord[0]][spawn_player.coord[1]] = "  "
                    spawn_player.coord = [spawn_player.coord[0]+1,spawn_player.coord[1]]
                    ravenshire.map[spawn_player.coord[0]][spawn_player.coord[1]] = " O"
                    afficher_carte(ravenshire.map)
            if spawn_player.coord in last_map_pos:
                ravenshire.map[spawn_player.coord[0]][spawn_player.coord[1]] = "  "
                spawn_player.coord = [1, spawn_player.coord[1]]
                spawn_nextmap()