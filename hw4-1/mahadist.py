import sys

def toF(array):
  return [float(x) for x in array]


def readFile(filename):
  lines = [toF(line.rstrip('\n').rstrip('\r').split()) for line in open(filename)]

  return lines











trainingData = readFile(sys.argv[1])
testingData = readFile(sys.argv[2])

M = trainingData[0][0]
N = trainingData[0][1]
trainingData = trainingData[1:]

print M, N, trainingData