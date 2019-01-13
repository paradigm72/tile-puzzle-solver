import main

# framework
def assertThat(expression):
    if (eval(expression) != True):
        print "Test failed: ",expression," was false"
        return False
    return True

def resultToDisplay(outcome):
    if (outcome == True):
        return "Pass"
    else:
        return "Fail"
