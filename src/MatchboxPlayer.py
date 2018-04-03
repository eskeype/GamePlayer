
from RandomizedCollection import RandomizedCollection
import random
from TicTacToe import *
import CPickle as pickle
# CPickle apparently works much faster than regular pickle on python 2.x. Python 3 auto uses it
from datetime import datetime

#dictionary: board represntation -> randomized collection (matchbox)

class MatchboxGamePlayer:
	def __init__(self, player_id, move_distribution = {}):
		if type(move_distribution) is str:
			#treat it like a filename 
			 #move_distribution_file = open(move_distribution, 'r')
			 #self.move_distribution = pickle.load(move_distribution_file)
			 #move_distribution_file.close()
			self.move_distribution = pickle.load( open( "move_distribution.p", "rb" ) )

		else: #it should be a dictionary	
			self.move_distribution = move_distribution

		self.move_history = [] # list of (board, move I made)
		self.player_id = player_id

	def move_choice(self, player,board):
		tup_board = tuple(board)
		if tup_board not in self.move_distribution:
			distribution = RandomizedCollection()
			
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
			#punish 
			for move in self.move_history:
				self.move_distribution[move[0]].remove(move[1])
		#out_file = open("move_distribition"+str(datetime.now())+".pickle", "w")
		#pickle.dump(self.move_distribution, out_file)
		pickle.dump( move_distribution, open( "move_distribution.p", "wb" ) )


		out_file.close()




