# represent a quilt square as a 4-tuple in TRBL orientation:
# 1=bluebottomtulips, 2=bluebottomdaisys, 3=whitebottomhearts, 4=whitebottomflowers
# a=bluetoptulips, b=bluetopdaisys, c=whitetophearts, d=whitetopflowers

# given the set of 9 squares, try each rotation by brute force

import math

class Square:
	def __init__(self, layout):
		self.layout = layout
	def rotateClockWise(self):
		temp = self.layout
		self.layout = temp[1] + temp[2] + temp[3] + temp[0]


def doCodesMatch(code1,code2):
# if code1 == '1' and code2 == 'a':
# 	return True
# elif code1 == '2' and code2 == 'b':
# 	return True
# elif code1 == '3' and code2 == 'c':
# 	return True
# elif code1 == '4' and code2 == 'd':
# 	return True
# elif code1 == 'a' and code2 == '1':
# 	return True
# elif code1 == 'b' and code2 == '2':
# 	return True
# elif code1 == 'c' and code2 == '3':
# 	return True
# elif code1 == 'd' and code2 == '4':
# 	return True
# else:
# 	return False
# return False
    if (ord(code1) - 96 == code2) or (ord(code2) - 96 == code1):
        return True
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
	squaresList.append(Square('dcb2'))
	squaresList.append(Square('2c1d'))
	squaresList.append(Square('3b4a'))
	squaresList.append(Square('24ac'))
	squaresList.append(Square('3124'))
	squaresList.append(Square('31db'))
	squaresList.append(Square('243a'))
	squaresList.append(Square('4ba1'))
	squaresList.append(Square('4acb'))


