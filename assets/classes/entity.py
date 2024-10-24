import random


class entity :
    def __init__(self, name, hp, atk, defense, level, ) :
        self.name = name
        self.hp = hp
        self.atk = atk
        self.defense = defense
        self.level = level



class player(entity) :
    def __init__(self, name, hp, atk, defense, xp, level,inventory, ) :
        super().__init__(name, hp, atk, defense, level)
        self.xp = xp
        self.inventory = inventory


    def attack(self, target) :
        damage = self.atk - target.defense
        target.hp -= damage


    def flee(self, target) :
        chance = 100 - target.focus
        if random.randint(1, 100) <= chance :
            return True
        else :
            return False

    def use_inventory(self) :
        pass

class mob(entity) :
    def __init__(self, name, hp, atk, defense, level, focus, image, ) :
        super().__init__(name, hp, atk, defense, level ,)
        self.focus = focus
        self.image = image

    def attack(self, target) :
        damage = self.atk - target.defense
        target.hp -= damage
