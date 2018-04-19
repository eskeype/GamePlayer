class GamePlayer:

	def __init__(self):

		# Every GamePlayer should have a 'turn' attribute and a 'game' attribute

		# The turn attribute refers to which turn the player has in a game - either first or second
		# The game attribute is an instance of a game (e.g. an instance of class TicTacToe)

		# GamePlayers are operated by Match objects. A Match object takes two Game Players and a 
		# Game instance, 

		self.turn = None
		self.game = None


	def match_initializer(self, turn, game):
		self.turn = turn
		self.game = game

	def play_move(self):
		# NEEDS TO BE OVERRIDDEN
		# Must update board corresponding to a player move
		pass

	def finalize(self):
		pass