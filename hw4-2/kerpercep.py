import sys
from numpy import matrix
from math import exp

def toF(array):
  return [float(x) for x in array]

def readFile(filename):
  lines = [toF(line.rstrip('\n').rstrip('\r').split()) for line in open(filename)]
  return lines

def K(x1, x2, sigma):
  return exp(-1.0 * ((x1-x2) * (x1-x2).T) / 2.0 * sigma**2)

def kernalPerceptron(D, K, Y):
  n = len(D)
  a = [0] * n
  converged = False
  while(converged == False):
    converged = True
    for i in range(n):
      if (Y[i] * sum([a[j] * Y[j] * K[i][j] for j in range(n)]) <= 0):
        a[i] = a[i] + 1
        converged = False
  return a

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

K_matrix = [[K(matrix(trainingData[i]), matrix(trainingData[j]), sigma) for j in range(M)] for i in range(M)]
Y = [1] * M_pos + [-1] * M_neg
alpha = kernalPerceptron(trainingData, K_matrix, Y)

print "Alphas: ",
for i in range(len(alpha)):
  print alpha[i],
print " "

##### testing
testingData_pos = readFile(sys.argv[4])
testingData_neg = readFile(sys.argv[5])

M_test_pos = int(testingData_pos[0][0])
M_test_neg = int(testingData_neg[0][0])
N_test_pos = int(testingData_pos[0][1])
N_test_neg = int(testingData_neg[0][1])
M_test = M_test_neg + M_test_pos

testingData_pos = testingData_pos[1:]
testingData_neg = testingData_neg[1:]
testingData = testingData_pos + testingData_neg

FP = 0
FN = 0
for i in range(M_test_pos):
  if (sum([alpha[i] * Y[i] * K(x, matrix(testingData_pos[i]), sigma) for x in testingData]) <= 0):
    FN += 1

for j in range(M_test_neg):
  if (sum([alpha[j] * Y[j] * K(y, matrix(testingData_neg[j]), sigma) for y in testingData]) >= 0):
    FP += 1

print "False positives: ", FP
print "False negatives: ", FN
print "Error rate: ", str((FP + FN) * 100.0 / M) + "%"


















