board = [
	[None, None, None],
	[None, None, None],
	[None, None, None]
]

def print_board():
	for row in board:
		print row

def x_turn():
	move = []
	move_row = raw_input("X, what row would you like to place your piece on? ")
	move_col = raw_input("X, what column would you like to place your piece on? ")

	move.append(int(move_row) - 1)
	move.append(int(move_col) - 1)

	board[move[0]][move[1]] = "X"

	print_board()
def o_turn():
	move_row = raw_input("O, what row would you like to place your piece on? ")
	move_col = raw_input("O, what column would you like to place your piece on? ")


print_board()
x_turn()