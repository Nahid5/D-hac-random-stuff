"""
https://d-hac.github.io/puzzle/scrabble
Scrabble is a word game where players are given 7 tiles and take turns strategically placing them to spell words with the highest value. More obscure letters have a higher point value. Today, our challenge involves taking a set of seven tiles and determining if a given word can be spelled using those tiles.

The extension of this challenge is, given a list of 20 tiles, what is the longest word that can be spelled out of the list of English words found in this text file.

longest("dcthoyueorza") ->  "coauthored"
longest("uruqrnytrois") -> "turquois"
longest("rryqeiaegicgeo??") -> "greengrocery"
longest("udosjanyuiuebr??") -> "subordinately"
longest("vaakojeaietg????????") -> "ovolactovegetarian"
"""
from itertools import permutations

###########################################################################################################
#finds the longest word that can be made using the words
###########################################################################################################
def findLongest(words, perms):
    max = 0
    position = -1
    for x in range(0, len(words)):
        for y in range(0, len(perms)):
            if (words[x] in perms[y]):
                if (len(words[x]) > max):
                    max = len(words[x])
                    position = x
    if (position == -1):
        print("No words can be made")
    else:
        print(words[position])

###########################################################################################################
myFile = open('enable1.txt', 'r')
words = []
for lines in myFile:
    words.append(lines.rstrip())

perms = [''.join(p) for p in permutations('ladilmy')]
findLongest(words, perms)