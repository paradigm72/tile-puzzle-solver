import main
from testFramework import assertThat, resultToDisplay


# dependency router, so the test framework doesn't need to
# reference any particular project
def routeAssertion(expression, objectStore=None):
    if objectStore is None:
        objectStore = []
    outcome = True
    return assertThat(eval(expression), expression)


# generic tests
def testOppositeDirection():
    outcome = True
    outcome = outcome & routeAssertion("main.Direction.Opposite(main.Direction.Left) == main.Direction.Right")
    outcome = outcome & routeAssertion("main.Direction.Opposite(main.Direction.Up) == main.Direction.Down")
    print "Test opposite direction: ", resultToDisplay(outcome)


def testInverseDirection():
    outcome = True
    outcome = outcome & routeAssertion("main.isInverseDirection(main.Direction.Right,main.Direction.Left) == True")
    outcome = outcome & routeAssertion("main.isInverseDirection(main.Direction.Up,main.Direction.Down) == True")
    print "Test inverse direction: ", resultToDisplay(outcome)


def testDoCodesMatch():
    outcome = True
    outcome = outcome & routeAssertion("main.doCodesMatch(\"2\",\"b\")")
    outcome = outcome & routeAssertion("main.doCodesMatch(\"b\",\"2\")")
    outcome = outcome & routeAssertion("main.doCodesMatch(\"5\",\"e\")")
    print "Test 'do codes match'", resultToDisplay(outcome)


# test the Path class
def testIsPathFullyInBounds():
    outcome = True
    objectStore = []
    objectStore.append(main.Path.fromString("xxxx-->Left-->xxxx-->Left-->xxxx-->Left-->xxxx"))
    objectStore.append(main.Path.fromString("xxxx-->Left-->xxxx-->Left-->xxxx-->Right-->xxxx"))
    objectStore.append(main.Path.fromString("xxxx-->Up-->xxxx-->Down-->xxxx-->Left-->xxxx-->Right-->xxxx"))
    objectStore.append(main.Path.fromString(
        "xxxx-->Up-->xxxx-->Up-->xxxx-->Left-->xxxx-->Left-->xxxx-->Down-->xxxx-->Down-->xxxx-->Right-->xxxx"))
    objectStore.append(main.Path.fromString("xxxx-->Up-->xxxx-->Up-->xxxx-->Up-->xxxx-->Down-->xxxx-->Right-->xxxx"))
    objectStore.append(main.Path.fromString(
        "Up-->xxxx-->Up-->xxxx-->Up-->xxxx-->Up-->xxxx-->Down-->xxxx-->Down-->xxxx-->Down-->xxxx-->Left"))
    outcome = outcome & routeAssertion("objectStore[0].isPathFullyInBounds() == False", objectStore)
    outcome = outcome & routeAssertion("objectStore[1].isPathFullyInBounds() == True", objectStore)
    outcome = outcome & routeAssertion("objectStore[2].isPathFullyInBounds() == True", objectStore)
    outcome = outcome & routeAssertion("objectStore[3].isPathFullyInBounds() == True", objectStore)
    outcome = outcome & routeAssertion("objectStore[4].isPathFullyInBounds() == False", objectStore)
    outcome = outcome & routeAssertion("objectStore[5].isPathFullyInBounds() == False", objectStore)
    print "Test 'is path fully in bounds'", resultToDisplay(outcome)


