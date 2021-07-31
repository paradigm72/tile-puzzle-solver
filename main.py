# represent a quilt square as a 4-tuple in TRBL orientation:
# 1=bluebottomtulips, 2=bluebottomdaisys, 3=whitebottomhearts, 4=whitebottomflowers
# a=bluetoptulips, b=bluetopdaisys, c=whitetophearts, d=whitetopflowers

# given the set of 9 squares, try each rotation by brute force
from direction import Direction
from lib import doCodesMatch
from square import Square
from path import Path

# globals
squaresList = []
currentPath = Path()
maxDepthReached = 0
maxDepthPath = ""
depthNineCount = 0


def isInverseDirection(dir1, dir2):
    if (Direction.Opposite(dir1) == dir2):
        return True
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


def findAllNotYetVisitedSquares():
    matchesArray = []
    for potentialNextSquare in squaresList:
        if (not potentialNextSquare.visited):
            # no longer checking compatibility here; it needs to be inside the loop
            matchesArray.append(potentialNextSquare)
    return matchesArray


def findAdjacentSquare(StartingSquare, CurrentDepth, PathString, PrevMoveDirection):
    global depthNineCount

    StartingSquare.visited = True
    # add delimiter and then the next square
    if PrevMoveDirection != "":
        PathString = PathString + "-->" + PrevMoveDirection + "-->" + StartingSquare.getShortDescription()
        currentPath.addSquareAndDir(StartingSquare.getShortDescription(), PrevMoveDirection)
    # for the first square, don't start with the delimiter
    else:
        PathString = PathString + StartingSquare.getShortDescription()
        currentPath.addSquareOnly(StartingSquare.getShortDescription())
    # if we now have an out-of-bounds, bail and unwind
    if not (currentPath.isPathFullyInBounds()):
        # print "Path went out of bounds at depth",CurrentDepth," with path",currentPath.toString()
        currentPath.unwindByOneSquareAndDir()
        StartingSquare.visited = False
        return
    # if we now have an overlapping path, bail and unwind
    if not ((currentPath.doesPathContainNoOverlap())):
        # print "Path overlapped at depth",CurrentDepth," with path",currentPath.toString()
        currentPath.unwindByOneSquareAndDir()
        StartingSquare.visited = False
        return
    # path seems valid, check if we hit 9 squares
    if (CurrentDepth == 9):
        # print depthNineCount,"Reached depth 9! (string): ",PathString
        depthNineCount = depthNineCount + 1
        print "Reached depth 9! (object): ", currentPath.toString()
        currentPath.printGridRepresentation()
    if CurrentDepth > maxDepthReached:
        recordLongestPath(CurrentDepth, currentPath)
    # the recursion loop
    for MoveDirection in [Direction.Left, Direction.Right, Direction.Down, Direction.Up]:
        if (not (isInverseDirection(MoveDirection, PrevMoveDirection))):
            # get a list of possible next squares that haven't been visited yet
            nextSquaresToMoveTo = findAllNotYetVisitedSquares()
            for nextSquare in nextSquaresToMoveTo:
                if (nextSquare is not None):
                    for rotation in 1, 2, 3, 4:
                        nextSquare.rotateClockWise()
                        # print CurrentDepth,":",Path.PathDebugVisualization(CurrentDepth),": [",
                        # StartingSquare.getShortDescription(),"] ->",Direction.Padded(MoveDirection)," \t-> [",
                        # nextSquare.getShortDescription(),"]" print PathString
                        if StartingSquare.isCompatibleInDirection(nextSquare, MoveDirection):
                            findAdjacentSquare(nextSquare, CurrentDepth + 1, PathString, MoveDirection)
    # unmark, so we can revisit on a different sibling path
    StartingSquare.visited = False
    # now that path is an object, we need to manually unwind by one when we leave this recursion level
    if CurrentDepth == 1:
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
    print "-----Next Starting Square:", potentialStartSquare.getShortDescription(), "...-----"
    findAdjacentSquare(potentialStartSquare, 1, "", "")
print "Max Depth reached was: ", maxDepthReached, ", Path: ", maxDepthPath
print "A total of", depthNineCount, "paths were found of depth 9."

