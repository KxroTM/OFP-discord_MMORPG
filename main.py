from assets.event.introduction import intro
from assets.object.game import village_spawn
import argparse


parser = argparse.ArgumentParser(description="Lancer le jeu avec ou sans une carte spécifique.")
parser.add_argument('-i', '--input', type=str, help="Nom de la carte à charger")

args = parser.parse_args()

if args.input:
    village_spawn(True)
else:
    intro() 
