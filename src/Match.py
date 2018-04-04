from TicTacToe import *
from OtherPlayers import *
from PerfectPlayer import *
from MatchboxPlayer import *
import pickle
import os.path
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
			#print("MOVE MADE: " + str(player_move))
			#self.move_histories[current_player].append((board, player_move))

			board = update_board(board, player_move, current_player)

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

FILENAME = "move_distribution.pickle"

if __name__ == "__main__":


	if os.path.isfile(FILENAME):
		move_distribution_file = open(FILENAME,"r")
		move_distribution = pickle.load(move_distribution_file)
		move_distribution_file.close()
	else:
		move_distribution = {}

	n = int(raw_input("Input a number of training games: "))

	wins = 0
	draws = 0
	for i in range(n):

		player2 = RandomGamePlayer()
		player1 = MatchboxGamePlayer(1,move_distribution)

		match = Match(player1,player2)

		wins += 1 if match.play(False) == 1 else 0
		draws += 1 if match.play(False) == 0 else 0

	print("Wins: {} Losses: {} Draws: {}".format(wins, n - wins - draws, draws))

	output_file = open(FILENAME,"w")
	pickle.dump(move_distribution, output_file)
	output_file.close()

