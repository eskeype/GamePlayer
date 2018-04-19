class Game:

	def __init__(self):
		"""
		Initializes the game play to a starting state
		"""
		pass

	def valid_moves(self, player):
		"""
		Returns an iterable of the valid moves that can be made on a board for
		the input 'player'
		"""
		pass

	def winner(self):

		"""
		Returns player id (1 or 2) of winner if a winner can be determined

		If no winner can be determined, return 0 
		"""

		pass

	def draw(self):

		"""
		Returns true when a winner has not been determined and no more valid moves remain
		"""
		
		pass

	def update_board(self, player, move):

		"""
		Updates self.board according to a given player's move
		(e.g. player 1 occupies a space on the board)

		This method should be called by a GamePlayer's play_move method
		"""

		# It may be worth asserting that a move is valid
		# Maybe if a player attempts an invalid move, they
		# get an instant DQ?

		pass

	def board_to_string(self):

		"""
		Returns a string represntation of self.board

		Player 1's moves are represented as X

		Player 2's moves are represented as O

		Unoccupied spaces are represented as _ 
		"""
		
		pass

	def clone(self):
		
		"""
		Returns a deep copy of self.
		"""
		
		pass


	# Some of the AI game players (currently PerfectGamePlayer and MatchboxGamePlayer) use dictionaries
	# to help make decisions in their 'play_move' methods. Override __hash__ and __eq__ by ensuring that
	# equivalent game states (including perhaps board configuration and player's turn, if necessary)
	# are equal using '==', and ensure that the __hash__ method satisfies the usual constraints with 
	# respect to __eq__.

	# Note: Game objects are mutable, but they will be used as dictionary keys. In PerfectGamePlayer
	# and MatchboxGamePlayer, issues are avoided by using Game clones as keys, where the state of these
	# clones are never changed

	# A PerfectGamePlayer will likely still work without these methods filled in (but it will be slow)
	# A MatchboxGamePlayer will be unable to learn without these methods filled in

	#def __eq__(self, other):

	#def __hash__(self):