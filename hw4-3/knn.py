import sys
from numpy import matrix
from math import sqrt

def toF(array):
  return [float(x) for x in array]

def readFile(filename):
  lines = [toF(line.rstrip('\n').rstrip('\r').split()) for line in open(filename)]
  return lines

class Point:
  def __init__(self, description):
    description = [float(x) for x in description]
    self.coordinate = description[:-1]
    self.label = description[-1]

  def show(self):
    for i in range(len(self.coordinate)):
      print self.coordinate[i],
    print " -- ", self.label

##### training
trainingData = readFile(sys.argv[1])
M = int(trainingData[0][0])
N = int(trainingData[0][1])
trainingData = trainingData[1:]

Points = []
for i in range(M):
  Points.append(Point(trainingData[i]))

for j in range(M):
  Points[j].show()

##### testing
testingData = readFile(sys.argv[2])
M_test = int(testingData[0][0])
N_test = int(testingData[0][1])
testingData = testingData[1:]




















