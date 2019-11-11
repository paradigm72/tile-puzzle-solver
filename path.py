class Path:
    def __init__(self):
        self.Path = []

    def __init__(self, pathString):
        self.Path = pathString.split("-->")

    def addSquare(self, square, direction):
        self.Path.append(direction)
        self.Path.append(square)

    def unwindToStart(self):
        startDir = self.Path[0]
        startSquare = self.Path[1]
        self.Path = []
        self.Path.append(startDir)
        self.Path.append(startSquare)

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

    # PathString is in a format like 4acb-->Up-->31db-->Right-->243a-->Right-->2c1d-->Up-->dcb2-->Left-->3b4a
    @staticmethod
    def isPathFullyInBounds(PathString):
        # print "Checking path: ",PathString
        PathArray = PathString.split("-->")
        # print "Split array: ",PathArray
        PathArray = filter(lambda x: (x in ["Left", "Right", "Up", "Down"]), PathArray)
        # print "Filtered array: ",PathArray
        subArrayToTest = []
        for start in range(0, len(PathArray)):
            for end in range(start, len(PathArray)):
                horizontalCounter = 0
                verticalCounter = 0
                # grab the slice of the array
                subArrayToTest = PathArray[start:end+1]
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
