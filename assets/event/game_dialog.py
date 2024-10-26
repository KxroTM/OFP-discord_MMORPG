import os
import time
import sys
import pygame
from assets.classes.entity import player
from assets.classes.inventory import inventory
from assets.object.items import Carte


def Alberic_dialog(map_name):
    pygame.mixer.stop()
    pygame.mixer.music.load("./src/audio/speaking.wav")
    pygame.mixer.music.play(-1, 3.0)
    pygame.mixer.music.set_volume(0.2)
    if map_name == "village_spawn_map" :
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
    elif map_name == "village_spawn_map2" :
        dialog = [
            "Alberic: Tu es encore là..",
            "Alberic: Je te conseille d'aller te diriger à l'ouest",
            "Alberic: N'oublie pas ce que je t'ai dit..",
            "Alberic: Hahahahaha..",
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

def Alberic_player_intro():
    
    dialog = [
        "Alberic: Attends un instant..",
        "Alberic: Je oublier de te demander ton nom",
        "Alberic: Comment t'appelles-tu ?",
        ]
    
    dialog2 = [
        "Alberic: C'est donc toi.. ",
        "Alberic: Pour t'aider durant ton aventure, je vais te donner un objet qui te sera utile..",
        "*Alberic vous a donner une carte, pour pouvoir l'utiliser appuyez sur i*",
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
            input("\nPress Enter to continue...")
    
    username = input("\n> ")

    Player = player(
        name = username,
        hp=15,
        atk=3,
        defense=0,
        xp=0,
        level=1,
        inventory= inventory(),
        crit_rate=10,
        crit_dmg=2,
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
        input("\nPress Enter to continue...")

    os.system('cls' if os.name == 'nt' else 'clear')
    return Player


