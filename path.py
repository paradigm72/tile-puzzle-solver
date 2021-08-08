from square import Square
from direction import Direction

class Path:
    def __init__(self):
        self.Path = []

    # factory constructor from a pre-constructed string
    @classmethod
    def fromString(cls, pathString):
        pathObj = cls()
        pathObj.Path = pathString.split("-->")
        return pathObj

    def addSquareAndDir(self, square, direction):
        self.Path.append(direction)
        self.Path.append(square)

    def addSquareOnly(self, square):
        self.Path.append(square)

    def unwindToStart(self):
        startDir = self.Path[0]
        startSquare = self.Path[1]
        self.Path = []
        self.Path.append(startDir)
        self.Path.append(startSquare)

    def unwindByOneSquareAndDir(self):
        del self.Path[-1]  # remove the last square
        del self.Path[-1]  # remove the last direction

    def unwindByOneSquareOnly(self):
        del self.Path[-1]  # remove the last square

    def getSquareList(self):
        # any array element that isn't a direction is a square
        return filter(lambda x: (x not in ["Left", "Right", "Up", "Down"]), self.Path)

    def getDirectionList(self):
        # only return the directions
        return filter(lambda x: (x in ["Left", "Right", "Up", "Down"]), self.Path)

    def getNextSquare(self, squareNumber):
        # the path alternates square, dir, square, dir, etc., so take only multiples of 2
        indexOfThisSquare = squareNumber * 2
        if indexOfThisSquare > self.Path.length():
            return None
        return self.Path[indexOfThisSquare]

    def getNextDirection(self, dirNumber):
        # the path alternates square, dir, square, dir, etc., so take only multiples of 2,
        # and make sure we get the odd remainder for the direction
        indexOfThisDir = (dirNumber * 2) + 1
        if indexOfThisDir > self.Path.length():
            return None
        return self.Path[indexOfThisDir]

    def toString(self):
        returnString = ""
        for squareOrDirection in self.Path:
            returnString = returnString + squareOrDirection + "-->"
        returnString = returnString[:-3]  # strip the three characters - - > from the right end
        return returnString

    def isPathFullyInBounds(self):
        # print "Split array: ",PathArray
        pathSquaresOnly = filter(lambda x: (x in ["Left", "Right", "Up", "Down"]), self.Path)
        # print "Filtered array: ",PathArray
        subArrayToTest = []
        for start in range(0, len(pathSquaresOnly)):
            for end in range(start, len(pathSquaresOnly)):
                horizontalCounter = 0
                verticalCounter = 0
                # grab the slice of the array
                subArrayToTest = pathSquaresOnly[start:end + 1]
                # debug print "Path Length=",len(PathArray),"Start=",start,"End=",end,"About to test array slice: ",
                # subArrayToTest loop over each element in the slice
                for strDirection in subArrayToTest:
                    # adjust the appropriate counter
                    if strDirection == "Left":
                        horizontalCounter = horizontalCounter - 1
                    if strDirection == "Right":
                        horizontalCounter = horizontalCounter + 1
                    if strDirection == "Up":
                        verticalCounter = verticalCounter + 1
                    if strDirection == "Down":
                        verticalCounter = verticalCounter - 1
                        # if at any point, we've strayed more than 2 from the origin, we're out of bounds
                    if ((abs(horizontalCounter) > 2) or (abs(verticalCounter) > 2)):
                        # print "Path fell out of bounds"
                        return False
                        # print "Path did not violate the bounds"
        return True

    # whether the path does not close in on itself
    def doesPathContainNoOverlap(self):
        pathDirsOnly = self.getDirectionList()
        self.buildGridRepresentation()  # make sure we have built the grid view
        foundOverlap = False
        # print "PathArray = ",PathArray
        # loop through the nodes in PathString
        x = 2  # cannot have negative list indices, so start at 2, leaving space for 1 and 0
        y = 2
        index = 0  # which path entry we are currently adding
        for node in pathDirsOnly:
            # move in the coordinate space
            if node == "Left":
                x = x - 1
            if node == "Right":
                x = x + 1
            if node == "Up":
                y = y - 1
            if node == "Down":
                y = y + 1
            # advance to the next index in the path
            index = index + 1
            # check for duplicates, failure case if so
            # print "Checking whether " + (str(x) + "," + str(y)) + " is occupied."
            try:
                if ((self.OccupiedCoordinates[x][y]) == "****"):
                    foundOverlap = True  # mark that we found an overlap, but we still want to build the grid
            except IndexError:
                pass  # if not found, those coordinates haven't been visited yet, i.e. not occupied
        return (foundOverlap == False)

    # set up OccupiedSquares as a grid representation, for use in overlap checking and nonlinear edge checking
    def buildGridRepresentation(self):
        pathDirsOnly = self.getDirectionList()
        pathSquaresOnly = self.getSquareList()
        self.OccupiedCoordinates = [["" for i in range(6)] for j in range(6)]
        # print "PathArray = ",PathArray
        # loop through the nodes in PathString
        x = 2   # cannot have negative list indices, so start at 2, leaving space for 1 and 0
        y = 2
        index = 0  # which path entry we are currently adding
        self.OccupiedCoordinates[x][y] = pathSquaresOnly[index]
        index = index + 1
        for node in pathDirsOnly:
            # print OccupiedCoordinates
            # print "Node: ",node
            # move in the coordinate space
            if node == "Left":
                x = x - 1
            if node == "Right":
                x = x + 1
            if node == "Up":
                y = y - 1   # when printing, lower y values are towards the top
            if node == "Down":
                y = y + 1
            # mark the current node as occupied
            if (len(self.OccupiedCoordinates[x][y]) == 4):
                self.OccupiedCoordinates[x][y] = "****"  # error code meaning two squares tried to occupy this spot
            else:
                try:
                    self.OccupiedCoordinates[x][y] = pathSquaresOnly[index]
                except IndexError:
                    pass
            # print "Marking " + (str(x) + "," + str(y)) + " as occupied."
            index = index + 1

    def printGridRepresentation(self):
        print "Final grid for this path:"
        numOverlaps = 0
        for y in range(6):
            thisRowString = ""
            for x in range(6):
                if (len(self.OccupiedCoordinates[x][y]) == 4):

                    # track # overlaps, to know whether we missed an overlap in the recursive algorithm
                    if ((self.OccupiedCoordinates[x][y]) == "****"):
                        numOverlaps = numOverlaps + 1

                    thisRowString += self.OccupiedCoordinates[x][y] + "-"
                else:
                    thisRowString += "    -"
            print thisRowString

        # show the error about overlap count (set a breakpoint here)
        if (numOverlaps > 1):
            print "Logic error: overlapped more than once!!"


    def areAllLinearMatchesValid(self):
        # check each square
        for y in range(6):
            for x in range(6):
                currentSquareLayout = self.OccupiedCoordinates[x][y]
                # don't check nulls
                if (currentSquareLayout == ''):
                    continue
                # check each adjacent direction
                currentSquare = Square(currentSquareLayout)
                # BEGIN 4x DIRECTION BLOCK
                for testDirection in Direction.Left, Direction.Right, Direction.Up, Direction.Down:
                    try:
                        adjacentX, adjacentY = Direction.StepCoordsInDirection(testDirection, x, y)
                        adjacentSquareLayout = self.OccupiedCoordinates[adjacentX][adjacentY]
                    except IndexError:
                        continue  # if off the grid, just pass; never invalid to be on the edge
                    # if it's an empty spot, valid
                    if (adjacentSquareLayout == ''):
                        continue
                    adjacentSquare = Square(adjacentSquareLayout)
                    if (currentSquare.isCompatibleInDirection(adjacentSquare, testDirection)):
                        continue
                    else:
                        return False
                # END 4X DIRECTION BLOCK
        return True

    @staticmethod
    def PathDebugVisualization(length):
        visualizedLength = ""
        for x in range(1, 10):
            if x <= length:
                visualizedLength = visualizedLength + "*"
            else:
                visualizedLength = visualizedLength + " "
        return visualizedLength
