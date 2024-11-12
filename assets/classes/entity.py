# entity.py

import random


class entity :
    def __init__(self, name, hp, atk, defense, level,crit_rate,crit_dmg) :
        self.name = name
        self.hp = hp
        self.atk = atk
        self.defense = defense
        self.level = level
        self.crit_rate = crit_rate
        self.crit_dmg = crit_dmg



class player(entity) :
    def __init__(self, name, hp, atk, defense, xp, level,inventory,  crit_rate, crit_dmg, coord) :
        super().__init__(name, hp, atk, defense, level , crit_rate, crit_dmg)
        self.xp = xp
        self.inventory = inventory
        self.coord = coord

    def attack(self, target) :
        crit = random.randint(1, 100)
        if crit <= self.crit_rate : 
            damage = self.atk * self.crit_dmg - target.defense
            print(f'You crit {target.name} for {damage} damage!')
        else :
            damage = self.atk - target.defense
            print(f'You hit {target.name} for {damage} damage!')
        target.hp -= damage

    def flee(self, target) :
        chance = 100 - target.focus
        if random.randint(1, 100) <= chance :
            return True
        else :
            return False

    def use_inventory(self) :
        if len(self.inventory.items) == 0 :
            print("Inventory is empty.")
            return
        else :
            print("Inventory:")

class mob(entity) :
    def __init__(self, name, hp, atk, defense, level,crit_rate,crit_dmg, focus, image) :
        super().__init__(name, hp, atk, defense, level , crit_rate, crit_dmg)
        self.focus = focus
        self.image = image

    def attack(self, target) :
        crit = random.randint(1, 100)
        if crit <= self.crit_rate : 
            damage = self.atk * self.crit_dmg - target.defense
            print(f'{self.name} crits {target.name} for {damage} damage!')
        else :
            damage = self.atk - target.defense
            print(f'{self.name} hits {target.name} for {damage} damage!')
        target.hp -= damage

