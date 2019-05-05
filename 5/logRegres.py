import numpy as np


def loadDataSet():
    dataMat = []
    labelMat = []
    fr = open('testSet.txt', 'r')
    # 初始化参数读取和设置，x0取1
    for line in fr.readlines():
        lineArr = line.strip().split()
        dataMat.append([1.0, float(lineArr[0]), float(lineArr[1])])
        labelMat.append(int(lineArr[2]))
    return dataMat, labelMat


def sigmoid(inx):
    return 1.0 / (1 + np.exp(-inx))


def gradAscent(dataMatIn, classLabels):
    dataMatrix = np.mat(dataMatIn)
    labelMat = np.mat(classLabels).transpose()
    m, n = np.shape(dataMatrix)

    alpha = 0.001
    maxCycles = 500
    weights = np.ones((n, 1))
    # 1.对数据进行二分类判别，计算标签误差
    # 2.权重更新，在原参数权重的基础上，以aplha步长和误差进行更新 负减小正增加，最终获得权重参数
    for k in range(maxCycles):
        h = sigmoid(dataMatrix * weights)
        error = labelMat - h
        weights = weights + alpha * dataMatrix.transpose() * error
    return weights


dataArr, labelMat = loadDataSet()
print(gradAscent(dataArr, labelMat))
