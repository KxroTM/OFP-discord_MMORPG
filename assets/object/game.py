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
from assets.object.maps import caelid, route_1 , ravenshire, route_5, route_2, eldermbrume, route_4, route_6 , fernhollow, route_7, route_8, route_9
from assets.object.mob import createFarmerMob, createGoblinMob, createKnightMob, createSqueletonMob
from assets.classes.inventory import epee


global Player
Player = spawn_player


def gamestart(player=None,map=None):
    if player == None and map == None:
        global spawn_player
        spawn_player.coord = [10, 11]
        spawn()
    else:
        global Player
        Player = player
        if map == "caelid":
            caelid.map[Player.coord[0]][Player.coord[1]] = " O"
            spawn()
        elif map == "route_1":
            route_1.map[Player.coord[0]][Player.coord[1]] = " O"
            spawn_nextmap()
        elif map == "ravenshire":
            ravenshire.map[Player.coord[0]][Player.coord[1]] = " O"
            village_spawn()
        elif map == "route_5":
            route_5.map[Player.coord[0]][Player.coord[1]] = " O"
            route5()
        elif map == "route_2":
            route_2.map[Player.coord[0]][Player.coord[1]] = " O"
            route2()
        elif map == "eldermbrume":
            eldermbrume.map[Player.coord[0]][Player.coord[1]] = " O"
            eldermbrum()
        elif map == "route_4":
            route_4.map[Player.coord[0]][Player.coord[1]] = " O"
            route4()
        elif map == "route_6":
            route_6.map[Player.coord[0]][Player.coord[1]] = " O"
            route6()
        elif map == "fernhollow":
            fernhollow.map[Player.coord[0]][Player.coord[1]] = " O"
            fernhollow()
        elif map == "route_7":
            route_7.map[Player.coord[0]][Player.coord[1]] = " O"
            route7()
        elif map == "route_8":
            route_8.map[Player.coord[0]][Player.coord[1]] = " O"
            route8()
        elif map == "route_9":
            route_9.map[Player.coord[0]][Player.coord[1]] = " O"
            route9()
        

def afficher_carte(map):
    os.system('cls' if os.name == 'nt' else 'clear')
    for row in map:
        print("".join(row))

def deplacer_joueur(direction,map):
    global Player, monster_pos, monster_defait
    new_pos = Player.coord.copy()

    if direction == Controls["up"]:  # Haut
        new_pos[0] -= 1
    elif direction == Controls["down"]:  # Bas
        new_pos[0] += 1
    elif direction == Controls["left"]:  # Gauche
        new_pos[1] -= 1
    elif direction == Controls["right"]:  # Droite
        new_pos[1] += 1

    if (0 <= new_pos[0] < len(map.map) and
            0 <= new_pos[1] < len(map.map[0]) and
            map.map[new_pos[0]][new_pos[1]] not in map.collision):
        map.map[Player.coord[0]][Player.coord[1]] = "  "
        Player.coord = new_pos
        map.map[Player.coord[0]][Player.coord[1]] = " O"

        if map.map == caelid.map:
            if Player.coord[0] == 7 and monster_pos == None and monster_defait == False:
                monster_pos = [3, 11]
                map.map[monster_pos[0]][monster_pos[1]] = emoji.emojize("🧟 ")

def deplacer_monstre():
    global monster_pos
    if monster_pos:
        caelid.map[monster_pos[0]][monster_pos[1]] = "  "  

        if monster_pos[0] < Player.coord[0]:  # Descendre
            monster_pos[0] += 1
        elif monster_pos[0] > Player.coord[0]:  # Monter
            monster_pos[0] -= 1
        if monster_pos[1] < Player.coord[1]:  # Aller à droite
            monster_pos[1] += 1
        elif monster_pos[1] > Player.coord[1]:  # Aller à gauche
            monster_pos[1] -= 1

        caelid.map[monster_pos[0]][monster_pos[1]] = emoji.emojize("🧟 ")

