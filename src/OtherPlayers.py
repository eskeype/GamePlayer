import random
from GamePlayer import GamePlayer

# Currently only applies to TicTacToe

class RandomGamePlayer(GamePlayer): 

	def play_move(self):

		self.game.update_board(self.turn, random.choice(self.game.valid_moves(self.turn)))
	
class HumanGamePlayer(GamePlayer):
	def play_move(self):
		
		row = None

		while row is None:

			try:
				row = int(raw_input("Player {}, input the row for your move (1, 2, or 3): ".format(self.turn)))

			except ValueError:
				print("Please enter an integer\n")
		
		col = None

		while col is None:

			try:
				col = int(raw_input("Player {}, input the column for your move (1, 2, or 3): ".format(self.turn)))

			except ValueError:
				print("Please enter an integer\n")

		self.game.update_board(self.turn, (col - 1) + 3 * (row - 1))

