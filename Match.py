from TicTacToe import *
from OtherPlayers import *
from PerfectPlayer import *

#MAKE THIS RETURN LIST OF MOVES MADE

class Match:
	def __init__(self, player1, player2):
		self.players = {1:player1, 2:player2}
		#self.move_histories = {1:[], 2:[]}

	def play(self,verbose=True):
		board = tuple([0]*9)
		current_player = 1

		if verbose:
			print(board_to_string(board))
			print("\n")
		
		while not draw(board):
			
			player_move = self.players[current_player].move_choice(current_player, board)
			#self.move_histories[current_player].append((board, player_move))

			board = update_board(board, player_move, board, current_player)

			if verbose:
				print(board_to_string(board))
				print("\n")

			if is_winner(current_player,board):
				if verbose:
					print("Player {} won!".format(current_player))

				self.players[current_player].train(current_player)
				self.players[3 - current_player].train(current_player)
				return current_player
			
			current_player = 3 - current_player

		if verbose:
			print("Draw game!")

		
		return 0

if __name__ == "__main__":
	player1 = PerfectGamePlayer()
	player2 = RandomGamePlayer()

	match = Match(player1,player2)

	match.play()
	#scoreboard = {0:0, 1:0, 2:0}
	#for i in range(1000):
	#	scoreboard[match.play(False)] +=1
	#print scoreboard
