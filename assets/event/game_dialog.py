import os
import time
import sys
import pygame

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
            "Alberic: Si tu veux vraiment rester alors de ne faire confiance à personne et de ne pas te fier aux apparences, ni même à moi hahahahahaha..",
            "Alberic: Bon courage à toi, aventurier..",
            "Alberic: Tu en auras besoin.."
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