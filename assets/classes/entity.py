# entity.py

import random
import time

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
    def __init__(self, name, hp, atk, defense, xp, level,inventory,  crit_rate, crit_dmg, coord, max_hp) :
        super().__init__(name, hp, atk, defense, level , crit_rate, crit_dmg)
        self.xp = xp
        self.inventory = inventory
        self.coord = coord
        self.max_hp = max_hp

    def attack(self, target) :
        crit = random.randint(1, 100)
        if crit <= self.crit_rate : 
            damage = self.atk * self.crit_dmg - target.defense
            print(f'Vous avez crit {target.name} pour {damage} damage!')
        else :
            damage = self.atk - target.defense
            print(f'Vous avez attaqué {target.name} pour {damage} damage!')
        target.hp -= damage

    def flee(self, target) :
        chance = 100 - target.focus
        if random.randint(1, 100) <= chance :
            return True
        else :
            return False

    def use_inventory(self,player) :
        if len(self.inventory.items) == 0 :
            print("Il n'y a rien dans votre inventaire")
            return
        else :
            self.inventory.show_in_fight(player)

    def level_up(self) :
        if self.xp >= self.level * 100 :
            self.level += 1
            self.xp = 0
            self.max_hp += 10
            self.hp += 10
            self.atk += 5
            self.defense += 5
            print(f"Vous avez atteint le niveau {self.level} !")
            time.sleep(1)

class mob(entity) :
    def __init__(self, name, hp, atk, defense, level,crit_rate,crit_dmg, focus, image) :
        super().__init__(name, hp, atk, defense, level , crit_rate, crit_dmg)
        self.focus = focus
        self.image = image

    def attack(self, target) :
        crit = random.randint(1, 100)
        if crit <= self.crit_rate : 
            damage = self.atk * self.crit_dmg - target.defense
            print(f'{self.name} vous a crit pour {damage} damage!')
        else :
            damage = self.atk - target.defense
            print(f'{self.name} vous a attaqué pour {damage} damage!')
        if damage < 0 :
            damage = 0
        target.hp -= damage

