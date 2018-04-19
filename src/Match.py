
class Match:
	def __init__(self, game, player1, player2):

		self.game = game


		player1.match_initializer(1, game)

		player2.match_initializer(2, game)

		self.players = {1:player1, 2:player2}


	def play(self, verbose = True, finalize = True):

		current_player = 1

		if verbose:
			print( "{}\n".format(self.game.board_to_string()))
		
		while not (self.game.draw() or self.game.winner() != 0):
			
			self.players[current_player].play_move()

			if verbose:
				print( "{}\n".format(self.game.board_to_string()))
			
			current_player = 3 - current_player

		
		if finalize:
			
			# Finalization methods are called here
			# These can be used to train learning game players
			# or do other bookkeeping at the end of a game

			# Finalization can be skipped, so that if a Match
			# is being played for validation, the training method
			# does not need to be called

			self.players[1].finalize()
			self.players[2].finalize()

		winner = self.game.winner()


		if winner != 0:
			if verbose:
				print("Player {} won!\n".format(winner))
			return winner

		elif verbose:
			#draw game
			print("Draw Game!\n")
		
		return 0

