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

def testGetMatchingCode():
    outcome = True
    outcome = outcome & routeAssertion("main.getMatchingCode(\"c\") == \"3\"")
    outcome = outcome & routeAssertion("main.getMatchingCode(\"a\") == \"1\"")
    outcome = outcome & routeAssertion("main.getMatchingCode(\"1\") == \"a\"")
    outcome = outcome & routeAssertion("main.getMatchingCode(\"3\") == \"c\"")
    print "Test get matching codes: ",resultToDisplay(outcome)

def testDoCodesMatch():
    outcome = True
    outcome = outcome & routeAssertion("main.doCodesMatch(\"2\",\"b\")")
    outcome = outcome & routeAssertion("main.doCodesMatch(\"b\",\"2\")")
    outcome = outcome & routeAssertion("main.doCodesMatch(\"5\",\"e\")")
    print "Test 'do codes match'",resultToDisplay(outcome)

# test the Square class
def testSquareInit():
    objectStore = [];
    objectStore.append(main.Square('abcd'));
    outcome = True
    outcome = outcome & routeAssertion("objectStore[0].layout == \'abcd\'", objectStore)
    outcome = outcome & routeAssertion("objectStore[0].visited == False", objectStore)
    outcome = outcome & routeAssertion("objectStore[0].getShortDescription() == \'abcd\'", objectStore)
    print "Test square initialization: ",resultToDisplay(outcome)


# run the tests
print "Running unit tests..."
testOppositeDirection()
testGetMatchingCode()
testDoCodesMatch()
testInverseDirection()
testSquareInit()
print "Done running unit tests."
