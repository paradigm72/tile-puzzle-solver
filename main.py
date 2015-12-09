# represent a quilt square as a 4-tuple in TRBL orientation:
# 1=bluebottom1, 2=bluebottom2, 3=whitebottom1, 4=whitebottom2
# a=bluetop1, b=bluetop2, c=whitetop1, d=whitetop2

# given the set of 9 squares, try each rotation by brute force

class Square:
	def __init__(self, layout):
		self.layout = layout
	def rotateClockWise(self):
		temp = self.layout
		self.layout = temp[1] + temp[2] + temp[3] + temp[0]


def doCodesMatch(code1,code2):
	if code1 == '1' and code2 == 'a':
		return True
	elif code1 == '2' and code2 == 'b':
		return True
	elif code1 == '3' and code2 == 'c':
		return True
	elif code1 == '4' and code2 == 'd':
		return True
	elif code1 == 'a' and code2 == '1':
		return True
	elif code1 == 'b' and code2 == '2':
		return True
	elif code1 == 'c' and code2 == '3':
		return True
	elif code1 == 'd' and code2 == '4':
		return True
	else:
		return False
	return False

def areCompatible(Square1,Square2,Direction):
	if Direction == 'right':
		if doCodesMatch(Square1.layout[1],Square2.layout[3]):
			return True
		else:
			return False
	elif Direction == 'down':
		if doCodesMatch(Square1.layout[2],Square2.layout[0]):
			return True
		else:
			return False
	else:
		return False

def initializeSquares():
	squaresList = [];
	squaresList.append(Square(''))
	squaresList.append(Square(''))
	squaresList.append(Square(''))
	squaresList.append(Square(''))
	squaresList.append(Square(''))
	squaresList.append(Square(''))
	squaresList.append(Square(''))
	squaresList.append(Square(''))
	squaresList.append(Square(''))


