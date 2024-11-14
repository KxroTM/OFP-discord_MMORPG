from assets.object.ascii import farmer_mob_image, goblin_monster_image, knight_image, squeleton_image
from assets.classes.entity import mob


def createFarmerMob(Player):
    farmer_mob = mob(
        name="Fermier",
        hp=Player.hp-5,
        atk=Player.hp/6,
        defense=0,
        level=Player.level-1,
        focus=20,
        image=farmer_mob_image,
        crit_rate=10,
        crit_dmg=2,
    )
    return farmer_mob


def createGoblinMob(Player):
    goblin_monster = mob(
        name="Goblin",
        hp=Player.hp,
        atk=Player.hp/6,
        defense=2,
        level=Player.level+2,
        focus=50,
        image=goblin_monster_image,
        crit_rate=30,
        crit_dmg=2,
    )
    return goblin_monster

def createKnightMob(Player):
    knight_mob = mob(
        name="Chevalier",
        hp=Player.hp+5,
        atk=Player.hp/4,
        defense=5,
        level=Player.level+5,
        focus=80,
        image=knight_image,
        crit_rate=30,
        crit_dmg=2,
    )
    return knight_mob


def createSqueletonMob(Player):
    squeleton_mob = mob(
        name="Squelette",
        hp=Player.hp,
        atk=Player.hp/6,
        defense=0,
        level=Player.level+3,
        focus=100,
        image=squeleton_image,
        crit_rate=30,
        crit_dmg=2,
    )
    return squeleton_mob
