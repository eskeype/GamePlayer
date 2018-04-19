from Match import Match
from TicTacToe import TicTacToe
from MatchboxPlayer import MatchboxGamePlayer
from OtherPlayers import RandomGamePlayer, HumanGamePlayer

import pickle
import os.path


CONFIG_FILENAME = "../player_configs/matchbox_parameters.pickle"

if __name__ == "__main__":

	print("Welcome! In this demonstration, we will see how well a Matchbox reinforcement learning agent can learn Tic Tac Toe\n")

	train = False
	while True:

		usr_in = raw_input("Do you want to train the Matchbox player on your machine? (Y/n): ").strip().upper()


		if usr_in == 'Y':
			train = True
			break
		elif usr_in == 'N':
			break

		print("Please input Y or N")

	config = {}

	if train:
		cycles = int(input("Enter a number of training cycles (It becomes notably better than a random player after 10,000 cycles): "))

		for i in range(cycles):
			Match(TicTacToe(), MatchboxGamePlayer(config), RandomGamePlayer()).play(verbose = False, finalize = True)

		print("\nThe Matchbox player has played {} games against a random game player\n".format(cycles))

	else:
		if not os.path.isfile(CONFIG_FILENAME):
			raise ValueError("matchbox_parameters.pickle was not found in the player_configs directory.")

		config_file = open(CONFIG_FILENAME, "r")
		config = pickle.load(config_file)
		config_file.close()

		print("The Matchbox player has been loaded with parameters learned from 500,000 games\n")


	print("The Matchbox player will now play 1000 games against a random player and see how it fares")
	print("NOTE: The learning feature for the Matchbox player will be turned off for these games\n")

	scoreboard = [0,0,0]
	for i in range(1000):
		result = Match(TicTacToe(), MatchboxGamePlayer(config), RandomGamePlayer()).play(verbose = False, finalize = False)

		scoreboard[result] += 1

	print("Wins: {}, Losses: {}, Draws: {}\n".format(scoreboard[1], scoreboard[2], scoreboard[0]))

	print("Now you can play with the Matchbox player. You are player 2")	
	Match(TicTacToe(), MatchboxGamePlayer(config), HumanGamePlayer()).play(verbose = True, finalize = False)



