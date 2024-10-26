# inventory.py

class inventory :
    def __init__(self, items, ) :
        self.items = items

    async def use(self, item) :
        if item in self.items :
            await item.use()
        else :
            return False
        
    def add(self, item) :
        self.items.append(item)
    
    def remove(self, item) :
        self.items.remove(item)


class item :
    def __init__(self, name, description) :
        self.name = name
        self.description = description

    async def use(self) :
        pass
    

class carte(item) :
    def __init__(self) :
        super().__init__("Carte", "Une carte qui vous permet de voir votre position sur la carte")
    
    async def use(self) :
        print("Vous regardez la carte..")
        print("Vous êtes actuellement à l'endroit indiqué par le point rouge")
        print("Vous pouvez voir les différentes zones que vous avez déjà visité")
        print("Vous pouvez également voir les zones que vous n'avez pas encore visité")