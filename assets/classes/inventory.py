# inventory.py
import time
import os
import msvcrt

def move_in_inventory(items,player) :
    os.system('cls' if os.name == 'nt' else 'clear')
    item_temp = []
    for item in items :
        if item.type == "usable" :
            if item.used == False :
                item_temp.append(item)
        else :
            item_temp.append(item)

    items = item_temp


    if len(items) == 0 :
        print("Votre inventaire est vide")
        time.sleep(1)
        return
    else :
        cursor = [0,1]

        def print_inventaire(items):
            os.system('cls' if os.name == 'nt' else 'clear')
            for i in range(len(items)) :
                map = [[items[i].name, " "] for i in range(len(items))]
            
            map[cursor[0]][cursor[1]] = "<"

            print("Inventaire :\n\n\n")
            for i in range(len(map)) :
                print(map[i][0] + "   " + map[i][1])

            print("\n\n\nAppuyez sur 'i' pour quitter l'inventaire")

        def afficher_inventaire(items, key) :
            print_inventaire(items)
            if key == "z" and cursor[0] > 0 :
                cursor[0] -= 1
                print_inventaire(items)
            elif key == "s" and cursor[0] < len(items)-1:
                cursor[0] += 1
                print_inventaire(items)
            elif key == "e" :
                if items[cursor[0]].type != "important" :
                    items[cursor[0]].use(player)
                    if items[cursor[0]].type == "usable" :
                        items.remove(items[cursor[0]])
                        if cursor[0] == len(items) :
                            cursor[0] -= 1
                        print_inventaire(items)
                else :
                    items[cursor[0]].use()


    afficher_inventaire(items,"")
    while True:
        key = msvcrt.getch().decode('utf-8')
        afficher_inventaire(items, key)
        if key == "i":
            return

def move_in_inventory_fight(items,player) :
    os.system('cls' if os.name == 'nt' else 'clear')
    items = [item for item in items if item.type == "usable"]
    items = [item for item in items if item.used == False]
    if len(items) == 0 :
        print("Votre inventaire est vide")
        time.sleep(1)
        return
    else :
        cursor = [0,1]

        def print_inventaire(items):
            os.system('cls' if os.name == 'nt' else 'clear')

            for i in range(len(items)) :
                map = [[items[i].name, " "] for i in range(len(items))]
            
            map[cursor[0]][cursor[1]] = "<"

            print("Inventaire :\n\n\n")
            for i in range(len(map)) :
                print(map[i][0] + "   " + map[i][1])


        def afficher_inventaire(items, key) :
            print_inventaire(items)
            if key == "z" and cursor[0] > 0 :
                cursor[0] -= 1
                print_inventaire(items)
            elif key == "s" and cursor[0] < len(items) - 1 :
                cursor[0] += 1
                print_inventaire(items)
            elif key == "e" :
                items[cursor[0]].use(player)
                return True

    afficher_inventaire(items,"")
    while True:
        key = msvcrt.getch().decode('utf-8')
        if afficher_inventaire(items, key) :
            return

class inventory :
    
    def __init__(self) :
        self.items = []
        
    def add(self, item) :
        self.items.append(item)
    
    def remove(self, item) :
        self.items.remove(item)

    def use(self, item) :
        item_ = self.get_item(item)
        if item_ != None :
            item_.use()
        else :
            print("Vous n'avez pas cet objet dans votre inventaire")
            time.sleep(1)

    def show(self,player) :
        move_in_inventory(self.items,player)

    def show_in_fight(self,player) :
        move_in_inventory_fight(self.items,player)

    def get_item(self, item_aimed) :
        for item in self.items :
            if item.name == item_aimed :
                return item
        return None


class item :
    def __init__(self, name, description,type) :
        self.name = name
        self.description = description
        self.type = type

    def use(self) :
        pass
    

class carte(item) :
    def __init__(self) :
        super().__init__("Carte", "Une carte qui vous permet de voir votre position sur la carte","important")
    
    def use(self) :
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Vous regardez la carte..")
        print("Vous êtes actuellement à l'endroit indiqué par le point rouge")
        print("Vous pouvez voir les différentes zones que vous avez déjà visité")
        print("Vous pouvez également voir les zones que vous n'avez pas encore visité")
        input("Entrer pour continuer..")
        os.system('cls' if os.name == 'nt' else 'clear')

class potion(item) :
    def __init__(self, name, description, point) :
        super().__init__(name, description,"usable")
        self.point = point
        self.used = False

    def use(self) :
        self.used = True
        print(f"Vous avez utilisé {self.name}")
        time.sleep(1)

class potion_hp(potion) :
    def __init__(self,name) :
        super().__init__(name, "Une potion qui vous soigne de 50 hp", 20)

    def use(self,player) :
        super().use()
        player.hp += self.point

class potion_force(potion) :
    def __init__(self,name) :
        super().__init__(name, "Une potion qui augmente votre force de 10", 10)

    def use(self,player) :
        super().use()
        player.atk += self.point
        
class potion_defense(potion) :
    def __init__(self,name) :
        super().__init__(name, "Une potion qui augmente votre défense de 10", 10)

    def use(self,player) :
        super().use()
        player.defense += self.point


class arme(item) :
    def __init__(self, name, description, atk) :
        super().__init__(name, description,"arme")
        self.atk = atk

    def use(self) :
        pass
    
class epee(arme) :
    def __init__(self,name,description,atk) :
        super().__init__(name, description, atk)
        self.equiper = False

    def use(self,player) :
        if self.equiper :
            player.atk -= self.atk
            self.equiper = False
            print("Vous avez déséquipé l'épée : votre force a été réduite de 10")
            time.sleep(1)
        else :
            player.atk += self.atk
            self.equiper = True
            print("Vous avez équipé l'épée : votre force a été augmentée de 10")
            time.sleep(1)