def deplacer_Alberic():
    global Alberic_pos
    if Alberic_pos:
        ravenshire.map[Alberic_pos[0]][Alberic_pos[1]] = "  "  

        # gestion des diagonales
        if Alberic_pos[0] < Player.coord[0] and Alberic_pos[1] < Player.coord[1]:  # si le joueur est en bas à droite de Alberic
            Alberic_pos[0] += 1
            ravenshire.map[Alberic_pos[0]][Alberic_pos[1]] = "🧙"
            return Alberic_pos
        elif Alberic_pos[0] < Player.coord[0] and Alberic_pos[1] > Player.coord[1]:  # si le joueur est en bas à gauche de Alberic
            Alberic_pos[0] += 1
            ravenshire.map[Alberic_pos[0]][Alberic_pos[1]] = "🧙"
            return Alberic_pos
        elif Alberic_pos[0] > Player.coord[0] and Alberic_pos[1] < Player.coord[1]:  # si le joueur est en haut à droite de Alberic
            Alberic_pos[0] -= 1
            ravenshire.map[Alberic_pos[0]][Alberic_pos[1]] = "🧙"
            return Alberic_pos
        elif Alberic_pos[0] > Player.coord[0] and Alberic_pos[1] > Player.coord[1]:  # si le joueur est en haut à gauche de Alberic
            Alberic_pos[0] -= 1
            ravenshire.map[Alberic_pos[0]][Alberic_pos[1]] = "🧙"
            return Alberic_pos

        if Alberic_pos[0] < Player.coord[0]:  # si le joueur est en dessous de Alberic
            Alberic_pos[0] += 1
        elif Alberic_pos[0] > Player.coord[0]:  # si le joueur est au dessus de Alberic
            Alberic_pos[0] -= 1
        if Alberic_pos[1] < Player.coord[1]:  # si le joueur est à droite
            Alberic_pos[1] += 1
        elif Alberic_pos[1] > Player.coord[1]:  # si le joueur est à gauche
            Alberic_pos[1] -= 1
        
        ravenshire.map[Alberic_pos[0]][Alberic_pos[1]] = "🧙"

        return Alberic_pos

def rdm_fight(taux_spawn): # A CHANGER LES MOBS
    rdm = random.randint(1, taux_spawn) 
    if rdm == 1:
        mob = random.randint(1,100)
        if mob <= 30:
            fight(Player, createFarmerMob(Player))
            if Player.hp <= 0:
                gameoverscreen()
                quit()
        elif mob > 30 and mob <= 60:
            fight(Player, createGoblinMob(Player))
            if Player.hp <= 0:
                gameoverscreen()
                quit()
        elif mob < 90:
            fight(Player, createKnightMob(Player))
            if Player.hp <= 0:
                gameoverscreen()
                quit()
        elif mob > 60 and mob <= 90:
            fight(Player, createSqueletonMob(Player))
            if Player.hp <= 0:
                gameoverscreen()
                quit()

def spawn() :
    global monster_pos, monster_defait, tp_pos
    caelid.map[Player.coord[0]][Player.coord[1]] = " O"
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
            move_in_pause_menu(Player, "caelid")
        if key == Controls["map"]:
            Player.inventory.use(Carte)
            afficher_carte(caelid.map)
        if key == Controls["inventory"]:
            Player.inventory.show(Player)
            afficher_carte(caelid.map)
        deplacer_joueur(key, caelid)
        deplacer_monstre()
        if monster_pos == Player.coord:
            pygame.mixer.music.stop()
            fight(Player, spawn_mob)
            if Player.hp <= 0:
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

        if Player.coord in tp_pos:
            caelid.map[Player.coord[0]][Player.coord[1]] = "  "
            Player.coord = [15, Player.coord[1]]
            spawn_nextmap()           

