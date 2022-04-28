from random import randrange

#Prints out the current board
def display_board(board):
	print("+---" * 3,"+", sep="")
	for row in range(3):
		for col in range(3):
			print("| " + str(board[row][col]) + " ", end="")
		print("|")
		print("+---" * 3,"+",sep="")

#Take user input for their move
def play_move(board):
	ok = False	
	while not ok:
		move = input("Enter your move: ") 
		
		#Check if user input is valid
		ok = len(move) == 1 and move >= '1' and move <= '9' 
		if not ok:
			print("Invalid move - try again ")
			continue
		
		#set players move
		move = int(move) - 1 	
		row = move // 3 	
		col = move % 3

		#Check if board position is not already occupied		
		pos = board[row][col]	
		valid = pos not in ['O','X'] 
		if not valid:	# it's occupied - to the input again
			print("Position already occupied - try again")
			continue
	board[row][col] = 'X' 	

#Iterate through board, if spot is free append new tuple to list free
def create_open(board):
	free = []	
	for row in range(3):
		for col in range(3): 
			if board[row][col] not in ['O','X']: 
				free.append((row,col)) 
	return free

#Check for winner
def victory(board,marker):
	if marker == "O":	
		winner = 'computer'	
	elif marker == "X": 
		winner = 'you'	
	else:
		winner = None

	diag1 = diag2 = True 
	for i in range(3):
		#Check horizontal and vertical
		if board[i][0] == marker and board[i][1] == marker and board[i][2] == marker:	
			return winner
		if board[0][i] == marker and board[1][i] == marker and board[2][i] == marker:
			return winner
		#Check diagonals
		if board[i][i] != marker:
			diag1 = False
		if board[2 - i][2 - i] != marker:
			diag2 = False
	if diag1 or diag2:
		return winner
	return None

#Randomly selects a plce to play from a list of open spaces
def draw_move(board):
	open = create_open(board) 
	cnt = len(open)
	if cnt > 0:
		this = randrange(cnt)
		row, col = open[this]
		board[row][col] = 'O'

#Create an empty board
board = [ [3 * j + i + 1 for i in range(3)] for j in range(3) ] 

free = create_open(board)

#Human takes first turn, game continues till someone wins or no more open spots to play
human_turn = True
while len(free):
	display_board(board)
	if human_turn:
		play_move(board)
		victor = victory(board,'X')
	else:	
		draw_move(board)
		victor = victory(board,'O')
	if victor != None:
		break
	human_turn = not human_turn		
	free = create_open(board)
display_board(board)

#Display win/lose message
if victor == 'you':
	print("Yay, you won!")
elif victor == 'computer':
	print("So Sorry, you lost!")
else:
	print("Tie!")