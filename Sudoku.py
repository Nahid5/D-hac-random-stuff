"""
This brute forces a sudoku puzzle by trying random combination
"""

#https://d-hac.github.io/puzzle/sudoku
import random
import copy
import time


start = time.time()
###########################################################################################################
# checks if the rows are equal to the sum (10 for a 4x4 and 45 for 9x9)
###########################################################################################################
def checkRow(list):
    for lines in list:
        sum = 0
        temp = set(lines)
        if (len(temp) != len(lines)):
            return False
        for val in temp:
            sum += int(val)
        #break if the sum of the row is not 10 for a 4x4
        if (len(list) == 4 and sum != 10):
            return False
        #break if the su of the row is not 45 for a 9x9
        if (len(list) == 9 and sum != 45):
            return False
    return True

###########################################################################################################
#reverses the rows and columns
###########################################################################################################
def reverseBoard(board):
    reversed = []
    for x in range(len(board)):
        reversed.append([])
        for y in range(len(board)):
            reversed[x].append(int (board[y][x]))
    return reversed

###########################################################################################################
#solves a 4x4 or 9x9 Sodoku puzzle
###########################################################################################################
def solveSudoku(fileName):
    myFile = open(fileName, 'r')
    board = []
    # reads form file into a 4x4 list
    sizeOfGrid = 0
    for lines in myFile:
        board.append([])
        for line in lines:
            if (line != "\n"):
                board[sizeOfGrid].append(int(line))
        sizeOfGrid += 1

    #possible numbers in the grid
    if (sizeOfGrid == 4):
        validNumbers = [1, 2, 3, 4]
    if (sizeOfGrid == 9):
        validNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    #a new board is created to store the original state of the board
    newBoard = copy.deepcopy(board)
    #another board is created where the rows and columns are reversed
    boardReverse = reverseBoard(newBoard)

    # keeps looping until the sudoku is solved
    while (checkRow(newBoard) == False or checkRow(boardReverse) == False):
        newBoard = copy.deepcopy(board)
        for x in range(0, sizeOfGrid):
            avliableNum = []
            counter = 0
            for t in validNumbers:
                # stores numbers that are already not in the row of the board
                if (t not in newBoard[x]):
                    avliableNum.append(t)
                    random.shuffle(avliableNum)
            for y in range(0, sizeOfGrid):
                if (newBoard[x][y] == 0):
                    newBoard[x][y] = avliableNum[counter]
                    counter += 1
        boardReverse = reverseBoard(newBoard)
    print(newBoard)


solveSudoku("grid.txt")
end = time.time()- start
print(end)