def spawn_nextmap() :
    global Player, tp_pos
    route_1.map[Player.coord[0]][Player.coord[1]] = " O"
    tp_pos = [[0,9],[0,10],[0, 11],[0,12],[0,13]]
    last_map_pos = [[16,9],[16,10],[16, 11],[16,12],[16,13]]
    collision_spawn_map = ["🌲"]
    while True:
        afficher_carte(route_1.map)
        key = msvcrt.getch().decode('utf-8')
        if key == Controls["exit"]:
            move_in_pause_menu(Player, "route_1")
        if key == Controls["map"]:
            Player.inventory.use(Carte)
            afficher_carte(route_1.map)
        if key == Controls["inventory"]:
            Player.inventory.show(Player)
            afficher_carte(route_1.map)
        deplacer_joueur(key, route_1)

        if Player.coord in tp_pos:
            route_1.map[Player.coord[0]][Player.coord[1]] = "  "
            Player.coord = [15,Player.coord[1]]
            village_spawn()
        
        if Player.coord in last_map_pos:
            route_1.map[Player.coord[0]][Player.coord[1]] = "  "
            Player.coord = [1,Player.coord[1]]
            spawn()

def village_spawn(spawn=False) :
    global Player, tp_pos, tp_pos2, Alberic_pos
    Alberic_pos = [7, 10]
    if spawn == True:
        Player.coord = [15, 11]
    tp_pos = [[4,0], [5,0],[6,0],[7,0],[8,0],[9,0],[10,0],[11,0],[12,0]]
    tp_pos2 = [[0,10], [0,11], [0,12]]
    last_map_pos = [[16, 9], [16, 11], [16, 12], [16, 13], [16, 10]]
    ravenshire.map[Alberic_pos[0]][Alberic_pos[1]] = "🧙"
    ravenshire.map[Player.coord[0]][Player.coord[1]] = " O"
    tombe_pos = [5,17]
    ravenshire.map[tombe_pos[0]][tombe_pos[1]] = "📜"
    while True:
        afficher_carte(ravenshire.map)
        while True:
            afficher_carte(ravenshire.map)
            key = msvcrt.getch().decode('utf-8')
            if key == Controls["exit"]:
                move_in_pause_menu(Player, "ravenshire")
            if key == Controls["map"]:
                Player.inventory.use(Carte)
                afficher_carte(ravenshire.map)
            if key == Controls["inventory"]:
                Player.inventory.show(Player)
                afficher_carte(ravenshire.map)

            deplacer_joueur(key, ravenshire)

            if (ravenshire.map[Alberic_pos[0]-1][Alberic_pos[1]] == ravenshire.map[Player.coord[0]][Player.coord[1]] or ravenshire.map[Alberic_pos[0]+1][Alberic_pos[1]] == ravenshire.map[Player.coord[0]][Player.coord[1]] or ravenshire.map[Alberic_pos[0]][Alberic_pos[1]-1] == ravenshire.map[Player.coord[0]][Player.coord[1]] or ravenshire.map[Alberic_pos[0]][Alberic_pos[1]+1] == ravenshire.map[Player.coord[0]][Player.coord[1]]) and key == Controls["interact"]:
                if Player.name == spawn_player.name:
                    Alberic_dialog("ravenshire")
                    pygame.mixer.music.load("./src/audio/spawn.wav")
                    pygame.mixer.music.play(-1, 3.0)
                    pygame.mixer.music.set_volume(0.2)
                    for i in range(4):
                        afficher_carte(ravenshire.map)
                        key = msvcrt.getch().decode('utf-8')
                        if key == Controls["exit"]:
                            move_in_pause_menu(Player, "ravenshire")
                        deplacer_joueur(key, ravenshire)
                    while (ravenshire.map[Alberic_pos[0]-1][Alberic_pos[1]] != ravenshire.map[Player.coord[0]][Player.coord[1]] and ravenshire.map[Alberic_pos[0]+1][Alberic_pos[1]] != ravenshire.map[Player.coord[0]][Player.coord[1]] and ravenshire.map[Alberic_pos[0]][Alberic_pos[1]-1] != ravenshire.map[Player.coord[0]][Player.coord[1]] and ravenshire.map[Alberic_pos[0]][Alberic_pos[1]+1] != ravenshire.map[Player.coord[0]][Player.coord[1]]):
                        Alberic_pos = deplacer_Alberic()
                        afficher_carte(ravenshire.map)
                        time.sleep(1)
                    Player = Alberic_player_intro(Player.coord)
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load("./src/audio/spawn.wav")
                    pygame.mixer.music.play(-1, 3.0)
                    pygame.mixer.music.set_volume(0.2)
                else:
                    if Player.hp < Player.max_hp:
                        Alberic_dialog("ravenshire3")
                        choice = input("Écrivez oui pour vous soigner ou non pour refuser\n")
                        if choice == "oui":
                            Player.hp = Player.max_hp
                            Alberic_dialog("ravenshire4")
                    else :
                        Alberic_dialog("ravenshire2")
                    pygame.mixer.music.load("./src/audio/spawn.wav")
                    pygame.mixer.music.play(-1, 3.0)
                    pygame.mixer.music.set_volume(0.2)
            
            if Player.coord[1] != 22 :
                if ravenshire.map[Player.coord[0]][Player.coord[1]+1]=="🌱" and key == Controls["interact"]:
                    if Player == Player:
                        print("Vous n'avez pas d'objet pour couper cette arbuste, revenez plus tard")
                        time.sleep(1)
                    elif "" in Player.inventory.items :
                        ravenshire.map[18,13] = "  "
                        print("Vous avez coupé l'arbuste")
                        time.sleep(1)
                    else:
                        print("Vous n'avez pas d'objet pour couper cette arbuste")
                        time.sleep(1)
            
            if Player.coord[0] != 0 :
                if ravenshire.map[Player.coord[0]-1][Player.coord[1]]=="💼" and key == Controls["interact"]:
                    print("Vous avez trouvé une carte")
                    time.sleep(1)

            if (ravenshire.map[tombe_pos[0]-1][tombe_pos[1]]==ravenshire.map[Player.coord[0]][Player.coord[1]]or ravenshire.map[tombe_pos[0]+1][tombe_pos[1]]==ravenshire.map[Player.coord[0]][Player.coord[1]]or ravenshire.map[tombe_pos[0]][tombe_pos[1]-1]==ravenshire.map[Player.coord[0]][Player.coord[1]]) and key == Controls["interact"]:
                print("Il y a un panneau devant vous, voulez vous le lire ? (y/n)")
                if input() == "y":
                    print("") # LORE A RACONTER ICI AVEC CONDITION CONTINUER DE LIRE 
                    time.sleep(1)


            if Player.coord in tp_pos:
                if Player.name == spawn_player.name:
                    afficher_carte(ravenshire.map)
                    print("Il est encore trop tôt pour partir")   
                    time.sleep(1)
                    ravenshire.map[Player.coord[0]][Player.coord[1]] = "  "
                    Player.coord = [Player.coord[0], Player.coord[1]+1]
                    ravenshire.map[Player.coord[0]][Player.coord[1]] = " O"
                    afficher_carte(ravenshire.map)
                else :
                    ravenshire.map[Player.coord[0]][Player.coord[1]] = "  "
                    Player.coord = Player.coord
                    Player.coord = [Player.coord[0], 21]
                    route2()
                   
            if  Player.coord in tp_pos2:
                if Player.name == spawn_player.name:
                    afficher_carte(ravenshire.map)
                    print("Il est encore trop tôt pour partir")           
                    time.sleep(1)
                    ravenshire.map[Player.coord[0]][Player.coord[1]] = "  "
                    Player.coord = [Player.coord[0]+1,Player.coord[1]]
                    ravenshire.map[Player.coord[0]][Player.coord[1]] = " O"
                    afficher_carte(ravenshire.map)
                else :
                    ravenshire.map[Player.coord[0]][Player.coord[1]] = "  "
                    Player.coord = Player.coord
                    Player.coord = [18, Player.coord[1]]
                    route5()
                
            if Player.coord in last_map_pos:
                ravenshire.map[Player.coord[0]][Player.coord[1]] = "  "
                Player.coord = [1,Player.coord[1]]
                spawn_nextmap()

            if Player.coord == [2,2] and key == Controls["interact"]:
                if Player.name == spawn_player.name:
                    afficher_carte(ravenshire.map)
                    print("Vous voyez quelque chose mais le vieil homme plus loin attire votre attention")
                    time.sleep(1)
                else :
                    if Player.inventory.get_item("Épée en pierre") == None:
                        afficher_carte(ravenshire.map)
                        Player.inventory.add(epee(
                            "Épée en pierre",
                            "Une épée en pierre",
                            5,
                        ))
                        print("Vous avez trouvé une épée en pierre")
                        time.sleep(1)

