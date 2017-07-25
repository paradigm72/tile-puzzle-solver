# represent a quilt square as a 4-tuple in TRBL orientation:
# 1=bluebottomtulips, 2=bluebottomdaisys, 3=whitebottomhearts, 4=whitebottomflowers
# a=bluetoptulips, b=bluetopdaisys, c=whitetophearts, d=whitetopflowers

# given the set of 9 squares, try each rotation by brute force

import math

# globals
squaresList = [];

# static class for directional enums
class Direction:
    Left = "Left"
    Right = "Right"
    Down = "Down"
    Up = "Up"

class Square:
    def __init__(self, layout):
        self.layout = layout

    def rotateClockWise(self):
        temp = self.layout
        self.layout = temp[1] + temp[2] + temp[3] + temp[0]

    def printLongDescription(self):
        print "Square is in orientation TRBL = ", self.layout

    def getShortDescription(self):
        return self.layout


def doCodesMatch(code1, code2):
    # 96 is the ASCII offset for 'a'
    if (ord(code1) - 96 == code2) or (ord(code2) - 96 == code1):
        return True
    return False


def areCompatible(Square1, Square2, MoveDirection):
    if MoveDirection == Direction.Left:
        if doCodesMatch(Square1.layout[1], Square2.layout[3]):
            return True
        else:
            return False
    elif MoveDirection == Direction.Down:
        if doCodesMatch(Square1.layout[2], Square2.layout[0]):
            return True
        else:
            return False
    else:
        return False


def initializeSquares():
    squaresList.append(Square('dcb2'))
    squaresList.append(Square('2c1d'))
    squaresList.append(Square('3b4a'))
    squaresList.append(Square('24ac'))
    squaresList.append(Square('3124'))
    squaresList.append(Square('31db'))
    squaresList.append(Square('243a'))
    squaresList.append(Square('4ba1'))
    squaresList.append(Square('4acb'))

print doCodesMatch('b','2')
initializeSquares()
squaresList[1].printLongDescription()
for i in range(0,8):
    print squaresList[i].getShortDescription(), "is compatible with", squaresList[i+1].getShortDescription(), "?"
    print "Down  :", areCompatible(squaresList[i], squaresList[i+1], Direction.Down)
    print "Left  :", areCompatible(squaresList[i], squaresList[i+1], Direction.Left)
    print "Right :", areCompatible(squaresList[i], squaresList[i+1], Direction.Right)
    print "Up    :", areCompatible(squaresList[i], squaresList[i+1], Direction.Up)

