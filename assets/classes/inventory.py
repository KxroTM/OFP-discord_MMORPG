# inventory.py
import time
import os

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
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Inventaire :")
        for item in self.items :
            print(item.name + " : " + item.description)
        input("Entrer pour continuer..")
        os.system('cls' if os.name == 'nt' else 'clear')


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