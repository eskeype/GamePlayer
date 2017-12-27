
from RandomizedCollection import RandomizedCollection
import random
from TicTacToe import *

class MatchboxGamePlayer:
	def __init__(self, move_distribution = {}):
		self.move_distribution = move_distribution

	def make_move(self, player,board):
		tup_board = tuple(board)
		if tup_board not in move_distribution:
			distribution = RandomCollection()
			
			valid_moves_list = valid_moves(board)

			for i in valid_moves_list:
				for i in range(len(valid_moves_list)):
					distribution.insert(i)

			self.move_distribution[tup_board] = distribution

		return self.move_distribution[tup_board].getRandom()
