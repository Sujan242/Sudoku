board = [   [3, 0, 6, 5, 0, 8, 4, 0, 0],
            [5, 2, 0, 0, 0, 0, 0, 0, 0],  
            [0, 8, 7, 0, 0, 0, 0, 3, 1],  
            [0, 0, 3, 0, 1, 0, 0, 8, 0],  
            [9, 0, 0, 8, 6, 3, 0, 0, 5],  
            [0, 5, 0, 0, 9, 0, 6, 0, 0],  
            [1, 3, 0, 0, 0, 0, 2, 5, 0],  
            [0, 0, 0, 0, 0, 0, 0, 7, 4],  
            [0, 0, 5, 2, 0, 6, 3, 0, 0]
        ]
modifyList = []

def printBoard(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("---------------------")
        for j in range(len(board[i])):
            if j % 3 == 0 and j != 0:
                print("| ", end = "")
            print(board[i][j], end = ' ')
        print()
printBoard(board)

def isNumValid(board, row, column, num):
    
    for i in range(len(board)):
        if num == board[i][column]:
            return -1

    for j in range(len(board[row])):
        if num == board[row][j]:
            return -1
    squaresize = int(len(board) ** (0.5))

    for i in range( squaresize):
        for j in range( squaresize):
            if num == board[ (row // squaresize) * squaresize + i][(column // squaresize) * squaresize + j]:
                return -1
    
    return 0

def sudokuSolver(board, i, j, n):
    
    while i <= 9 :
        while j <= 9:

            if board[i][j] == 0:
                while n <= 9:
                    if isNumValid(board, i, j, n) == 0:
                        board[i][j] = n
                        modifyList.append([i, j, n])
                        break
                    if n == 9:
                        itemp = modifyList[-1][0]
                        jtemp = modifyList[-1][1]
                        ntemp = modifyList[-1][2]
                        board[itemp][jtemp] = 0
                        modifyList.pop()
                        
                        return                  
                    n += 1




sudokuSolver(board, 0, 0, 1)
print("--------------------")
print("Solution:")
print("--------------------")
printBoard(board)