def route5():
    route_5.map[Player.coord[0]][Player.coord[1]] = " O"
    tp_pos = [[0,10], [0,11], [0,12]]
    last_map_pos = [[19,10], [19,11], [19,12]]
    while True:
        afficher_carte(route_5.map)
        key = msvcrt.getch().decode('utf-8')
        if key == Controls["exit"]:
            move_in_pause_menu(Player, "route_5")
        if key == Controls["map"]:
            Player.inventory.use(Carte)
            afficher_carte(route_5.map)
        if key == Controls["inventory"]:
            Player.inventory.show(Player)
            afficher_carte(route_5.map)
        deplacer_joueur(key, route_5)
        rdm_fight(40)
        if Player.coord in tp_pos:
            route_5.map[Player.coord[0]][Player.coord[1]] = "  "
            Player.coord = [20,Player.coord[1]]
            route4()

        
        if Player.coord in last_map_pos:
            route_5.map[Player.coord[0]][Player.coord[1]] = "  "
            Player.coord = [1,Player.coord[1]]
            village_spawn()

def route2():
    route_2.map[Player.coord[0]][Player.coord[1]] = " O"
    tp_pos = [[4,0], [5,0],[6,0],[7,0],[8,0],[9,0],[10,0],[11,0],[12,0]]
    last_map_pos = [[4,22], [5,22],[6,22],[7,22],[8,22],[9,22],[10,22],[11,22],[12,22]]
    while True:
        afficher_carte(route_2.map)
        key = msvcrt.getch().decode('utf-8')
        if key == Controls["exit"]:
            move_in_pause_menu(Player, "route_2")
        if key == Controls["map"]:
            Player.inventory.use(Carte)
            afficher_carte(route_2.map)
        if key == Controls["inventory"]:
            Player.inventory.show(Player)
            afficher_carte(route_2.map)
        deplacer_joueur(key, route_2)
        rdm_fight(40)
        if Player.coord in tp_pos:
            route_2.map[Player.coord[0]][Player.coord[1]] = "  "
            Player.coord = [Player.coord[0],22]
            eldermbrum()
        
        if Player.coord in last_map_pos:
            route_2.map[Player.coord[0]][Player.coord[1]] = "  "
            Player.coord = [Player.coord[0],1]
            village_spawn()

