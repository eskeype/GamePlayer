from Game import Game
class TicTacToe(Game):

	def __init__(self):
		self.board = [0 for i in range(9)]

	def valid_moves(self, player):
		return [i for i,mark in enumerate(self.board) if mark==0]

	def winner(self):

		"""
		Returns player id (1 or 2) of winner if a winner can be determined

		If no winner can be determined, return 0 
		"""

		#check rows and columns for win conditions
		for i in range(3):

			#Checks the i'th row
			if self.board[3*i] == self.board[3*i + 1] == self.board[3*i + 2]:
				return self.board[3*i]

			#checks the i'th column
			if self.board[i] == self.board[3+i] == self.board[6+i]:
				return self.board[i]

		if self.board[0] == self.board[4] == self.board[8]:
			return self.board[0]

		if self.board[2]== self.board[4] == self.board[6]:
			return  self.board[2]
		
		#No win condition was detected, return 0
		return 0

	def draw(self):

		"""
		Returns true when a winner has not been determined and no more valid moves remain
		"""
		
		return not self.valid_moves(1) and self.winner() == 0

	def update_board(self, player, move):

		"""
		Updates self.board according to a given player's move
		(e.g. player 1 occupies a space on the board)
		"""

		# It may be worth asserting that a move is valid
		# Maybe if a player attempts an invalid move, they
		# get an instant DQ?

		self.board[move] = player

	def board_to_string(self):

		"""
		Returns a string represntation of self.board

		Player 1's moves are represented as X

		Player 2's moves are represented as O

		Unoccupied spaces are represented as _ 
		"""
		
		out = []
		for i in range(3):
			line = []
			for j in range(3):
				
				if self.board[j + 3*i] == 0:
					line.append("_")
				
				elif self.board[j+ 3*i] == 1:
					line.append("X")
				
				else:	
					line.append("O")
			
			out.append("\t".join(line))

		return "\n".join(out)

	def clone(self):
		
		"""
		Returns a deep copy of self.
		"""
		
		cln = TicTacToe()
		cln.board = list(self.board)
		return cln


	def __eq__(self, other):
		
		return type(self) == type(other) and self.board == other.board

	def __hash__(self):

		return hash(tuple(self.board))
