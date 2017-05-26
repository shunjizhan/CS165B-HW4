import sys
from numpy import matrix

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







trainingData = readFile(sys.argv[1])
testingData = readFile(sys.argv[2])

M = int(trainingData[0][0])
N = int(trainingData[0][1])
trainingData = trainingData[1:]

# print type(N)

centroid =  findCentroids(trainingData, N)
trainingData = matrix(trainingData)
Cov = (trainingData.T * trainingData) / M - centroid.T * centroid

print centroid
















