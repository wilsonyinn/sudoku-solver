board = [
    [0, 9, 0, 7, 5, 1, 0, 2, 3],
    [2, 1, 8, 6, 0, 3, 7, 5, 4],
    [0, 0, 0, 4, 0, 2, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 9, 2],
    [0, 0, 0, 5, 0, 0, 3, 8, 0],
    [3, 0, 0, 8, 2, 0, 5, 0, 6],
    [0, 0, 0, 0, 7, 0, 0, 4, 8],
    [0, 4, 9, 0, 0, 0, 0, 7, 0],
    [0, 2, 0, 0, 0, 5, 6, 3, 1],
]
 
#Sudoku constraints
#each column must contain one of each of the numbers 1-9
#each row much contain one of each of the numbers 1-9
#there are nine 3x3 sub squares within the board and each subsquare must contain one of each of the numbers 1-9

#Backtracking Algorithm Steps
#1. pick an empty spot
#2. try a number until a number doesnt disobey the constraints
#3. repeat on next empty spot until dead end
#4. backtrack 

def solve(board):
    find = find_empty(board)    
    if not find:             #base case happens when there are no more empty spots
        return True          #which means that a solution has been found
    else:
        row, col = find      

    for i in range(1,10):                   #testing the numbers from 1-9 for each empty spot
        if valid(board, i, (row, col)):     #
            board[row][col] = i             #set empty spot to a valid number
            if solve(board):                #recursively call this solve function
                return True                         #goes to next empty spot, tries for 1-9 
            board[row][col] = 0                     #continues until a dead end and returns back (backtracking, the rescursive functions unfolds)

    return False 

    


def find_empty(arr):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if (arr[i][j] == 0):
                return (i, j) #row, col
    #idk what to return if no empty spot is found
    return None

def print_board(arr):
    for i in range(len(arr)):
        if (i % 3 == 0):
            print("- - - - - - - - - - - - - - - - - ")
        for j in range(len(arr[i])):
            if (j % 3 == 0):
                print(" | ", end=" ")
            print(arr[i][j], end=" ")
        print(" | ", end=" ")
        print()
    print("- - - - - - - - - - - - - - - - - ")

def valid(board, num, pos):
    #check horizontal constraint
    for i in range(len(board)):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    #check vertical constraint
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    #check subsquare
    xbox = pos[1] // 3
    ybox = pos[0] // 3
    for i in range(ybox * 3, ybox * 3 + 3):
        for j in range(xbox * 3, xbox * 3 + 3):
            if (board[i][j] == num and (i,j) != pos):
                return False

    return True

print_board(board)
solve(board)
print_board(board)