def eldermbrum():
    eldermbrume.map[Player.coord[0]][Player.coord[1]] = " O"
    tp_pos = [[0,9],[0,10],[0,11],[0,12],[0,13]]
    last_map_pos = [[4,22], [5,22],[6,22],[7,22],[8,22],[9,22],[10,22],[11,22],[12,22]]
    while True:
        afficher_carte(eldermbrume.map)
        key = msvcrt.getch().decode('utf-8')
        if key == Controls["exit"]:
            move_in_pause_menu(Player, "eldermbrume")
        if key == Controls["map"]:
            Player.inventory.use(Carte)
            afficher_carte(eldermbrume.map)
        if key == Controls["inventory"]:
            Player.inventory.show(Player)
            afficher_carte(eldermbrume.map)
        deplacer_joueur(key, eldermbrume)
        rdm_fight(20)
        if Player.coord in tp_pos:
            eldermbrume.map[Player.coord[0]][Player.coord[1]] = "  "
            Player.coord = [14,Player.coord[1]]
            route6()
        
        if Player.coord in last_map_pos:
            eldermbrume.map[Player.coord[0]][Player.coord[1]] = "  "
            Player.coord = [Player.coord[0],1]
            route2()

def route4():
    route_4.map[Player.coord[0]][Player.coord[1]] = " O"
    tp_pos = [[0,10], [0,11], [0,12]]
    last_map_pos = [[21,10], [21,11], [21,12]]
    while True:
        afficher_carte(route_4.map)
        key = msvcrt.getch().decode('utf-8')
        if key == Controls["exit"]:
            move_in_pause_menu(Player, "route_4")
        if key == Controls["map"]:
            Player.inventory.use(Carte)
            afficher_carte(route_4.map)
        if key == Controls["inventory"]:
            Player.inventory.show(Player)
            afficher_carte(route_4.map)
        deplacer_joueur(key, route_4)
        rdm_fight(50)
        if Player.coord in tp_pos:
            route_4.map[Player.coord[0]][Player.coord[1]] = "  "
            Player.coord = [14,Player.coord[1]]
            fernhollo()

        if Player.coord in last_map_pos:
            route_4.map[Player.coord[0]][Player.coord[1]] = "  "
            Player.coord = [1,Player.coord[1]]
            route5()

