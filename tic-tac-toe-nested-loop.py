SIZE = 3
board = [] # Start with an empty List
for y in range(SIZE):
    # Each element in the board will also be a List
    board.append([])        
    for x in range(SIZE):
        # Fill our inner Lists with the coordinates
        board[y].append("[%d][%d]" % (y, x))

# Print the board as a grid
for row in board:
    for column in row:
        print("%s  " % column, end="")
    print("\n")

print("\n\nPlayer X is moving.\n\n")
board[0][2] = "X"

# Print the board as a grid
for row in board:
    for column in row:
        print("%s  " % column, end="")
    print("\n")