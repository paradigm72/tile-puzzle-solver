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

    @staticmethod
    def Padded(testDir):
        if testDir == Direction.Right:
            return testDir
        elif testDir == Direction.Left:
            return testDir + " "
        elif testDir == Direction.Down:
            return testDir + " "
        elif testDir == Direction.Up:
            return testDir + "   "
        return ""

    @staticmethod
    def Opposite(testDir):
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
    if (Direction.Opposite(dir1) == dir2):
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
    squaresList.append(Square('2cad'))
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
        if (not potentialMatchingSquare.visited):
            # upgrade to "are compatible in direction", check all 4, and use directionality when appending
            # maybe mutate the actual square object and leave it that way, for all future comparisons
            # but we do need a way to try the same square twice in two different orientations
            if (areCompatible(StartingSquare, potentialMatchingSquare, MoveDirection)):
                matchesArray.append(potentialMatchingSquare)
    return matchesArray

def findAdjacentSquare(StartingSquare, CurrentDepth, PathString, PrevMoveDirection):
    StartingSquare.visited = True
    # add delimiter and then the next square
    if PrevMoveDirection != "":
        PathString = PathString + "-->" + PrevMoveDirection + "-->" + StartingSquare.getShortDescription()
        currentPath.addSquareAndDir(StartingSquare.getShortDescription(), PrevMoveDirection)
    # for the first square, don't start with the delimiter
    else:
        PathString = PathString + StartingSquare.getShortDescription()
        currentPath.addSquareOnly(StartingSquare.getShortDescription())
    # if we now have an out-of-bounds or overlapping path, bail and unwind
    if not (currentPath.isPathFullyInBounds() & (currentPath.doesPathContainNoOverlap())):
        print "Path went out of bounds/overlapped at depth",CurrentDepth," with path",currentPath.toString()
        currentPath.unwindByOneSquareAndDir()
        return
    # path seems valid, check if we hit 9 squares
    if (CurrentDepth == 9):
        print "Reached depth 9! (string): ",PathString
        print "Reached depth 9! (object): ",currentPath.toString()
    if CurrentDepth > maxDepthReached:
        recordLongestPath(CurrentDepth, currentPath)
    # the recursion loop
    for MoveDirection in [Direction.Left, Direction.Right, Direction.Down, Direction.Up]:
        if (not (isInverseDirection(MoveDirection, PrevMoveDirection))):
            # get a list of all matching squares that would work for the given direction, then go that way
            nextSquaresToMoveTo = findAllMatchesInDirection(StartingSquare, MoveDirection)
            # count the number of next adjacent squares we've tried, for tracing
            squareNumberAttempted = 1
            for nextSquare in nextSquaresToMoveTo:
                if (nextSquare != None):
                    print Path.PathDebugVisualization(CurrentDepth),": [",StartingSquare.getShortDescription(),"] ->",Direction.Padded(MoveDirection)," \t-> [",nextSquare.getShortDescription(),"], candidate",squareNumberAttempted,"of",len(nextSquaresToMoveTo),"possible adjacent next squares from",StartingSquare.getShortDescription()
                    findAdjacentSquare(nextSquare, CurrentDepth + 1, PathString, MoveDirection)
                    squareNumberAttempted = squareNumberAttempted + 1
                    # print "Unwind"
    # unmark, so we can revisit on a different sibling path
    StartingSquare.visited = False
    # now that path is an object, we need to manually unwind by one when we leave this recursion level
    if (CurrentDepth == 1):
        currentPath.unwindByOneSquareOnly()
    else:
        currentPath.unwindByOneSquareAndDir()

def recordLongestPath(CurrentDepth, currentPath):
    global maxDepthReached
    global maxDepthPath
    maxDepthReached = CurrentDepth
    maxDepthPath = currentPath.toString()

# implementation
initialize()
for potentialStartSquare in squaresList:
    print "-----Next Starting Square:",potentialStartSquare.getShortDescription(),"...-----"
    findAdjacentSquare(potentialStartSquare, 1, "", "")
print "Max Depth reached was: ",maxDepthReached,", Path: ",maxDepthPath

