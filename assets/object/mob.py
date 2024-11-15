from assets.object.ascii import farmer_mob_image, goblin_monster_image, knight_image, squeleton_image,boss_stonehollow_ascii,boss_brackenstone_ascii,boss__duskreap_ascii,boss_kingshollow_ascii
from assets.classes.entity import mob


def createFarmerMob(Player):
    farmer_mob = mob(
        name="Fermier",
        hp=Player.max_hp-5,
        atk=3,
        defense=0,
        level=5,
        focus=20,
        image=farmer_mob_image,
        crit_rate=10,
        crit_dmg=2,
    )
    return farmer_mob


def createGoblinMob(Player):
    goblin_monster = mob(
        name="Goblin",
        hp=Player.max_hp,
        atk=5,
        defense=Player.atk/4,
        level=12,
        focus=50,
        image=goblin_monster_image,
        crit_rate=30,
        crit_dmg=2,
    )
    return goblin_monster

def createKnightMob(Player):
    knight_mob = mob(
        name="Chevalier",
        hp=Player.max_hp+5,
        atk=8,
        defense=Player.atk/2,
        level=30,
        focus=80,
        image=knight_image,
        crit_rate=30,
        crit_dmg=2,
    )
    return knight_mob


def createSqueletonMob(Player):
    squeleton_mob = mob(
        name="Squelette",
        hp=Player.max_hp/2,
        atk=2,
        defense=0,
        level=3,
        focus=100,
        image=squeleton_image,
        crit_rate=30,
        crit_dmg=2,
    )
    return squeleton_mob


def createBossStonehollow(Player):
    boss_stonehollow = mob(
        name="Boss Stonehollow",
        hp=Player.max_hp,
        atk=12, 
        defense=Player.atk/2,
        level=50,
        focus=100,
        image=boss_stonehollow_ascii,
        crit_rate=30,
        crit_dmg=2,
    )
    return boss_stonehollow

def createBossBrackenstone(Player):
    boss_brackenstone = mob(
        name="Boss Brackenstone",
        hp=Player.max_hp*1.5,
        atk=17,
        defense=Player.atk/2,
        level=70,
        focus=100,
        image=boss_brackenstone_ascii,
        crit_rate=30,
        crit_dmg=2,
    )
    return boss_brackenstone

def createBossDuskreap(Player):
    boss_duskreap = mob(
        name="Boss Duskreap",
        hp=Player.max_hp*2,
        atk=22,
        defense=Player.atk/2,
        level=90,
        focus=100,
        image=boss__duskreap_ascii,
        crit_rate=30,
        crit_dmg=2,
    )
    return boss_duskreap

def createBossKingshollow(Player):
    boss_kingshollow = mob(
        name="Boss Kingshollow",
        hp=Player.max_hp*2.5,
        atk=30,
        defense=Player.atk/2,
        level=120,
        focus=100,
        image=boss_kingshollow_ascii,
        crit_rate=30,
        crit_dmg=2,
    )
    return boss_kingshollow

