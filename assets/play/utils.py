import os
import msvcrt
from assets.play.controls import Controls
from assets.event.save import save
from assets.object.spawn import spawn_player
import time

def move_in_pause_menu(player,carte):
    os.system('cls' if os.name == 'nt' else 'clear')
    cursor = [0,1]
    map = [["Reprendre", " "], ["Sauvegarder"," "], ["Quitter", " "]]
    map[cursor[0]][cursor[1]] = "<"

    print("Pause\n\n\n")
    for i in range(len(map)) :
        print(map[i][0] + "   " + map[i][1])

    while True:
        cursor_temp = cursor.copy()
        key = msvcrt.getch().decode('utf-8')
        os.system('cls' if os.name == 'nt' else 'clear')
        if key == Controls["up"] and cursor[0] > 0 :
            cursor[0] -= 1
        elif key == Controls["down"] and cursor[0] < len(map) - 1 :
            cursor[0] += 1
        elif key == Controls["exit"]:
            break
        elif key == "e" :
            if cursor[0] == 0 :
                break
            elif cursor[0] == 1 :
                if player.name == spawn_player.name :
                    print("Vous ne pouvez pas sauvegarder pour l'instant.")
                    time.sleep(2)
                    os.system('cls' if os.name == 'nt' else 'clear')
                else :
                    save(player,carte)
                    print("Sauvegarde réussie")
                    time.sleep(2)
                    os.system('cls' if os.name == 'nt' else 'clear')
            elif cursor[0] == 2 :
                print("Quitter")
                exit()
        else :
            print("Pause\n\n\n")
            for i in range(len(map)) :
                print(map[i][0] + "   " + map[i][1])
            continue
        map[cursor[0]][cursor[1]] = "<"
        map[cursor_temp[0]][cursor_temp[1]] = " "
        print("Pause\n\n\n")
        for i in range(len(map)) :
            print(map[i][0] + "   " + map[i][1])

