import main

# framework
def assertThat(expression):
    if (expression != True):
       print "Test failed: ",expression," was false"
       return False
    return True

def resultToDisplay(outcome):
    if (outcome == True):
        return "Pass"
    else:
        return "Fail"

# define the tests
def testOppositeDirection():
    outcome = assertThat(main.OppositeDirection(main.Direction.Left) == main.Direction.Right)
    outcome = outcome & assertThat(main.OppositeDirection(main.Direction.Up) == main.Direction.Down)
    print "Test opposite direction: ",resultToDisplay(outcome)

def testGetMatchingCode():
    outcome = assertThat(main.getMatchingCode("c") == 3)
    outcome = outcome & assertThat(main.getMatchingCode("a") == 1)
    outcome = outcome & assertThat(main.getMatchingCode("1") == "a")
    outcome = outcome & assertThat(main.getMatchingCode("3") == "c")
    print "Test get matching codes: ",resultToDisplay(outcome)

# run the tests
print "Running unit tests..."
testOppositeDirection()
testGetMatchingCode()
print "Done running unit tests."
