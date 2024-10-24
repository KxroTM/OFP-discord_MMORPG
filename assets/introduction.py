import time
import os
import keyboard

def apparition_progressive(frames, vitesse=0.2):
    frames_visible = ['' for _ in frames]
    
    for i in range(len(frames)):
        os.system('cls' if os.name == 'nt' else 'clear') 

        for j in range(i + 1): 
            frames_visible[j] = frames[j] 
            print(frames_visible[j])

        time.sleep(vitesse)

frames = [
    "╔══════════════════════════════════════════《✧ 》═══════════════════════════════════════╗",
    "                                                                                        ",
    "  ████████╗██╗░░██╗███████╗  ░█████╗░██████╗░██████╗░███████╗██████╗░  ░█████╗░███████╗",
    "  ╚══██╔══╝██║░░██║██╔════╝  ██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗  ██╔══██╗██╔════╝",
    "  ░░░██║░░░███████║█████╗░░  ██║░░██║██████╔╝██║░░██║█████╗░░██████╔╝  ██║░░██║█████╗░░",
    "  ░░░██║░░░██╔══██║██╔══╝░░  ██║░░██║██╔══██╗██║░░██║██╔══╝░░██╔══██╗  ██║░░██║██╔══╝░░",
    "  ░░░██║░░░██║░░██║███████╗  ╚█████╔╝██║░░██║██████╔╝███████╗██║░░██║  ╚█████╔╝██║░░░░░",
    "  ░░░╚═╝░░░╚═╝░░╚═╝╚══════╝  ░╚════╝░╚═╝░░╚═╝╚═════╝░╚══════╝╚═╝░░╚═╝  ░╚════╝░╚═╝░░░░░",
    "        ████████╗██╗░░██╗███████╗  ███████╗███████╗██╗░░░░░██╗███╗░░██╗███████╗",
    "        ╚══██╔══╝██║░░██║██╔════╝  ██╔════╝██╔════╝██║░░░░░██║████╗░██║██╔════╝",
    "        ░░░██║░░░███████║█████╗░░  █████╗░░█████╗░░██║░░░░░██║██╔██╗██║█████╗░░",
    "        ░░░██║░░░██╔══██║██╔══╝░░  ██╔══╝░░██╔══╝░░██║░░░░░██║██║╚████║██╔══╝░░",
    "        ░░░██║░░░██║░░██║███████╗  ██║░░░░░███████╗███████╗██║██║░╚███║███████╗",
    "        ░░░╚═╝░░░╚═╝░░╚═╝╚══════╝  ╚═╝░░░░░╚══════╝╚══════╝╚═╝╚═╝░░╚══╝╚══════╝",
    "               ██████╗░███████╗░█████╗░███╗░░██╗██╗░░░██╗████████╗░██████╗",
    "               ██╔══██╗██╔════╝██╔══██╗████╗░██║██║░░░██║╚══██╔══╝██╔════╝",
    "               ██████╔╝█████╗░░███████║██╔██╗██║██║░░░██║░░░██║░░░╚█████╗░",
    "               ██╔═══╝░██╔══╝░░██╔══██║██║╚████║██║░░░██║░░░██║░░░░╚═══██╗",
    "               ██║░░░░░███████╗██║░░██║██║░╚███║╚██████╔╝░░░██║░░░██████╔╝",
    "               ╚═╝░░░░░╚══════╝╚═╝░░╚═╝╚═╝░░╚══╝░╚═════╝░░░░╚═╝░░░╚═════╝░",
    "                                                                                        ",
    "╚══════════════════════════════════════════《✧ 》═══════════════════════════════════════╝",
    "                                                                                         ",
    "                                                                                         ",
    "                                   1✦「 𝕹𝖔𝖚𝖛𝖊𝖑𝖑𝖊 𝖕𝖆𝖗𝖙𝖎𝖊 」                                 ",
    "                                   2✦「 𝕮𝖔𝖓𝖙𝖎𝖓𝖚𝖊𝖗 」                                      ",
    "                                   3✦「 𝕼𝖚𝖎𝖙𝖙𝖊𝖗 」                                        "
]

apparition_progressive(frames, vitesse=0.13)

while True:
    if keyboard.is_pressed("1"):
        os.system("python main.py")
        break

    elif keyboard.is_pressed("2"):
        print("Option 2 sélectionnée.")
        # ici our l'option 2

    elif keyboard.is_pressed("3"):
        print(" 𝕬𝖚 𝖗𝖊𝖛𝖔𝖎𝖗 !")
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear') 
        exit()

