# spawn.py

from assets.classes.entity import player, mob
from assets.classes.inventory import inventory
from assets.object.ascii import spawn_monster

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
    max_hp=15,
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
