"""
https://d-hac.github.io/puzzle/defuse-the-bomb

To disarm a bomb, one must cut some wires. The order in which the wires are cut is very important;
cut the wires in the wrong order and the bomb will explode. Here are the rules for how the wires should be cut:
If you cut a white wire you can't cut white or black wire. If you cut a red wire you have to cut a green one.
If you cut a black wire, you are not allowed to cut a white, green or orange one. If you cut a orange wire, you should
cut a red or black one. If you cut a green one, you have to cut a orange or white one. If you cut a purple wire, you can't cut
a purple, green, orange or white wire. There can be multiple wires with the same color, however, only one wire may be cut at a time.
"""
explode = False
wireP = input("Enter the wire you want to cut: ")
howManyToCut = 4
counter = 1
while (explode == False and counter != howManyToCut):
    wireC = input("Enter the next wire you want to cut: ")
    if (wireP == "white" and (wireC == "white" or wireC == "black")):
        explode == True
        print("Boom!")
        break
    if (wireP == "red" and (wireC == "white" or wireC == "red" or wireC == "black" or wireC == "orange" or wireC == "purple")):
        explode == True
        print("Boom!")
        break
    if (wireP == "black" and (wireC == "white" or wireC == "green" or wireC == "orange")):
        explode == True
        print("Boom!")
        break
    if (wireP == "orange" and (wireC == "white" or wireC == "orange" or wireC == "green" or wireC == "purple")):
        explode == True
        print("Boom!")
        break
    if (wireP == "green" and (wireC == "red" or wireC == "black" or wireC == "green" or wireC == "purple")):
        explode == True
        print("Boom!")
        break
    if (wireP == "purple" and (wireC == "purple" or wireC == "green" or wireC == "orange" or wireC == "white")):
        explode == True
        print("Boom!")
        break
    counter += 1
    wireP = wireC

if (counter == howManyToCut):
    print("Success!")