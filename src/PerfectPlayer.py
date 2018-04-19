from GamePlayer import GamePlayer
import random

class PerfectGamePlayer(GamePlayer):
	def __init__(self, game_tree = {}):
		
		self.turn = None
		self.game = None
		self.game_tree = game_tree

	def play_move(self):

		count = 0

		# reservoir sampling
		# If board_tuple.valid_moves() is empty, something is wrong
		candidate_move = None

		for move in self.game.valid_moves():
				
			candidate_game = self.game.clone()
			candidate_game.update_board(self.turn, move)

			favors = position_favors(3 - self.turn, candidate_game, self.game_tree)

			if favors == self.turn:
				self.game.update_board(self.turn, move)
				return

			elif favors == 0:
				count += 1
				if random.randint(1,count) == 1:
					candidate_move = move

		#This would be a good time to assert that candidate_move is not null
		self.game.update_board(self.turn, candidate_move)


def position_favors(player, game, game_tree):
	
	if game in game_tree:
		return game_tree[game]

	winner = game.winner()

	if winner != 0:
		game_tree[game] = winner
		return winner

	if game.draw():
		game_tree[game] = 0
		return 0

	# check all of the child cases
	# if they are all losing positions, this position is as well
	# if any of them are winning positions, this is a winning position
	other_player = 3 - player
	lose_count = 0
	for move in game.valid_moves():
		candidate_game = game.clone()
		candidate_game.update_board(player, move)

		favors = position_favors(other_player, candidate_game, game_tree) 

		if favors == player:
			game_tree[game] = player
			return player
		
		elif favors == other_player:
			lose_count += 1


	if lose_count == len(game.valid_moves()):
		game_tree[game] = other_player
		return other_player

	game_tree[game] = 0
	return 0

 #Also build "first winning move" perfect game player instead of forking


if __name__ == "__main__":
	game_tree = {}
	starting_board = tuple([0]*9)
	position_favors(starting_board, 1, game_tree)

	for board in game_tree:
		print("{}\n\nwinner: {}".format(board_to_string(board),game_tree[board]))