def testDoesPathContainNoOverlap():
    outcome = True
    objectStore = []
    objectStore.append(main.Path.fromString("xxxx-->Left-->xxxx-->Right-->xxxx"))
    objectStore.append(main.Path.fromString("xxxx-->Left-->xxxx-->Left-->xxxx"))
    objectStore.append(main.Path.fromString("xxxx-->Left-->xxxx-->Down-->xxxx-->Right-->xxxx-->Up-->xxxx"))
    objectStore.append(
        main.Path.fromString("xxxx-->Left-->xxxx-->Left-->xxxx-->Down-->xxxx-->Right-->xxxx-->Right-->xxxx"))
    objectStore.append(
        main.Path.fromString("xxxx-->Left-->xxxx-->Left-->xxxx-->Down-->xxxx-->Right-->xxxx-->Right-->xxxx-->Up"))
    objectStore.append(main.Path.fromString(
        "xxxx-->Left-->xxxx-->Left-->xxxx-->Down-->xxxx-->Down-->xxxx-->Right-->xxxx-->Up-->xxxx-->Up"))

    # this is a real path which we found, but it does contain overlap (doesn't contain no overlap)
    objectStore.append(main.Path.fromString(
        "2c1d-->Left-->243a-->Left-->3124-->Up-->4acb-->Right-->4ba1-->Up-->31db-->Right-->3b4a-->Down-->dcb2-->Down-->24ac"))

    outcome = outcome & routeAssertion("objectStore[0].doesPathContainNoOverlap() == False", objectStore)
    outcome = outcome & routeAssertion("objectStore[1].doesPathContainNoOverlap() == True", objectStore)
    outcome = outcome & routeAssertion("objectStore[2].doesPathContainNoOverlap() == False", objectStore)
    outcome = outcome & routeAssertion("objectStore[3].doesPathContainNoOverlap() == True", objectStore)
    outcome = outcome & routeAssertion("objectStore[4].doesPathContainNoOverlap() == False", objectStore)
    outcome = outcome & routeAssertion("objectStore[5].doesPathContainNoOverlap() == False", objectStore)
    outcome = outcome & routeAssertion("objectStore[6].doesPathContainNoOverlap() == False", objectStore)
    print "Test 'does path contain no overlap'", resultToDisplay(outcome)


# test the Square class
def testSquareInit():
    objectStore = []
    objectStore.append(main.Square('abcd'))
    outcome = True
    outcome = outcome & routeAssertion("objectStore[0].layout == \'abcd\'", objectStore)
    outcome = outcome & routeAssertion("objectStore[0].visited == False", objectStore)
    outcome = outcome & routeAssertion("objectStore[0].getShortDescription() == \'abcd\'", objectStore)
    print "Test square initialization: ", resultToDisplay(outcome)


def testSquareCompatibility():
    objectStore = []
    objectStore.append(main.Square('abaa'))
    objectStore.append(main.Square('4442'))
    outcome = True
    outcome = outcome & routeAssertion("main.areCompatible(objectStore[0],objectStore[1],main.Direction.Right)",
                                       objectStore)
    outcome = outcome & routeAssertion("not (main.areCompatible(objectStore[0],objectStore[1],7))", objectStore)
    outcome = outcome & routeAssertion("not (main.areCompatible(objectStore[0],objectStore[1],main.Direction.Left))",
                                       objectStore)
    print "Test square compatibility: ", resultToDisplay(outcome)


def testGetMatchingCode():
    outcome = True
    outcome = outcome & routeAssertion("main.Square.getMatchingCode(\"c\") == \"3\"")
    outcome = outcome & routeAssertion("main.Square.getMatchingCode(\"a\") == \"1\"")
    outcome = outcome & routeAssertion("main.Square.getMatchingCode(\"1\") == \"a\"")
    outcome = outcome & routeAssertion("main.Square.getMatchingCode(\"3\") == \"c\"")
    print "Test get matching codes: ", resultToDisplay(outcome)


def testPathDebugVisualization():
    outcome = True
    outcome = outcome & routeAssertion("main.Path.PathDebugVisualization(1) == \"*        \"")
    outcome = outcome & routeAssertion("main.Path.PathDebugVisualization(3) == \"***      \"")
    outcome = outcome & routeAssertion("main.Path.PathDebugVisualization(9) == \"*********\"")
    outcome = outcome & routeAssertion("main.Path.PathDebugVisualization(12) == \"*********\"")
    print "Test path debug visualization: ", resultToDisplay(outcome)


# run the tests
print "Running unit tests..."
testOppositeDirection()
testGetMatchingCode()
testPathDebugVisualization()
testDoCodesMatch()
testIsPathFullyInBounds()
testDoesPathContainNoOverlap()
testInverseDirection()
testSquareInit()
testSquareCompatibility()
print "Done running unit tests."
