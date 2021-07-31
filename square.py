from direction import Direction
from lib import doCodesMatch

# individual square
class Square:
    def __init__(self, layout):
        self.layout = layout
        self.visited = False

    def rotateClockWise(self):
        temp = self.layout
        self.layout = temp[1] + temp[2] + temp[3] + temp[0]

    def printLongDescription(self):
        print "Square is in orientation TRBL = ", self.layout

    def getShortDescription(self):
        return self.layout

    def getMatchingTransposition(self):
        transposed = str(self.getMatchingCode(self.layout[:1]))
        transposed += str(self.getMatchingCode(self.layout[1:2]))
        transposed += str(self.getMatchingCode(self.layout[2:3]))
        transposed += str(self.getMatchingCode(self.layout[3:4]))
        return transposed

    @staticmethod
    def getMatchingCode(code):
        # code is a char
        if (ord(code) > 60):     # if alpha, subtract 48 to get matching number
            return chr(ord(code) - 48)
        # code is an int
        else:   # otherwise numeric, add 48 to get alpha
            return chr(int(code) + 48 + 48)

    def isCompatibleInDirection(self, testSquare, MoveDirection):
        if MoveDirection == Direction.Left:
            if doCodesMatch(self.layout[3], testSquare.layout[1]):
                return True
            else:
                return False
        elif MoveDirection == Direction.Down:
            if doCodesMatch(self.layout[2], testSquare.layout[0]):
                return True
            else:
                return False
        elif MoveDirection == Direction.Right:
            if doCodesMatch(self.layout[1], testSquare.layout[3]):
                return True
            else:
                return False
        elif MoveDirection == Direction.Up:
            if doCodesMatch(self.layout[0], testSquare.layout[2]):
                return True
            else:
                return False
        else:
            return False