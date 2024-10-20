from assets.classes.entity import player, mob
from assets.classes.inventory import inventory

spawn_player = player(
    name = "Player",
    hp=15,
    atk=5,
    defense=0,
    xp=0,
    level=1,
    inventory= inventory(
        items=[]
    )
)

spawn_mob = mob(
    name="???",
    hp=20,
    atk=3,
    defense=0,
    level=1,
    focus=100,
    image="https://c.tenor.com/EOlZo1vc8lcAAAAC/tenor.gif"
)