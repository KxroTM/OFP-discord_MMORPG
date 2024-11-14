# spawn.py

from assets.classes.entity import player, mob
from assets.classes.inventory import inventory
from assets.object.ascii import spawn_monster,farmer_mob,goblin_monster,knight,squeleton

spawn_player = player(
    name = "Player",
    hp=15,
    atk=5,
    defense=0,
    xp=0,
    level=1,
    inventory= inventory(),
    crit_rate=10,
    crit_dmg=1,
    coord=[0,0],
)

spawn_mob = mob(
    name="???",
    hp=20,
    atk=3,
    defense=0,
    level=1,
    focus=100,
    image=spawn_monster,
    crit_rate=30,
    crit_dmg=2,
)

farmer_mob = mob(
    name="???",
    hp=20,
    atk=3,
    defense=0,
    level=1,
    focus=100,
    image=spawn_monster,
    crit_rate=30,
    crit_dmg=2,
)

goblin_monster = mob(
    name="???",
    hp=20,
    atk=3,
    defense=0,
    level=1,
    focus=100,
    image=spawn_monster,
    crit_rate=30,
    crit_dmg=2,
)

knight_mob = mob(
    name="???",
    hp=20,
    atk=3,
    defense=0,
    level=1,
    focus=100,
    image=spawn_monster,
    crit_rate=30,
    crit_dmg=2,
)

squeleton_mob = mob(
    name="???",
    hp=20,
    atk=3,
    defense=0,
    level=1,
    focus=100,
    image=spawn_monster,
    crit_rate=30,
    crit_dmg=2,
)
