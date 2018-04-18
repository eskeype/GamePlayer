import random
from GamePlayer import GamePlayer

class RandomGamePlayer(GamePlayer): 

	def play_move(self):

		self.game.update_board(self.turn, random.choice(self.game.valid_moves()))
	
class HumanGamePlayer(GamePlayer):

	def play_move(self):
		
		move = None

		while move is None:

			try:
				move = int(raw_input("Player {}, input your move: ".format(self.turn)))

			except ValueError:
				print("Please enter an integer\n")

		self.game.update_board(self.turn, move)

