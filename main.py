# represent a quilt square as a 4-tuple in TRBL orientation:
# 1=bluebottomtulips, 2=bluebottomdaisys, 3=whitebottomhearts, 4=whitebottomflowers
# a=bluetoptulips, b=bluetopdaisys, c=whitetophearts, d=whitetopflowers

# given the set of 9 squares, try each rotation by brute force

import math
from square import Square
from path import Path

# globals
squaresList = [];
currentPath = Path();
maxDepthReached = 0;
maxDepthPath = "";

# static class for directional enums
class Direction:
    Left = "Left"
    Right = "Right"
    Down = "Down"
    Up = "Up"

def OppositeDirection(testDir):
    if (testDir == Direction.Left):
        return Direction.Right
    if (testDir == Direction.Right):
        return Direction.Left
    if (testDir == Direction.Up):
        return Direction.Down
    if (testDir == Direction.Down):
        return  Direction.Up

def doCodesMatch(code1, code2):
    # 48 is the ASCII offset between '1' and 'a'
    ascii1 = ord(code1)
    ascii2 = ord(code2)
    if (ord(code1) - 48 == ord(code2)) or (ord(code2) - 48 == ord(code1)):
        return True
    return False

def isInverseDirection(dir1, dir2):
    if (OppositeDirection(dir1) == dir2):
        return True
    return False

def areCompatible(Square1, Square2, MoveDirection):
    if MoveDirection == Direction.Left:
        if doCodesMatch(Square1.layout[3], Square2.layout[1]):
            return True
        else:
            return False
    elif MoveDirection == Direction.Down:
        if doCodesMatch(Square1.layout[2], Square2.layout[0]):
            return True
        else:
            return False
    elif MoveDirection == Direction.Right:
        if doCodesMatch(Square1.layout[1], Square2.layout[3]):
            return True
        else:
            return False
    elif MoveDirection == Direction.Up:
        if doCodesMatch(Square1.layout[0], Square2.layout[2]):
            return True
        else:
            return False
    else:
        return False

def initialize():
    initializeSquares()
    maxDepthReached = 0

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

def findAllMatchesInDirection(StartingSquare, MoveDirection):
    matchesArray = []
    for potentialMatchingSquare in squaresList:
        if not (potentialMatchingSquare.getShortDescription == StartingSquare.getShortDescription):
            if (areCompatible(StartingSquare, potentialMatchingSquare, MoveDirection)):
                matchesArray.append(potentialMatchingSquare)
    return matchesArray

def findAdjacentSquare(StartingSquare, CurrentDepth, PathString, PrevMoveDirection):
    StartingSquare.visited = True
    # add delimeter and then the next square
    if PrevMoveDirection != "":
        PathString = PathString + "-->" + PrevMoveDirection + "-->" + StartingSquare.getShortDescription()
        currentPath.addSquareAndDir(StartingSquare.getShortDescription(), PrevMoveDirection)
    # for the first square, don't start with the delimiter
    else:
        PathString = PathString + StartingSquare.getShortDescription()
        currentPath.addSquareOnly(StartingSquare.getShortDescription())
    if (CurrentDepth == 9):
        print "Reached depth 9! (string): ",PathString
        print "Reached depth 9! (object): ",currentPath.toString()
    if CurrentDepth > maxDepthReached:
        recordLongestPath(CurrentDepth, PathString)
    # the recursion loop
    for MoveDirection in ["Left", "Right", "Down", "Up"]:
        if (not (isInverseDirection(MoveDirection, PrevMoveDirection))):
            # get a list of all matching squares that would work for the given direction, then go that way
            nextSquaresToMoveTo = findAllMatchesInDirection(StartingSquare, MoveDirection)
            for nextSquare in nextSquaresToMoveTo:
                if (nextSquare != None) & (currentPath.isPathFullyInBounds() & (currentPath.doesPathContainNoOverlap())):
                    if (not nextSquare.visited):
                        # print CurrentDepth,": [",StartingSquare.getShortDescription(),"] ->",MoveDirection," -> [",nextSquare.getShortDescription(),"]"
                        findAdjacentSquare(nextSquare, CurrentDepth + 1, PathString, MoveDirection)
                        # print "Unwind"
    # unmark, so we can revisit on a different sibling path
    StartingSquare.visited = False
    # now that path is an object, we need to manually unwind by one when we leave this recursion level
    if (CurrentDepth == 1):
        currentPath.unwindByOneSquareOnly()
    else:
        currentPath.unwindByOneSquareAndDir()

def recordLongestPath(CurrentDepth, PathString):
    global maxDepthReached
    global maxDepthPath
    maxDepthReached = CurrentDepth
    maxDepthPath = PathString

# implementation
initialize()
for potentialStartSquare in squaresList:
    findAdjacentSquare(potentialStartSquare, 1, "", "")
    print "-----Next Starting Square...-----"
print "Max Depth reached was: ",maxDepthReached,", Path: ",maxDepthPath

