from RandomizedCollection import RandomizedCollection
import random
from TicTacToe import *

class RandomGamePlayer:
	def __init__(self):
		pass
	def move_choice(self, player,board):
		return random.choice(valid_moves(board))

class HumanGamePlayer:
	def __init__(self):
		pass
	def move_choice(self, player, board):
		return int(raw_input("Player {}, input your move: ".format(player)))