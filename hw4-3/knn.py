import sys
from numpy import matrix
from math import sqrt

def toF(array):
  return [float(x) for x in array]

def readFile(filename):
  lines = [toF(line.rstrip('\n').rstrip('\r').split()) for line in open(filename)]
  return lines

##### training
trainingData = readFile(sys.argv[1])
M = int(trainingData[0][0])
N = int(trainingData[0][1])
trainingData = trainingData[1:]

print trainingData

##### testing
testingData = readFile(sys.argv[2])
M_test = int(testingData[0][0])
N_test = int(testingData[0][1])
testingData = testingData[1:]




















