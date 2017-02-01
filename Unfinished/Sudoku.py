#https://d-hac.github.io/puzzle/sudoku

import random

#checks if the rows are equal to 45
def checkRow(list):
    sum = 0
    for lines in list:
        temp = set(lines)
        for val in temp:
            sum += int(val)
    if (sum != 10): return False
    else: return True


myFile = open("grid.txt", 'r')
list = []
#for 4x4
list.append([])
list.append([])
list.append([])
list.append([])
sizeOfGrid = 4

#reads form file into multilist
a = 0
for lines in myFile:
    for line in lines:
        if (line != "\n"):
            list[a].append(int (line))
    a += 1

#replaces the values of 0 with something valid
newList = list
for x in range (0,sizeOfGrid):
    for y in range (0,sizeOfGrid):
        if (newList[x][y] == 0):
            newList[x][y] = random.randint(1,sizeOfGrid)
listCol = zip(*newList)            #columns becomes rows

#keeps looping until the sudoku is solved
while (checkRow(newList) == False and checkRow(listCol) == False):
    newList = list
    for x in range(0, sizeOfGrid):
        for y in range(0, sizeOfGrid):
            if (newList[x][y] == 0):
                newList[x][y] = random.randint(1, sizeOfGrid)
    print(newList)
    listCol = zip(*newList)  # columns becomes rows
