
from RandomizedCollection import RandomizedCollection
import random
from TicTacToe import *

#dictionary: board represntation -> randomized collection (matchbox)

class MatchboxGamePlayer:
	def __init__(self, player_id, move_distribution = {}):
		self.move_distribution = move_distribution
		self.move_history = [] # list of (board, move I made)
		self.player_id = player_id

	def make_choice(self, player,board):
		tup_board = tuple(board)
		if tup_board not in self.move_distribution:
			distribution = RandomCollection()
			
			valid_moves_list = valid_moves(board)

			for i in valid_moves_list:
				for i in range(len(valid_moves_list) + 1):
					distribution.insert(i)

			self.move_distribution[tup_board] = distribution

		elif self.move_distribution[tup_board].empty():
			return random.choice(valid_moves(board))

		move_choice = self.move_distribution[tup_board].getRandom()
		self.move_history.append( (tup_board, move_choice) )

		return move_choice

	def train(self, winner):
		if winner == self.player_id:
			#reward
			for move in self.move_history:
				self.move_distribution[move[0]].insert(move[1])

		elif winner == 3 - self.player_id:
			#punish (kinky)
			for move in self.move_history:
				self.move_distribution[move[0]].remove(move[1])




