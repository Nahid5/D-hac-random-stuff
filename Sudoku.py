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
        if (sum != 10): return False
    return True


myFile = open("grid.txt", 'r')
list = []
#for 4x4
list.append([])
list.append([])
list.append([])
list.append([])
sizeOfGrid = 4

#reads form file into a list
a = 0
for lines in myFile:
    for line in lines:
        if (line != "\n"):
            list[a].append(int (line))
    a += 1


newList = copy.deepcopy(list)
listCol = copy.deepcopy(zip(*newList))       #columns becomes rows
#keeps looping until the sudoku is solved
while (checkRow(newList) == False or checkRow(listCol) == False):
    newList = copy.deepcopy(list)
    for x in range(0, sizeOfGrid):
        for y in range(0, sizeOfGrid):
            if (newList[x][y] == 0):
                newList[x][y] = random.randint(1, sizeOfGrid)
    #print(newList)
    listCol = copy.deepcopy(zip(*newList))  # columns becomes rows

end = time.time()- start

print(newList)
print(end)
