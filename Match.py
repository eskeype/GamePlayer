from TicTacToe import *
from OtherPlayers import *

class Match:
	def __init__(self, player1, player2):
		self.players = {1:player1, 2:player2}

	def play(self,verbose=True):
		board = tuple([0]*9)
		current_player = 1

		if verbose:
			print(board_to_string(board))
			print("\n")
		
		while not draw(board):
			
			board = update_board(board, self.players[current_player].move_choice(current_player, board), current_player)

			if verbose:
				print(board_to_string(board))
				print("\n")

			if is_winner(current_player,board):
				if verbose:
					print("Player {} won!".format(current_player))
				return current_player
			
			current_player = 3 - current_player

		if verbose:
			print("Draw game!")
		return 0

if __name__ == "__main__":
	player1 = RandomGamePlayer()
	player2 = HumanGamePlayer()

	match = Match(player1,player2)
	#scoreboard = {0:0, 1:0, 2:0}
	#for i in range(1000):
	#	scoreboard[game.play()]+=1
	match.play()
	#print(scoreboard)