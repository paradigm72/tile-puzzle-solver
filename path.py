class Path:
    def __init__(self):
        self.Path = []

    # factory constructor from a pre-constructed string
    @classmethod
    def fromString(cls, pathString):
        cls.Path = pathString.split("-->")
        return cls

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
    @staticmethod
    def doesPathContainNoOverlap(PathString):
        PathArray = PathString.split("-->")
        PathArray = filter(lambda x: (x in ["Left", "Right", "Up", "Down"]), PathArray)
        # print "PathArray = ",PathArray
        # loop through the nodes in PathString
        x = 0
        y = 0
        OccupiedCoordinates = []
        for node in PathArray:
            # print OccupiedCoordinates
            # print "Node: ",node
            # check for duplicates, failure case if so
            # print "Checking whether " + (str(x) + "," + str(y)) + " is occupied."
            if (str(x) + "," + str(y)) in OccupiedCoordinates:
                return False
                # mark this position as occupied
            OccupiedCoordinates.append(str(x) + "," + str(y))
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
            # check for duplicates one last time
        # print "Checking whether " + (str(x) + "," + str(y)) + " is occupied."
        if (str(x) + "," + str(y)) in OccupiedCoordinates:
            return False
        return True
