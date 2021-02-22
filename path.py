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
        del self.Path[-1]   # remove the last square
        del self.Path[-1]   # remove the last direction

    def unwindByOneSquareOnly(self):
        del self.Path[-1]   # remove the last square

    def getSquareList(self):
        # any array element that isn't a direction is a square
        return filter(lambda x: (x not in ["Left", "Right", "Up", "Down"]), self.Path)

    def getDirectionList(self):
        # only return the directions
        return filter(lambda x: (x in ["Left", "Right", "Up", "Down"]), self.Path)

    def getNextSquare(self, squareNumber):
        # the path alternates square, dir, square, dir, etc., so take only multiples of 2
        indexOfThisSquare = squareNumber*2
        if indexOfThisSquare > self.Path.length():
            return None
        return self.Path[indexOfThisSquare]

    def getNextDirection(self, dirNumber):
        # the path alternates square, dir, square, dir, etc., so take only multiples of 2,
        # and make sure we get the odd remainder for the direction
        indexOfThisDir = (dirNumber*2) + 1
        if indexOfThisDir > self.Path.length():
            return None
        return self.Path[indexOfThisDir]

    def toString(self):
        returnString = ""
        for squareOrDirection in self.Path:
            returnString = returnString + squareOrDirection + "-->"
        returnString = returnString[:-3]   # strip the three characters - - > from the right end
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
                subArrayToTest = pathSquaresOnly[start:end+1]
                # debug
                # print "Path Length=",len(PathArray),"Start=",start,"End=",end,"About to test array slice: ",subArrayToTest
                # loop over each element in the slice
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
        pathDirsOnly = filter(lambda x: (x in ["Left", "Right", "Up", "Down"]), self.Path)
        foundOverlap = False
        # print "PathArray = ",PathArray
        # loop through the nodes in PathString
        x = 2   # cannot have negative list indices, so start at 2, leaving space for 1 and 0
        y = 2
        OccupiedCoordinates = [[0 for i in range(6)] for j in range(6)]
        for node in pathDirsOnly:
            # print OccupiedCoordinates
            # print "Node: ",node
            # mark the current node as occupied
            OccupiedCoordinates[x][y] = 1
            # print "Marking " + (str(x) + "," + str(y)) + " as occupied."
            # move in the coordinate space
            if node == "Left":
                x = x - 1
            if node == "Right":
                x = x + 1
            if node == "Up":
                y = y + 1
            if node == "Down":
                y = y - 1
            # check for duplicates, failure case if so
            # print "Checking whether " + (str(x) + "," + str(y)) + " is occupied."
            try:
                if OccupiedCoordinates[x][y] == 1:
                    foundOverlap = True  # mark that we found an overlap, but we still want to build the grid
            except IndexError:
                pass # if not found, those coordinates haven't been visited yet, i.e. not occupied
        return (foundOverlap == False)

    @staticmethod
    def PathDebugVisualization(length):
        visualizedLength = ""
        for x in range(1, 10):
            if x <= length:
                visualizedLength = visualizedLength + "*"
            else:
                visualizedLength = visualizedLength + " "
        return visualizedLength





