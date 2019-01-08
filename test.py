import main
from testFramework import assertThat,resultToDisplay

# generic tests
def testOppositeDirection():
    outcome = True
    outcome = outcome & assertThat(main.OppositeDirection(main.Direction.Left) == main.Direction.Right)
    outcome = outcome & assertThat(main.OppositeDirection(main.Direction.Up) == main.Direction.Down)
    print "Test opposite direction: ",resultToDisplay(outcome)

def testInverseDirection():
    outcome = True
    outcome = outcome & assertThat(main.isInverseDirection(main.Direction.Right,main.Direction.Left) == True)
    outcome = outcome & assertThat(main.isInverseDirection(main.Direction.Up,main.Direction.Down) == True)
    print "Test inverse direction: ",resultToDisplay(outcome)

def testGetMatchingCode():
    outcome = True
    outcome = outcome & assertThat(main.getMatchingCode("c") == "3")
    outcome = outcome & assertThat(main.getMatchingCode("a") == "1")
    outcome = outcome & assertThat(main.getMatchingCode("1") == "a")
    outcome = outcome & assertThat(main.getMatchingCode("3") == "c")
    print "Test get matching codes: ",resultToDisplay(outcome)

# run the tests
print "Running unit tests..."
testOppositeDirection()
testGetMatchingCode()
testInverseDirection()
print "Done running unit tests."
