from RandomizedCollection import RandomizedCollection
import random
from TicTacToe import *

class RandomGamePlayer:
	def __init__(self):
		pass
	def move_choice(self, player,board):
		return random.choice(valid_moves(board))
	def train(self, winner):
		pass

class HumanGamePlayer:
	def __init__(self):
		pass
	def move_choice(self, player, board):
		
		while True:

			try:
				move = int(raw_input("Player {}, input your move: ".format(player)))
				if move not in valid_moves(board):
					print("{} is not a valid move!\n".format(move))
				else:
					break

			except ValueError:
				print("Please enter an integer\n")
		return move
	def train(self, winner):
		pass
