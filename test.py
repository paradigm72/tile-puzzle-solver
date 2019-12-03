import main
from testFramework import assertThat,resultToDisplay


# dependency router, so the test framework doesn't need to
# reference any particular project
def routeAssertion(expression, objectStore = []):
    outcome = True
    return assertThat(eval(expression), expression)

# generic tests
def testOppositeDirection():
    outcome = True
    outcome = outcome & routeAssertion("main.OppositeDirection(main.Direction.Left) == main.Direction.Right")
    outcome = outcome & routeAssertion("main.OppositeDirection(main.Direction.Up) == main.Direction.Down")
    print "Test opposite direction: ",resultToDisplay(outcome)

def testInverseDirection():
    outcome = True
    outcome = outcome & routeAssertion("main.isInverseDirection(main.Direction.Right,main.Direction.Left) == True")
    outcome = outcome & routeAssertion("main.isInverseDirection(main.Direction.Up,main.Direction.Down) == True")
    print "Test inverse direction: ",resultToDisplay(outcome)

def testDoCodesMatch():
    outcome = True
    outcome = outcome & routeAssertion("main.doCodesMatch(\"2\",\"b\")")
    outcome = outcome & routeAssertion("main.doCodesMatch(\"b\",\"2\")")
    outcome = outcome & routeAssertion("main.doCodesMatch(\"5\",\"e\")")
    print "Test 'do codes match'",resultToDisplay(outcome)

def testIsPathFullyInBounds():
    outcome = True
    objectStore = []
    objectStore.append(main.Path.fromString("xxxx-->Left-->xxxx-->Left-->xxxx-->Left-->xxxx"))
    myNewPath =  main.Path.fromString("xxxx-->Left-->xxxx-->Left-->xxxx-->Left-->xxxx")
    print myNewPath.toString()
    print objectStore[0].toString()
    outcome = outcome & routeAssertion("objectStore[0].isPathFullyInBounds() == False")
    outcome = outcome & routeAssertion("main.Path.isPathFullyInBounds(\"xxxx-->Left-->xxxx-->Left-->xxxx-->Right-->xxxx\") == True")
    outcome = outcome & routeAssertion("main.Path.isPathFullyInBounds(\"xxxx-->Up-->xxxx-->Down-->xxxx-->Left-->xxxx-->Right-->xxxx\") == True")
    outcome = outcome & routeAssertion("main.Path.isPathFullyInBounds(\"xxxx-->Up-->xxxx-->Up-->xxxx-->Up-->xxxx-->Down-->xxxx-->Right-->xxxx\") == False")
    outcome = outcome & routeAssertion("main.Path.isPathFullyInBounds(\"Up-->xxxx-->Up-->xxxx-->Up-->xxxx-->Up-->xxxx-->Down-->xxxx-->Down-->xxxx-->Down-->xxxx-->Left\") == False")
    print "Test 'is path fully in bounds'",resultToDisplay(outcome)

def testDoesPathContainNoOverlap():
    outcome = True
    outcome = outcome & routeAssertion("main.Path.doesPathContainNoOverlap(\"xxxx-->Left-->xxxx-->Right-->xxxx\") == False")
    outcome = outcome & routeAssertion("main.Path.doesPathContainNoOverlap(\"xxxx-->Left-->xxxx-->Left-->xxxx\") == True")
    outcome = outcome & routeAssertion("main.Path.doesPathContainNoOverlap(\"xxxx-->Left-->xxxx-->Down-->xxxx-->Right-->xxxx-->Up-->xxxx\") == False")
    outcome = outcome & routeAssertion("main.Path.doesPathContainNoOverlap(\"xxxx-->Left-->xxxx-->Left-->xxxx-->Down-->xxxx-->Right-->xxxx-->Right-->xxxx\") == True")
    outcome = outcome & routeAssertion("main.Path.doesPathContainNoOverlap(\"xxxx-->Left-->xxxx-->Left-->xxxx-->Down-->xxxx-->Right-->xxxx-->Right-->xxxx-->Up\") == False")
    outcome = outcome & routeAssertion("main.Path.doesPathContainNoOverlap(\"xxxx-->Left-->xxxx-->Left-->xxxx-->Down-->xxxx-->Down-->xxxx-->Right-->xxxx-->Up-->xxxx-->Up\") == False")

    print "Test 'does path contain no overlap'",resultToDisplay(outcome)

# test the Square class
def testSquareInit():
    objectStore = []
    objectStore.append(main.Square('abcd'))
    outcome = True
    outcome = outcome & routeAssertion("objectStore[0].layout == \'abcd\'", objectStore)
    outcome = outcome & routeAssertion("objectStore[0].visited == False", objectStore)
    outcome = outcome & routeAssertion("objectStore[0].getShortDescription() == \'abcd\'", objectStore)
    print "Test square initialization: ",resultToDisplay(outcome)

def testSquareCompatibility():
    objectStore = []
    objectStore.append(main.Square('abaa'))
    objectStore.append(main.Square('4442'))
    outcome = True
    outcome = outcome & routeAssertion("main.areCompatible(objectStore[0],objectStore[1],main.Direction.Right)",objectStore)
    outcome = outcome & routeAssertion("not (main.areCompatible(objectStore[0],objectStore[1],7))",objectStore)
    outcome = outcome & routeAssertion("not (main.areCompatible(objectStore[0],objectStore[1],main.Direction.Left))",objectStore)
    print "Test square compatibility: ",resultToDisplay(outcome)

def testGetMatchingCode():
    outcome = True
    outcome = outcome & routeAssertion("main.Square.getMatchingCode(\"c\") == \"3\"")
    outcome = outcome & routeAssertion("main.Square.getMatchingCode(\"a\") == \"1\"")
    outcome = outcome & routeAssertion("main.Square.getMatchingCode(\"1\") == \"a\"")
    outcome = outcome & routeAssertion("main.Square.getMatchingCode(\"3\") == \"c\"")
    print "Test get matching codes: ",resultToDisplay(outcome)



# run the tests
print "Running unit tests..."
testOppositeDirection()
testGetMatchingCode()
testDoCodesMatch()
testIsPathFullyInBounds()
testDoesPathContainNoOverlap()
testInverseDirection()
testSquareInit()
testSquareCompatibility()
print "Done running unit tests."
