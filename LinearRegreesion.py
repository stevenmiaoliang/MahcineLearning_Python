######################################
#Machine Learning
#Linear Regression
#Author:steven.miaoliang@gmail.com
#Data:2016/5/23
######################################

from numpy import *
import matplotlib.pyplot as plt
import time

#formula
def leastSquares(train_x,train_y):
    train_xt = train_x.T
    dotTrainX = dot(train_xt,train_x)
    matX = mat(dotTrainX)
    dotTrainXInversion = matX.I
    theta = dotTrainXInversion*train_xt;
    theta = theta*train_y;
    return theta

def LMS(train_x,train_y,opts):
    numSamples, numfeatures = shape(train_x)
    alpha = opts['alpha'];
    maxIter = opts['maxIter']
    weights = ones((numfeatures, 1))
    for k in range(maxIter):
        if (opts['optimizeType'] == 'gradDescent'):
            output = train_x*weights
            error = train_y - output
            weights = weights + alpha * train_x.transpose() * error
    return  weights
