import os
import time
import sys
import pygame
from assets.classes.entity import player
from assets.classes.inventory import inventory
from assets.object.items import Carte


def Alberic_dialog(map_name):
    pygame.mixer.init()
    pygame.mixer.music.load("./src/audio/speaking.wav")
    pygame.mixer.music.play(-1, 3.0)
    pygame.mixer.music.set_volume(0.2)
    if map_name == "ravenshire" :
        dialog = [
            "Alberic: Oh, tu as donc réussi à fuir le monstre dans la forêt.. haha..",
            "Alberic: Ou bien tu as peut-être dû le tuer.. si c'est le cas j'espère qu'il n'a pas trop souffert..",
            "Alberic: Laisse moi me présenter, je suis Alberic, rescapé du village qui t'entoure..",
            "Alberic: Tu sais.. peut-être que survivre dans cette forêt n'était une si bonne idée.. Soit, tu n'es pas le seul aventurier à avoir réussi à venir jusqu'ici, laisse moi te dire deux trois choses.",
            "Alberic: Si tu le peux encore je te conseille de retourner d'où tu viens.",
            "Alberic: Si tu veux vraiment rester alors ne fais confiance à personne et de ne pas te fier aux apparences, ni même à moi hahahahahaha..",
            "Alberic: Bon courage à toi, aventurier..",
            "Alberic: Tu en auras besoin.."
        ]
    elif map_name == "ravenshire2" :
        dialog = [
            "Alberic: Tu es encore là..",
            "Alberic: Je te conseille d'aller te diriger à l'ouest",
            "Alberic: N'oublie pas ce que je t'ai dit..",
            "Alberic: Hahahahaha..",
            "Alberic: Oh et si tu as besoin de te soigner, reviens me voir.."
        ]
    elif map_name == "ravenshire3" :
        dialog = [
            "Alberic: Tu es venu pour te faire soigner ?",
        ]
    elif map_name == "ravenshire4" :
        dialog = [
            "Alberic: Te voilà maintenant en pleine forme..",
            "Alberic: Ton voyage n'a pas l'air très paisible..",
            "Alberic: ...",
        ]
    elif map_name == "route_9" :
        dialog = [
            "Alberic: Te revoilà..",
            "Alberic: Je suis aller voir comment tu t'es débrouillé dans la forêt..",
            "Alberic: Tu l'as vraiment tué..",
            "Alberic: Tu n'as donc pas changé..",
            "Alberic: Tous ces efforts pour rien..",
            "Alberic: Fais attention, derrière moi se trouve un des 4 Chevaliers de l'Apocalypse..",
            "Alberic: J'aurais préféré que tu changes sans avoir à les retrouver..",
            "Alberic: Qui sait, peut-être que après les avoir tous tués tu t'en souviendras..",
        ]

    os.system('cls' if os.name == 'nt' else 'clear')
    for i in range(0, (len(dialog))):
        os.system('cls' if os.name == 'nt' else 'clear')
        for j in range(0, i):
            print(dialog[j])
        for char in dialog[i]:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.03)
        input("\nPress Enter to continue...")
    pygame.mixer.music.stop()
    os.system('cls' if os.name == 'nt' else 'clear')

def Alberic_player_intro(coord=None):
    
    dialog = [
        "Alberic: Attends un instant..",
        "Alberic: Je oublier de te demander ton nom",
        "Alberic: Comment t'appelles-tu ?",
        ]
    
    dialog2 = [
        "Alberic: C'est donc toi.. ",
        "Alberic: Pour t'aider durant ton aventure, je vais te donner un objet qui te sera utile..",
        "\033[1m\033[3mAlberic vous a donner une carte, pour pouvoir l'utiliser appuyez sur m\033[0m\033[0m",
        "Alberic: Je te laisse maintenant",
        "Alberic: On se reverra peut-être..",
    ]

    os.system('cls' if os.name == 'nt' else 'clear')
    for i in range(0, (len(dialog))):
        os.system('cls' if os.name == 'nt' else 'clear')
        for j in range(0, i):
            print(dialog[j])
        for char in dialog[i]:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.03)
        if i != (len(dialog)-1):
            input("\nAppuyez sur Entrer pour continuer...")
    
    username = input("\n> ")

    Player = player(
        name = username,
        hp=15,
        atk=2,
        defense=0,
        xp=0,
        level=1,
        inventory= inventory(),
        crit_rate=15,
        crit_dmg=2,
        coord=coord,
        max_hp=15
    )

    Player.inventory.add(Carte)


    os.system('cls' if os.name == 'nt' else 'clear')

    for i in range(0, (len(dialog2))):
        os.system('cls' if os.name == 'nt' else 'clear')
        for j in range(0, i):
            print(dialog2[j])
        for char in dialog2[i]:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.03)
        input("\nAppuyez sur Entrer pour continuer...")

    os.system('cls' if os.name == 'nt' else 'clear')
    return Player


