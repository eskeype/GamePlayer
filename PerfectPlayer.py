from TicTacToe import *

class PerfectGamePlayer:
	def __init__(self):
		self.game_tree = {}
	def make_move(self, player, board):
		tup_board = tuple(board)

		if tup_board not in self.game_tree:
			position_favors(tup_board,player,self.game_tree)

		current_valid_moves = valid_moves(board)
		out_move = current_valid_moves[0]
		count = 0
		#reservoir sampling
		for move in current_valid_moves:
			move_board = list(tup_board)
			move_board[move] = player
			tup_move_board = tuple(move_board)

			if self.game_tree[tup_move_board] == player:
				print("i already won!\n")
				return move

			if self.game_tree[tup_move_board] == 0:
				print("MOVE CANDIDATE: {}\n".format(move))
				count+=1
				if random.randint(1,count)==1:
					out_move = move

		return out_move


def position_favors(board, player, cache):

	if board in cache:
		return cache[board]

	outcome = winner[board]
	if outcome!=0:
		cache[board] = outcome
		return outcome

	if draw(board):
		cache[board] = 0
		return 0

	for move in valid_moves(board):
		board_list = list(board)
		board_list[move] = player
		new_board = tuple(board_list)

		losing = True

		if position_favors(new_board,3-player, cache)==player:
			cache[board] = player
			return player

		elif position_favors(new_board, 3-player, cache)!=(3-player):
			losing = False

	cache[board] = (3-player) if losing else 0
	return cache[board]

print(__name__)

if __name__ == "__main__":
	game_tree = {}
	starting_board = tuple([0]*9)
	position_favors(starting_board, 1, game_tree)

	for board in game_tree:
		print("{}\n\nwinner: {}".format(board_to_string(board),game_tree[board]))