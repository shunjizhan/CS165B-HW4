import sys
from numpy import matrix
from math import exp

def toF(array):
  return [float(x) for x in array]

def readFile(filename):
  lines = [toF(line.rstrip('\n').rstrip('\r').split()) for line in open(filename)]
  return lines

def K(x1, x2, sigma):
  return exp(-2.0 * ((x1-x2) * (x1-x2).T) / sigma**2)

def KernalPerceptron(D, K):
  return

##### training
sigma = float(sys.argv[1])
trainingData_pos = readFile(sys.argv[2])
trainingData_neg = readFile(sys.argv[3])

M_pos = int(trainingData_pos[0][0])
M_neg = int(trainingData_neg[0][0])
M = M_pos + M_neg

N_pos = int(trainingData_pos[0][1])
N_neg = int(trainingData_neg[0][1])
N = N_pos + N_neg

trainingData_pos = trainingData_pos[1:]
trainingData_neg = trainingData_neg[1:]
trainingData = trainingData_pos + trainingData_neg

K_matrix = [[K(matrix(trainingData[i]), matrix(trainingData[j]), sigma) for j in range(10)] for i in range(10)]
print K_matrix

##### testing
testingData_pos = readFile(sys.argv[2])
testingData_neg = readFile(sys.argv[3])

M_test_pos = int(testingData_pos[0][0])
M_test_neg = int(testingData_neg[0][0])
N_test_pos = int(testingData_pos[0][1])
N_test_neg = int(testingData_neg[0][1])

testingData_pos = testingData_pos[1:]
testingData_neg = testingData_neg[1:]




















