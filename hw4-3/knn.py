import sys
from numpy import matrix
from math import sqrt

def toF(array):
  return [float(x) for x in array]

def readFile(filename):
  lines = [toF(line.rstrip('\n').rstrip('\r').split()) for line in open(filename)]
  return lines

def findLargestIndex(knn):
  index = 0
  maxDist = knn[0]["distance"]
  for i in range(1, len(knn)):
    if (knn[i]["distance"] > maxDist):
      index = i
      maxDist = knn[i]["distance"]
  return index

def printKNN(knn):
  for i in range(len(knn)):
    knn[i]["point"].show()
  print " "

def printLabels(labels):
  for label in labels:
    print "label = ", label,
    for x in labels[label]:
      print x, "=", labels[label][x],
    print ""
  print " "

class Point:
  def __init__(self, description):
    description = [float(x) for x in description]
    self.coordinate = description[:-1]
    self.label = description[-1]

  def show(self):
    for i in range(len(self.coordinate)):
      print self.coordinate[i],
    # print " -- ", self.label,
    print " -- ",

  def distance(self, p):
    sum = 0
    for i in range(len(self.coordinate)):
      sum += (self.coordinate[i] - p.coordinate[i])**2
    return sqrt(sum)

##### training
trainingData = readFile(sys.argv[2])
M = int(trainingData[0][0])
N = int(trainingData[0][1])
trainingData = trainingData[1:]

Points = []
for i in range(M):
  Points.append(Point(trainingData[i]))

##### testing
n = int(sys.argv[1])
testingData = readFile(sys.argv[3])
M_test = int(testingData[0][0])
N_test = int(testingData[0][1])
testingData = testingData[1:]

for x in range(M_test):
  currentPoint = Point(testingData[x] + [0.0])
  knn = []
  for i in range(n):
    comparePoint = Points[i]
    knn.append({"point": comparePoint, "distance": comparePoint.distance(currentPoint)}) # initial closest points
  largestIndex = findLargestIndex(knn)

  for j in range(n, M):
    maxDist = knn[largestIndex]["distance"]
    comparePoint = Points[j]
    # print comparePoint.distance(currentPoint), "<", maxDist
    if (comparePoint.distance(currentPoint) < maxDist):   # found closer point and finalize knn
      knn[largestIndex] = { "point": comparePoint, "distance": comparePoint.distance(currentPoint) }
      largestIndex = findLargestIndex(knn)

  # determine the predicted label according to knn
  # printKNN(knn)
  labels = {}
  for i in range(len(knn)):
    p = knn[i]
    label = p["point"].label
    distance = p["distance"]

    if (label in labels):
      labels[label]["count"] += 1
      if (distance < labels[label]["minDist"]):
        labels[label]["minDist"] = distance
    else:
      labels[label] = { "count": 1, "minDist": distance }

  # printLabels(labels)
  maxCount = -1
  prediction = -1
  minDist = 999999999999
  for label in labels:
    count = labels[label]["count"]
    dist = labels[label]["minDist"]
    if (count > maxCount or (count == maxCount and dist < minDist)):
      maxCount = count
      prediction = label
      minDist = dist
  print str(x + 1) + ".",
  currentPoint.show()
  print int(prediction)

















