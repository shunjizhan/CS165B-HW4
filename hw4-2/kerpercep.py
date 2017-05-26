import sys
from numpy import matrix
from math import sqrt

def toF(array):
  return [float(x) for x in array]

def readFile(filename):
  lines = [toF(line.rstrip('\n').rstrip('\r').split()) for line in open(filename)]
  return lines

##### training
trainingData_pos = readFile(sys.argv[2])
trainingData_neg = readFile(sys.argv[3])
M_pos = int(trainingData_pos[0][0])
M_neg = int(trainingData_neg[0][0])
N_pos = int(trainingData_pos[0][1])
N_neg = int(trainingData_neg[0][1])
trainingData_pos = trainingData_pos[1:]
trainingData_neg = trainingData_neg[1:]

##### testing
testingData_pos = readFile(sys.argv[2])
testingData_neg = readFile(sys.argv[3])
M_test_pos = int(testingData_pos[0][0])
M_test_neg = int(testingData_neg[0][0])
N_test_pos = int(testingData_pos[0][1])
N_test_neg = int(testingData_neg[0][1])
testingData_pos = testingData_pos[1:]
testingData_neg = testingData_neg[1:]




















