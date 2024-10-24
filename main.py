import msvcrt

print("Appuie sur une touche, appuie sur 'q' pour quitter.")
while True:
    if msvcrt.kbhit():
        key = msvcrt.getch().decode('utf-8')
        print(f"Touche appuyée: {key}")
        if key == 'q':
            break
