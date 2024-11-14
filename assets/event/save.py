from assets.classes.entity import player
from assets.classes.inventory import inventory, potion_defense, potion_force, potion_hp, epee, carte
import os 
import pygame

sqlite3 = __import__('sqlite3')

def save(player,map):
    os.remove('./save.sql')

    createtablesql()    
    dbsqlite = sqlite3.connect('./save.sql')
    cursor = dbsqlite.cursor()

    cursor.execute('''INSERT OR REPLACE INTO player (name, hp, attck, defense, level, crit_rate, crit_dmg, xp, max_hp) VALUES (?,?,?,?,?,?,?,?,?)''', (player.name, player.hp, player.atk, player.defense, player.level, player.crit_rate, player.crit_dmg, player.xp, player.max_hp))

    for item in player.inventory.items:
        if item.type == "usable":
            cursor.execute('''INSERT OR REPLACE INTO potion (name, description, type, point) VALUES (?,?,?,?)''', (item.name, item.description, item.type, item.point))
        elif item.type == "arme":
            cursor.execute('''INSERT OR REPLACE INTO arme (name, description, type, atk) VALUES (?,?,?,?)''', (item.name, item.description, item.type, item.atk))

    cursor.execute('''INSERT OR REPLACE INTO map (name) VALUES (?)''', (map,))

    cursor.execute('''INSERT OR REPLACE INTO coord (name, x, y) VALUES (?,?,?)''', (player.name, player.coord[1], player.coord[0]))


    dbsqlite.commit()
    dbsqlite.close() 

def load(name):
    dbsqlite = sqlite3.connect('./save.sql')
    cursor = dbsqlite.cursor()

    play = player(
        name=name,
        hp=100,
        atk=10,
        defense=10,
        xp=0,
        level=1,
        inventory= inventory(),
        crit_rate=10,
        crit_dmg=2,
        coord=[0,0],
        max_hp=100
    )

    cursor.execute('''SELECT * FROM player WHERE name = ?''', (name,))
    player_data = cursor.fetchone()
    if player_data:
        play.hp = player_data[1]
        play.atk = player_data[2]
        play.defense = player_data[3]
        play.level = player_data[4]
        play.crit_rate = player_data[5]
        play.crit_dmg = player_data[6]
        play.xp = player_data[7]
        play.max_hp = player_data[8]

    play.inventory.add(carte())

    cursor.execute('''SELECT * FROM potion''')
    potion_data = cursor.fetchall()
    for potion in potion_data:
        if potion[2] == "hp":
            play.inventory.add(potion_hp(potion[0]))
        elif potion[2] == "force":
            play.inventory.add(potion_force(potion[0]))
        elif potion[2] == "defense":
            play.inventory.add(potion_defense(potion[0]))

    cursor.execute('''SELECT * FROM arme''')
    arme_data = cursor.fetchall()
    for arme in arme_data:
        play.inventory.add(epee(arme[0], arme[1], arme[3]))


    cursor.execute('''SELECT * FROM coord WHERE name = ?''', (name,))
    coord_data = cursor.fetchone()
    if coord_data:
        play.coord[1] = coord_data[1]
        play.coord[0] = coord_data[2]

    carte_map = None

    cursor.execute('''SELECT * FROM map''')
    map_data = cursor.fetchone()
    if map_data:
        carte_map = map_data[0]

    dbsqlite.commit()
    dbsqlite.close() 

    pygame.mixer.init()

    return play, carte_map
    
def createtablesql():
    
    dbsqlite = sqlite3.connect('./save.sql')
    cursor = dbsqlite.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS player (
    name TEXT PRIMARY KEY,
    hp INTEGER,
    attck INTEGER,
    defense INTEGER,
    level INTEGER,
    crit_rate INTEGER,
    crit_dmg INTEGER,
    xp INTEGER,
    max_hp INTEGER
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS potion (
    name TEXT PRIMARY KEY,
    description TEXT,
    type TEXT,
    point INTEGER
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS arme (
    name TEXT PRIMARY KEY,
    description TEXT,
    type TEXT,
    atk INTEGER
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS coord (
    name TEXT PRIMARY KEY,
    x INTEGER,
    y INTEGER
    )''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS map (
    name TEXT PRIMARY KEY
    )''')

    dbsqlite.commit()
    dbsqlite.close() 