def route6():
    route_6.map[Player.coord[0]][Player.coord[1]] = " O"
    tp_pos = [[4,22], [5,22],[6,22],[7,22],[8,22],[9,22],[10,22],[11,22]]
    last_map_pos = [[15,9],[15,10],[15,11],[15,12],[15,13]]
    while True:
        afficher_carte(route_6.map)
        key = msvcrt.getch().decode('utf-8')
        if key == Controls["exit"]:
            move_in_pause_menu(Player, "route_6")
        if key == Controls["map"]:
            Player.inventory.use(Carte)
            afficher_carte(route_6.map)
        if key == Controls["inventory"]:
            Player.inventory.show(Player)
            afficher_carte(route_6.map)
        deplacer_joueur(key, route_6)
        rdm_fight(50)

        if Player.coord in tp_pos:
            route_6.map[Player.coord[0]][Player.coord[1]] = "  "
            Player.coord = [Player.coord[0],1]
            fernhollo()
        
        if Player.coord in last_map_pos:
            route_6.map[Player.coord[0]][Player.coord[1]] = "  "
            Player.coord = [1,Player.coord[1]]
            eldermbrum()

def fernhollo():
    fernhollow.map[Player.coord[0]][Player.coord[1]] = " O"
    tp_pos = [[0,10],[0,11],[0,12]]
    tp_pos2 = [[4,23], [5,23],[6,23],[7,23],[8,23],[9,23],[10,23],[11,23]]
    last_map_pos = [[4,0], [5,0],[6,0],[7,0],[8,0],[9,0],[10,0],[11,0]]
    last_map_pos2 = [[15,10], [15,11], [15,12]]
    while True:
        afficher_carte(fernhollow.map)
        key = msvcrt.getch().decode('utf-8')
        if key == Controls["exit"]:
            move_in_pause_menu(Player, "fernhollow")
        if key == Controls["map"]:
            Player.inventory.use(Carte)
            afficher_carte(fernhollow.map)
        if key == Controls["inventory"]:
            Player.inventory.show(Player)
            afficher_carte(fernhollow.map)
        deplacer_joueur(key, fernhollow)
        rdm_fight(20)

        if Player.coord in tp_pos:
            # fernhollow.map[Player.coord[0]][Player.coord[1]] = "  "
            # Player.coord = [15,Player.coord[1]]
            # route6()
            print("Vous avez trouvé un passage secret")
            time.sleep(1)
        
        if Player.coord in tp_pos2:
            fernhollow.map[Player.coord[0]][Player.coord[1]] = "  "
            Player.coord = [Player.coord[0], 1]
            route7()

        if Player.coord in last_map_pos:
            fernhollow.map[Player.coord[0]][Player.coord[1]] = "  "
            Player.coord = [Player.coord[0],21]
            route6()

        if Player.coord in last_map_pos2:
            fernhollow.map[Player.coord[0]][Player.coord[1]] = "  "
            Player.coord = [1,Player.coord[1]]
            route4()

