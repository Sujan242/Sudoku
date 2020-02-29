import math

board =  [[8, 1, 0, 0, 3, 0, 0, 2, 7], 
            [0, 6, 2, 0, 5, 0, 0, 9, 0], 
            [0, 7, 0, 0, 0, 0, 0, 0, 0], 
            [0, 9, 0, 6, 0, 0, 1, 0, 0], 
            [1, 0, 0, 0, 2, 0, 0, 0, 4], 
            [0, 0, 8, 0, 0, 5, 0, 7, 0], 
            [0, 0, 0, 0, 0, 0, 0, 8, 0], 
            [0, 2, 0, 0, 1, 0, 7, 5, 0], 
            [3, 8, 0, 0, 7, 0, 0, 4, 2]]

def printBoard(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("---------------------")
        for j in range(len(board[i])):
            if j % 3 == 0 and j != 0:
                print("| ", end = "")
            print(board[i][j], end = ' ')
        print()

def isNumPossible(n, x, y):
    global board
    blockSize = int(math.sqrt(len(board)))
    for i in range(len(board)):
        if board[x][i] == n:
            return False
        if board[i][y] == n:
            return False
    for i in range(blockSize):
        for j in range(blockSize):
            if board[(x//blockSize)*blockSize + i][(y//blockSize)*blockSize + j] == n:
                return False

    return True

def sudoku():
    global board
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                for n in range(1, len(board) + 1):
                    if isNumPossible(n, i, j) == True:
                        board[i][j] = n
                        sudoku()
                        board[i][j] = 0
                return
    
    print("\nSolution is: ")
    printBoard(board)
  #  if input("more?") == 'n':
   #     exit

print("Trying to solve: \n")
printBoard(board)

sudoku()

