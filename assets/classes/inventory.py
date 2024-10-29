# inventory.py
import time
import os
import msvcrt

def move_in_inventory(items) :
    os.system('cls' if os.name == 'nt' else 'clear')
    if len(items) == 0 :
        print("Votre inventaire est vide")
        time.sleep(1)
        return
    else :
        def afficher_inventaire(items, key) :
            os.system('cls' if os.name == 'nt' else 'clear')
            cursor = [0,1]
            for i in range(len(items)) :
                map = [[items[i].name, " "] for i in range(len(items))]
            
            map[cursor[0]][cursor[1]] = "<"

            print("Inventaire :\n\n\n")
            for i in range(len(map)) :
                print(map[i][0] + "   " + map[i][1])

            print("\n\n\nAppuyez sur 'i' pour quitter l'inventaire")

            if key == "z" and cursor[0] > 0 :
                cursor[0] -= 1
            elif key == "s" and cursor[0] < len(items) - 1 :
                cursor[0] += 1
            elif key == "e" :
                items[cursor[0]].use()
                afficher_inventaire(items, "")

    afficher_inventaire(items,"")
    while True:
        key = msvcrt.getch().decode('utf-8')
        afficher_inventaire(items, key)
        if key == "i":
            return

class inventory :
    
    def __init__(self) :
        self.items = []
        
    def add(self, item) :
        self.items.append(item)
    
    def remove(self, item) :
        self.items.remove(item)

    def use(self, item) :
        if item in self.items :
            item.use()
        else :
            print("Vous n'avez pas cet objet dans votre inventaire")
            time.sleep(1)

    def show(self) :
        move_in_inventory(self.items)


class item :
    def __init__(self, name, description) :
        self.name = name
        self.description = description

    def use(self) :
        pass
    

class carte(item) :
    def __init__(self) :
        super().__init__("Carte", "Une carte qui vous permet de voir votre position sur la carte")
    
    def use(self) :
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Vous regardez la carte..")
        print("Vous êtes actuellement à l'endroit indiqué par le point rouge")
        print("Vous pouvez voir les différentes zones que vous avez déjà visité")
        print("Vous pouvez également voir les zones que vous n'avez pas encore visité")
        input("Entrer pour continuer..")
        os.system('cls' if os.name == 'nt' else 'clear')


