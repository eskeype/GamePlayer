def valid_moves(board):
	return [i for i,mark in enumerate(board) if mark==0]

def is_winner(player, board):
	for i in range(3):
		if board[3*i]==board[3*i + 1]==board[3*i + 2]==player:
			return True
		if board[i]==board[3+i]==board[6+i]==player:
			return True
	if (board[0]==board[4]==board[8]==player) or (board[2]==board[4]==board[6]==player):
		return True
	return False

def winner(board):
	if is_winner(1,board):
		return 1
	if is_winner(2,board):
		return 2
	return 0

def draw(board):
	return not valid_moves(board) and not winner(board) == 0

def update_board(board, move, player):

	list_board = list(board)
	list_board[move] = player
	return tuple(list_board)

def board_to_string(board):
	out = []
	for i in range(3):
		line = []
		for j in range(3):
			if board[j + 3*i] == 0:
				line.append("_")
			elif board[j+ 3*i] == 1:
				line.append("X")
			else:
				line.append("O")
		out.append("\t".join(line))
	return "\n".join(out)