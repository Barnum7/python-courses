# Defining my Variables
board = [
	[None, None, None],
	[None, None, None],
	[None, None, None]
]

turn = "X"

# Defining my Functions
def print_board():
	for row in board:
		print row

def x_turn():
	move = []
	move_row = raw_input("X, what row would you like to place your piece on? ")
	move_col = raw_input("X, what column would you like to place your piece on? ")

	move.append(int(move_row) - 1)
	move.append(int(move_col) - 1)

	if board[move[0]][move[1]] == None:
		board[move[0]][move[1]] = "X"
	else:
		print "That's an illegal move!"
		print_board()
		x_turn()

	print_board()
	turn = "O"
	evaluate_board(turn)

def o_turn():
	move = []
	move_row = raw_input("O, what row would you like to place your piece on? ")
	move_col = raw_input("O, what column would you like to place your piece on? ")

	move.append(int(move_row) - 1)
	move.append(int(move_col) - 1)

	if board[move[0]][move[1]] == None:
		board[move[0]][move[1]] = "O"
	else:
		print "That's an illegal move!"
		print_board()
		o_turn()

	print_board()
	turn = "X"
	evaluate_board(turn)

def evaluate_board(turn):
	if board[0][0] == board[0][1] == board[0][2] != None:
		print "This game is over!", "Player", board[0][0], "wins!"
	elif board[1][0] == board[1][1] == board[1][2] != None:
		print "This game is over!", "Player", board[1][0], "wins!"
	elif board[2][0] == board[2][1] == board [2][0] != None:
		print "This game is over!", "Player", board[2][0], "wins!"
	elif board[0][0] == board[1][0] == board[2][0] != None:
		print "This game is over!", "Player", board[0][0], "wins!"
	elif board[0][1] == board[1][1] == board[2][1] != None:
		print "This game is over!", "Player", board[0][1], "wins!"
	elif board[0][2] == board[1][2] == board[2][2] != None:
		print "This game is over!", "Player", board[0][2], "wins!"
	elif board[0][0] == board[1][1] == board[2][2] != None:
		print "This game is over!", "Player", board[0][0], "wins!"
	elif board[2][0] == board[1][1] == board[0][2] != None:
		print "This game is over!", "Player", board[2][0], "wins!"
	elif any_legal_mov
		print "This game ends in a draw!"
	else:
		determine_turn(turn)

def determine_turn(turn):
	if turn == "X":
		x_turn()
	else:
		o_turn()

def any_legal_moves():
	legal_moves = False

	for row in board:
		for cell in row:
			if cell == None:
				legal_moves = True

	return legal_moves

# Calling my functions
print_board()
determine_turn(turn)