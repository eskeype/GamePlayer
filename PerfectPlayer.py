from TicTacToe import *
import random

class PerfectGamePlayer:
	def __init__(self):
		self.game_tree = {}
	def move_choice(self, player, board):
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
				#print("i already won!\n")
				return move

			if self.game_tree[tup_move_board] == 0:
				#print("MOVE CANDIDATE: {}\n".format(move))
				count+=1
				if random.randint(1,count)==1:
					out_move = move

		return out_move
	def train(self, winner):
		pass


def position_favors(board, player, game_tree):

	if board in game_tree:
		return game_tree[board]

	outcome = winner(board)
	if outcome!=0:
		game_tree[board] = outcome
		return outcome

	if draw(board):
		game_tree[board] = 0
		return 0

	losing = True
	for move in valid_moves(board):
		new_board = update_board(board, move, player)

		if position_favors(new_board,3-player, game_tree)==player:
			game_tree[board] = player
			return player

		elif position_favors(new_board, 3-player, game_tree)!=(3-player):
			losing = False

	game_tree[board] = (3-player) if losing else 0
	return game_tree[board]

 #Also build "first winning move" perfect game player instead of forking


if __name__ == "__main__":
	game_tree = {}
	starting_board = tuple([0]*9)
	position_favors(starting_board, 1, game_tree)

	for board in game_tree:
		print("{}\n\nwinner: {}".format(board_to_string(board),game_tree[board]))