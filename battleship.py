'''
Codecademy - Learn basic Pyhon https://www.codecademy.com/learn/python 
Assignment: Battleship
File: battleship.py
'''
# Create a square board size 5, load all cells with O (letter O upper case)
board = []
for x in range(0,5):
  board.append(["O"*5]
 
# print board to see
def print_board(board): # "board" arg is a list
  for row in board:
    print "".join(row)

print_board(board)

def random_row(board):
# return a random integer. This will be used as the row index of the move
# board is a list of lists, square size 5
  return randint(0, len(board) - 1)

def random_col(board)
# Similar to random_row above
  return randint(0, len(board) - 1)
 
ship_row = random_row(board)
ship_col = random_col(board)
guess_row = int(raw_input("Guess Row: "))
guess_col = int(raw_input("Guess Col: "))

print ship_row
print_ship_col

if guess_row == ship_row and guess_col == ship_col:
  print "Congratulations! You sank my battleship!"
else:
  if guess_row not in range(5) or guess_col not in range(5):
    print "Oops, that is not even in the ocean."
  elif board[guess_row][guess_col] == 'X':
    print "You guessed that one already."
  else:
    print "You missed my battleship!"
    board[guess_row][guess_col] = 'X'
  print_board(board)
# end  
