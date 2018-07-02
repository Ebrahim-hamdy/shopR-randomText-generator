from sys import getsizeof
from string import ascii_lowercase, digits
from random import randrange, randint, choice, uniform
from enum import Enum

class Types(Enum):
	INTEGER = 1
	FLOAT = 2
	STRING = 3
	ALPHANUMERIC = 4

# generating random objects
class GenerateObject:
	def __init__(self, type):
		self.type = type

	def getType(self):
		return  self.type

	def createObject(self):
		result = ''
		randomSize = randrange(3, 30)

		# object type is integer
		if self.type == Types.INTEGER.value:
			return result.join(choice(digits) for i in range(randomSize))

		# object type is float
		elif self.type == Types.FLOAT.value:
			randomSize = randint(1, 10)
			output = round(uniform(0.0, 10000.0), randomSize)
			result = '{}'.format(output)
			return result

		# object type is string
		elif self.type == Types.STRING.value:
			return result.join(choice(ascii_lowercase) for i in range(randomSize))

		# object type is alphanumeric
		elif self.type == Types.ALPHANUMERIC.value:
			spaces = randint(1,10)
			for i in range(spaces):
				result += ' '

			for i in range(randomSize):
				result += choice(ascii_lowercase + digits)

			spaces = randint(1,10)
			for i in range(spaces):
			   result += ' '

		return result

def createFile():
	fileName = r'writeRandom.txt'
	currentFileSize = 0;
	maxFileSize = 10485760

	genFile = open(fileName, 'w')

	print('Random data write has started in ' + fileName + '...')

	while currentFileSize <= maxFileSize:
		# create random types from 1 to 4
		randomType = randrange(1,5)
		randomOutput = GenerateObject(randomType).createObject()
		currentFileSize += getsizeof(randomOutput)

		# check if size is less or equal to max size 10MB
		if currentFileSize <= maxFileSize:
			# add random type separated with ',' to the file
			genFile.write(randomOutput + ',')

	print('Done with file size:', currentFileSize / 1000000, 'MB')
	genFile.close()

createFile()