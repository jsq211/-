# 随机梯度下降法　在下降中根据个体进行遍历　相对梯度下降中取整个矩阵进行权重计算时间上肯定更少
# 　但是相对的　通过个体进行迭代计算肯定更容易陷入局部最优中，图示结果中也可以看出

import numpy as np
import matplotlib.pyplot as plt


def stocGradAscent0(dataMatrix, classLabel):
    m, n = np.shape(dataMatrix)
    alpha = 0.01
    weight = np.ones(n)
    for i in range(m):
        h = sigmoid(sum(dataMatrix[i] * weight))
        error = classLabel[i] - h
        weight = weight + alpha * error * dataMatrix[i]
    return weight


# 书上代码有误　没注意说明　plot的方法中由于weight的格式有更改，不是矩阵形式，因此getA应该改为tolist
def plotBestFit(weight):
    w = weight.tolist()
    dataMat, labelMat = loadDataSet()
    dataArr = np.array(dataMat)
    n = np.shape(dataArr)[0]
    xcord1 = []
    ycord1 = []
    xcord2 = []
    ycord2 = []
    for i in range(n):
        if int(labelMat[i]) == 1:
            xcord1.append(dataArr[i, 1])
            ycord1.append(dataArr[i, 2])
        else:
            xcord2.append(dataArr[i, 1])
            ycord2.append(dataArr[i, 2])
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(xcord1, ycord1, s=30, c='red', marker='s')
    ax.scatter(xcord2, ycord2, s=30, c='green')
    x = np.arange(-3.0, 3.0, 0.1)
    y = (-w[0] - w[1] * x) / w[2]
    ax.plot(x, y)
    plt.xlabel('X1')
    plt.ylabel('X2')
    plt.show()


def loadDataSet():
    dataMat = []
    labelMat = []
    fr = open('testSet.txt', 'r')
    # 初始化参数读取和设置，x0取1 即直接对应常数项
    for line in fr.readlines():
        lineArr = line.strip().split()
        dataMat.append([1.0, float(lineArr[0]), float(lineArr[1])])
        labelMat.append(int(lineArr[2]))
    return dataMat, labelMat


def sigmoid(inx):
    return 1.0 / (1 + np.exp(-inx))


# 所谓的优化随机梯度下降法　实质上就是在进行梯度下降时进行随机个体计算error和权重
# 类似遗传　蚁群　退火　之类的启发式算法　随机看脸～
# 惊了　效果看起来和梯度下降法差不多　果然是500次大力出奇迹
def stocGradAscen1(dataMatrix, classLabels):
    numItem = 500
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


dataArray, labelMat = loadDataSet()
weights = stocGradAscen1(np.array(dataArray), labelMat)
# weights = stocGradAscent0(np.array(dataArray), labelMat)
plotBestFit(weights)
