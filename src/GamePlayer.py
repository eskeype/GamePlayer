class GamePlayer:

	def __init__(self):

		# Gets filled in by a Match object
		
		self.turn = None
		self.game = None


	def play_move(self):
		# NEEDS TO BE OVERRIDDEN
		# Must update board corresponding to a player move
		pass

	def finalize(self):
		pass