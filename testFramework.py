import main

# framework
def assertThat(evalResult, rawExpression):
    if (evalResult != True):
        print "Test failed: ",rawExpression," was false"
        return False
    return True

def resultToDisplay(outcome):
    if (outcome == True):
        return "Pass"
    else:
        return "Fail"
