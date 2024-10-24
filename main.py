import msvcrt

print("Appuie sur une touche, appuie sur 'q' pour quitter.")
while True:
    if msvcrt.kbhit():
        key = msvcrt.getch().decode('cp437')  # Remplacer 'utf-8' par 'cp437'
        print(f"Touche appuyée: {key}")
        if key == 'q':
            break