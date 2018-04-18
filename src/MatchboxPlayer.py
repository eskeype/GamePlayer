from RandomizedCollection import RandomizedCollection
from GamePlayer import GamePlayer
import random

#dictionary: board represntation -> randomized collection (matchbox)

class MatchboxGamePlayer(GamePlayer):
	def __init__(self, move_distribution = {}):

		self.turn = None
		self.game = None

		self.move_distribution = move_distribution
		self.move_history = [] # list of (board, move I made)

	def play_move(self):
		game_clone = self.game.clone()

		if game_clone not in self.move_distribution:
			
			matchbox = RandomizedCollection()
			
			valid_moves_list = game_clone.valid_moves()

			#insert beads into matchbox
			for i in valid_moves_list:
				for j in range(len(valid_moves_list)):
					matchbox.insert(i)

			self.move_distribution[game_clone] = matchbox


		if self.move_distribution[game_clone].empty():
			move = random.choice(game_clone.valid_moves())

		else:
			move = self.move_distribution[game_clone].getRandom()
			self.move_history.append( (game_clone, move) )

		self.game.update_board(self.turn, move)

	def finalize(self):

		# This is where the matchbox player is trained

		winner = self.game.winner()

		if winner == self.turn:
			#reward
			for move in self.move_history:
				self.move_distribution[move[0]].insert(move[1])

		elif winner == 3 - self.turn:
			#punish 
			for move in self.move_history:
				self.move_distribution[move[0]].remove(move[1])





