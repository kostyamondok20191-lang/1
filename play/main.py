import random

from monster import Golem, dragon
from arena import start_tournament

print("Симулятор гладіаторських боїв активовано.")

player_golem  = Golem("Голем", 200, 16, 10, 5)
enemy_dragon = dragon("Дракон", 210, 15, 7)

start_tournament(player_golem, enemy_dragon)