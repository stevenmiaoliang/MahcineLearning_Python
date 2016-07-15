######################################
#Machine Learning
#KNN
#Author:steven.miaoliang@gmail.com
#Data:2016/6/23
######################################

from numpy import  *
from sklearn import neighbors
import operator

def createTrainDataSet():
    group = array([[1.0,0.9], [1.0,1.0],[0.1,0.1],[0.0,0.1]])
    labels = ['A','A','B','B']
    return  group,labels

def kNNClassify(input,dataSet,labels,k):
    numSample = dataSet.shape[0]
    diff = tile(input,(numSample,1)) - dataSet
    squaredDiff = diff ** 2  # squared for the subtract
    squaredDist = sum(squaredDiff, axis=1)  # sum is performed by row
    distance = squaredDist ** 0.5

    ## step 2: sort the distance
    # argsort() returns the indices that would sort an array in a ascending order
    sortedDistIndices = argsort(distance)

    classCount = {}  # define a dictionary (can be append element)
    for i in xrange(k):
        ## step 3: choose the min k distance
        voteLabel = labels[sortedDistIndices[i]]

        ## step 4: count the times labels occur
        # when the key voteLabel is not in dictionary classCount, get()
        # will return 0
        classCount[voteLabel] = classCount.get(voteLabel, 0) + 1

        ## step 5: the max voted class will return
    maxCount = 0
    for key, value in classCount.items():
        if value > maxCount:
            maxCount = value
            maxIndex = key

    return maxIndex

dataSet, labels = createTrainDataSet()
testX = array([1.2, 1.0])
k = 3
outputLabel = kNNClassify(testX, dataSet, labels, 3)
print "Your input is:", testX, "and classified to class: ", outputLabel

testX = array([0.1, 0.3])
outputLabel = kNNClassify(testX, dataSet, labels, 3)
print "Your input is:", testX, "and classified to class: ", outputLabel
#sklearn
knn = neighbors.KNeighborsClassifier();
data = array([[3,104],[2,100],[1,81],[101,10],[99,5],[98,2]])
labels = array([1,1,1,2,2,2])
knn.fit(data,labels)
print  knn.predict([18,90])
