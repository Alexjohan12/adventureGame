import random

class Player:
 def __init__(self):
  self.name = input("Choose your name:")
  self.HP = 100
  self.exp = 0
  self.player_coins = 0
  self.enemies_killed = 0