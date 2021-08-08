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
            return Direction.Up

    @staticmethod
    def StepCoordsInDirection(testDir, x, y):
        if (testDir == Direction.Left):
            return x-1, y
        if (testDir == Direction.Right):
            return x+1, y
        if (testDir == Direction.Up):
            return x, y-1
        if (testDir == Direction.Down):
            return x, y+1
        return 0, 0
