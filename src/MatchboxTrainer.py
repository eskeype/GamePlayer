import os.path
import pickle

from Match import Match
from OtherPlayers import *
from TicTacToe import TicTacToe
from MatchboxPlayer import MatchboxGamePlayer


FILENAME = "../player_configs/matchbox_parameters.pickle"

if __name__ == "__main__":


	if os.path.isfile(FILENAME):
		move_distribution_file = open(FILENAME,"r")
		move_distribution = pickle.load(move_distribution_file)
		move_distribution_file.close()
	else:
		move_distribution = {}

	n = int(raw_input("Input a number of training games: "))

	scoreboard = [0,0,0]
	for i in range(n):

		player1 = MatchboxGamePlayer(move_distribution)
		player2 = RandomGamePlayer()
		game = TicTacToe()

		match = Match(game, player1,player2)

		result = match.play(False)
		
		scoreboard[result] += 1

	print("Player 1 wins: {} Player 2 wins: {} Draws: {}\n".format(scoreboard[1], scoreboard[2], scoreboard[0]))

	output_file = open(FILENAME,"w")
	pickle.dump(move_distribution, output_file)
	output_file.close()