def route7():
    route_7.map[Player.coord[0]][Player.coord[1]] = " O"
    last_map_pos = [[4,0], [5,0],[6,0],[7,0],[8,0],[9,0],[10,0],[11,0]]
    tp_pos = [[4,22], [5,22],[6,22],[7,22],[8,22],[9,22],[10,22],[11,22]]
    while True:
        afficher_carte(route_7.map)
        key = msvcrt.getch().decode('utf-8')
        if key == Controls["exit"]:
            move_in_pause_menu(Player, "route_7")
        if key == Controls["map"]:
            Player.inventory.use(Carte)
            afficher_carte(route_7.map)
        if key == Controls["inventory"]:
            Player.inventory.show(Player)
            afficher_carte(route_7.map)
        deplacer_joueur(key, route_7)
        rdm_fight(50)

        if Player.coord in tp_pos:
            route_7.map[Player.coord[0]][Player.coord[1]] = "  "
            Player.coord = [Player.coord[0],1]
            route8()
        
        if Player.coord in last_map_pos:
            route_7.map[Player.coord[0]][Player.coord[1]] = "  "
            Player.coord = [Player.coord[0],22]
            fernhollo()

def route8():
    route_8.map[Player.coord[0]][Player.coord[1]] = " O"
    tp_pos = [[16,12], [16,13], [16,14], [16,15], [16,16]]
    last_map_pos = [[4,0], [5,0],[6,0],[7,0],[8,0],[9,0],[10,0],[11,0]]
    while True:
        afficher_carte(route_8.map)
        key = msvcrt.getch().decode('utf-8')
        if key == Controls["exit"]:
            move_in_pause_menu(Player,"route_8")
        if key == Controls["map"]:
            Player.inventory.use(Carte)
            afficher_carte(route_8.map)
        if key == Controls["inventory"]:
            Player.inventory.show(Player)
            afficher_carte(route_8.map)
        deplacer_joueur(key, route_8)
        rdm_fight(50)

        if Player.coord in tp_pos:
            route_8.map[Player.coord[0]][Player.coord[1]] = "  "
            Player.coord = [1,Player.coord[1]]
            route9()
        
        if Player.coord in last_map_pos:
            route_8.map[Player.coord[0]][Player.coord[1]] = "  "
            Player.coord = [Player.coord[0],21]
            route7()


def route9():
    route_9.map[Player.coord[0]][Player.coord[1]] = " O"
    tp_pos = [[19,12], [19,13], [19,14], [19,15], [19,16]]
    last_map_pos = [[0,12], [0,13], [0,14], [0,15], [0,16]]
    while True:
        afficher_carte(route_9.map)
        key = msvcrt.getch().decode('utf-8')
        if key == Controls["exit"]:
            move_in_pause_menu(Player,"route_9")
        if key == Controls["map"]:
            Player.inventory.use(Carte)
            afficher_carte(route_9.map)
        if key == Controls["inventory"]:
            Player.inventory.show(Player)
            afficher_carte(route_9.map)
        deplacer_joueur(key, route_9)
        rdm_fight(50)


        if Player.coord in last_map_pos:
            route_9.map[Player.coord[0]][Player.coord[1]] = "  "
            Player.coord = [15,Player.coord[1]]
            route8()

        if Player.coord in tp_pos:
            route_9.map[Player.coord[0]][Player.coord[1]] = "  "
            Player.coord = [Player.coord[0],21]
            Alberic_dialog("route_9")
        
        if Player.coord == [18,16] and key == Controls["interact"]:
            if Player.hp < Player.max_hp:
                Alberic_dialog("ravenshire3")
                choice = input("Écrivez oui pour vous soigner ou non pour refuser\n")
                if choice == "oui":
                    Player.hp = Player.max_hp
                    Alberic_dialog("ravenshire4")
