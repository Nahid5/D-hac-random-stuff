"""
This brute forces a sudoku puzzle by trying random combination
"""

#https://d-hac.github.io/puzzle/sudoku
import random
import copy
import time


start = time.time()
#checks if the rows are equal to the sum (10 for a 4x4 and 45 for 9x9)
def checkRow(list):
    for lines in list:
        sum = 0
        temp = set(lines)
        if (len(temp) != len(lines)): return False
        for val in temp:
            sum += int(val)
        if (sum != 10): return False                    #need to change this depending on 4x4 or 9x9
    return True

def fourByFour(fileName):
    myFile = open(fileName, 'r')
    board = []
    # for 4x4
    board.append([])
    board.append([])
    board.append([])
    board.append([])
    sizeOfGrid = 4

    # reads form file into a list
    a = 0
    for lines in myFile:
        for line in lines:
            if (line != "\n"):
                board[a].append(int(line))
        a += 1

    validNumbers = [1,2,3,4]
    newBoard = copy.deepcopy(board)
    boardReverse = copy.deepcopy(zip(*newBoard))  # columns becomes rows
    # keeps looping until the sudoku is solved
    while (checkRow(newBoard) == False or checkRow(boardReverse) == False):
        newBoard = copy.deepcopy(board)
        for x in range(0, sizeOfGrid):
            newStorage = []
            counter = 0
            for t in validNumbers:
                # stores numbers that are already not in the row of the board
                if ((t not in newBoard[x])):
                    newStorage.append(t)
                    random.shuffle(newStorage)
            for y in range(0, sizeOfGrid):
                if (newBoard[x][y] == 0):
                    newBoard[x][y] = newStorage[counter]
                    counter += 1
        boardReverse = copy.deepcopy(zip(*newBoard))  # columns becomes rows
    print(newBoard)


fourByFour("grid.txt")
end = time.time()- start
print(end)
