unsolved_board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7],
]


def solve_sudoku(board):
    # using recursiont

    # base Case
    findEmptySquare = find_Zero(board)
    if not findEmptySquare:
        return True
    else:
        row, col = findEmptySquare

    # ----recurssion---
    # loop through digits to find the correct solution to the square
    for i in range(1, 10):
        if sudoku_rules(board, i, row, col):
            # if its a valid guess --> add that number to the empty square
            board[row][col] = i

            # check if the sudoku is solved -- recurssion
            if solve_sudoku(board):
                return True
            else:
                board[row][col] = 0
    return False


def sudoku_rules(board, guess, posR, posC):
    # Checking the column
    for i in range(len(board[0])):
        if board[posR][i] == guess and i != posC:  #
            return False

    # Checking the row
    for i in range(len(board)):
        if board[i][posC] == guess and i != posR:  #
            return False

    # Checking the square
    box_X = posC // 3
    box_Y = posR // 3
    for row in range(box_Y * 3, (box_Y * 3) + 3):
        for col in range(box_X * 3, (box_X * 3) + 3):
            if board[row][col] == guess and (row, col) != (posR, posC):
                return False

    return True


# Function to print the board
def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0:
            print("-----------------------")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")
    print("-----------------------")


def find_Zero(board):
    for row in range(len(board[1])):
        for col in range(len(board[0])):
            if board[row][col] == 0:
                return row, col
    return None


print_board(unsolved_board)
solve_sudoku(unsolved_board)
print("------------- SOLVING ----------------------")
print_board(unsolved_board)
