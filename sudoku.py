#sudoku solver
#default sudoku board may change to another for different output
board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]

# print(board)
# visually see the board
def print_board(puzzle):
    for r in range(len(puzzle)):
        if r % 3 == 0 and r != 0:
            print('- - - - - - - - - - -')
            # after every 3 rows this will print to show the actual board
        for c in range(len(puzzle[0])):
            if c % 3 == 0 and c != 0:
                print('|', end="")
            if c == 8:
                print(puzzle[r][c])
            else:
                print(str(puzzle[r][c]) + " ", end="")

def find_empty(puzzle):
    #find next row or column that is empty
    #return row, column, tuple None if there isn't
    for r in range(9): #0-8
        for c in range(9):
            #return these items
            if puzzle[r][c] == 0:
                return(r, c)
    return(None) #if no empty spaces

def num_valid(puzzle, num, row, column):
    #return true if num is valid
    row_num = puzzle[row]
    if num in row_num:
        return False
    col_num = []
    for i in range(9):
        #add value at the ith row at the column
        col_num.append(puzzle[i][column])
    #if number used return false
    if num in col_num:
        return False
    #square matrix, find index of row and column and iterate
    #3 - to get into another box 
    initial_row = (row // 3) * 3
    initial_col = (column // 3) * 3
    for r in range(initial_row, initial_row + 3):
        for c in range(initial_col, initial_col + 3):
            if puzzle[r][c] == num:
                return False
    #this means valid
    return True

def sudoku_solver(puzzle):
    #check if space is empty and if there is a valid number
    #when reach end, no where to go, board is complete
    look = find_empty(puzzle)
    if not look:
        return True #check if found solution or not
    else:
        row, column = look
    for r in range(1, 10): #add values into board and check if values work
        if num_valid(puzzle, r, row, column):
            #if valid put values in board
            puzzle[row][column] = r

            #recursion, keep checking till numbers are looped to see which fit in empty space
            if sudoku_solver(puzzle):
                return True
            puzzle[row][column] = 0 #reset value
    return False

print_board(board)
sudoku_solver(board)
print("This is the solved sudoku puzzle")
print_board(board)




