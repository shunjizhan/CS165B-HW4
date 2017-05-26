import sys
from numpy import matrix
from math import sqrt

def toF(array):
  return [float(x) for x in array]

def readFile(filename):
  lines = [toF(line.rstrip('\n').rstrip('\r').split()) for line in open(filename)]
  return lines

def findCentroids(data, dimension):
  pointCount = len(data)
  theSum = []
  for k in range (0, dimension):
    theSum.append(0)

  for i in range(0, pointCount):
    point = data[i]
    for j in range (0, dimension):
      theSum[j] = theSum[j] + point[j]

  centroid = []
  for a in range (0, dimension):
    centroid.append(theSum[a] / pointCount)

  return matrix(centroid)

def printCentroid(centroid):
  print "Centroid:"
  n = len(centroid)
  for i in range(n):
    print centroid[i], " ",
  print " "

def printCov(cov):
  print "Covariance Matrix:"
  n = len(cov)
  m = len(cov[0])
  for i in range(n):
    for j in range(m):
      print cov[i][j], " ",
    print " "

def printPoint(p):
  print p[0], " ", p[1], " -- ",

##### training
trainingData = readFile(sys.argv[1])
M = int(trainingData[0][0])
N = int(trainingData[0][1])
trainingData = trainingData[1:]

centroid =  findCentroids(trainingData, N)
trainingData = matrix(trainingData)
XZ = trainingData - centroid
covariance = XZ.T * XZ / M
# covariance = (trainingData.T * trainingData) / M - centroid.T * centroid

printCentroid(centroid.tolist()[0])
printCov(covariance.tolist())

##### testing
testingData = readFile(sys.argv[2])
M_test = int(testingData[0][0])
N_test = int(testingData[0][1])
testingData = testingData[1:]

print "Distances:"
for i in range(len(testingData)):
  p = matrix(testingData[i])
  distance = sqrt( (p - centroid) * covariance.I * (p - centroid).T )
  print str(i) + ". ",
  printPoint(testingData[i])
  print distance



















