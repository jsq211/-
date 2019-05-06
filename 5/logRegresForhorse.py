# 总感觉这个代码是有问题的　因为在数据处理的时候是直接去除了数据缺失的字段，权重应该对应收到影响
# 掏出matlab看了一下　代码中读的数据是处理过了的　缺失数据已经补0　其实和正常的预测就没有什么区别了　太秀了８
import numpy as np
import matplotlib.pyplot as plt


def sigmoid(inx):
    return 1.0 / (1 + np.exp(-inx))


def classifyVector(inX, weights):
    prob = sigmoid(sum(inX * weights))
    if prob > 0.5:
        return 1
    else:
        return 0


#
def stocGradAscen1(dataMatrix, classLabels, numItem=500):
    m, n = np.shape(dataMatrix)
    weights = np.ones(n)
    for i in range(numItem):
        dataIndex = list(range(m))
        for j in range(m):
            alpha = 4 / (1.0 + j + i) + 0.01
            randIndex = int(np.random.uniform(0, len(dataIndex)))
            h = sigmoid(sum(dataMatrix[randIndex] * weights))
            error = classLabels[randIndex] - h
            weights = weights + alpha * error * dataMatrix[randIndex]
            del (dataIndex[randIndex])
    return weights


def colicTest():
    frTrain = open('horseColicTraining.txt')
    frTest = open('horseColicTest.txt')
    trainingSet = []
    trainingLabels = []
    for line in frTrain.readlines():
        currLine = line.strip().split('\t')
        lineArr = []
        for i in range(21):
            lineArr.append(float(currLine[i]))
        trainingSet.append(lineArr)
        trainingLabels.append(float(currLine[21]))
    trainWeights = stocGradAscen1(np.array(trainingSet), trainingLabels, 500)
    errorCount = 0
    numTestVec = 0.0
    for line in frTest.readlines():
        numTestVec += 1
        currLine = line.strip().split('\t')
        lineArr = []
        for i in range(21):
            lineArr.append(float(currLine[i]))
        if int(classifyVector(np.array(lineArr), trainWeights)) != int(currLine[21]):
            errorCount += 1
    errorRate = (float(errorCount) / numTestVec)
    print('the weights is :', trainWeights)
    print('the error rate is %f' % errorRate)
    return errorRate


def multiTest():
    numTests = 10
    errorSum = 0.0
    for k in range(numTests):
        errorSum += colicTest()
    print('after %d iterations the average error rate is : %f' % (numTests, errorSum / float(numTests)))


multiTest()
