from numpy import *
import operator
import matplotlib.pyplot as plt


# 算法大致流程为，通过比对测试集与训练集的差距，进行最近标签归类。通过对标签的count进行判断
# 数据集中训练集是否不够均衡，做分类抽样效果应该更好些？

def file2matrix(fileName):
    fr = open(fileName)

    arrayOfLines = fr.readlines()
    numberOfLines = len(arrayOfLines)
    returnMat = zeros((numberOfLines, 3))
    classLabelVector = []
    index = 0
    for line in arrayOfLines:
        line = line.strip()
        listFromLine = line.split('\t')
        returnMat[index, :] = listFromLine[0:3]
        # 获取标签放入向量
        if listFromLine[-1] == 'largeDoses':
            classLabelVector.append(3)
        elif listFromLine[-1] == 'smallDoses':
            classLabelVector.append(2)
        elif listFromLine[-1] == 'didntLike':
            classLabelVector.append(1)
        else:
            classLabelVector.append(int(listFromLine[-1]))
        index += 1
    return returnMat, classLabelVector


# 归一化特征值
def autoNorm(dataSet):
    minValues = dataSet.min(0)
    maxValues = dataSet.max(0)
    ranges = maxValues - minValues
    normDataSet = zeros(shape(dataSet))
    m = dataSet.shape[0]
    normDataSet = dataSet - tile(minValues, (m, 1))
    normDataSet = normDataSet / tile(ranges, (m, 1))
    return normDataSet, ranges, minValues


def datingClassTest():
    hoRatio = 0.1
    datingDataMat, datingLabels = file2matrix('datingTestSet.txt')
    normMat, ranges, minValues = autoNorm(datingDataMat)
    m = normMat.shape[0]
    numTestVecs = int(m * hoRatio)
    errorCount = 0.0
    for i in range(numTestVecs):
        classifierResult = classify0(normMat[i, :], normMat[numTestVecs:m, :], datingLabels[numTestVecs:m], 3)
        print("the classifier came back with : %d ,the real answer is : %d" % (classifierResult, datingLabels[i]))
        if classifierResult != datingLabels[i]:
            errorCount += 1.0
    print("the total error rate is %f" % (errorCount / float(numTestVecs)))


def createDataSet():
    group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    label = ['A', 'A', 'B', 'B']
    return group, label


def classify0(inX, dataSet, labels, k):
    # shape 返回[行数 列数]
    dataSetSize = dataSet.shape[0]
    # 复制inX，按照dataSet行1列进行复制 复制后减去dataSet
    diffMat = tile(inX, (dataSetSize, 1)) - dataSet
    sqDiffMat = diffMat ** 2
    # 矩阵每一行相加
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances ** 0.5
    # 返回distances中元素从小到大排序后的索引值
    sortedDistIndicies = distances.argsort()
    classCount = {}
    for i in range(k):
        # 取出前k个元素的类别
        voteIlabel = labels[sortedDistIndicies[i]]
        # 计算类别次数 类别如果在字典中存在，则取出其值后加1 如果不存在取默认值再+1
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    # items 以map形式返回可遍历数组
    # key=operator.itemgetter(1)根据字典的值进行排序
    # key=operator.itemgetter(0)根据字典的键进行排序
    # reverse降序排序字典
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
    print(sortedClassCount[0][0])
    return sortedClassCount[0][0]


def classifyPerson():
    resultList = ['not at all', 'in small doses', 'in large doses']
    precentTats = float(input("precentage of time spent playing video games?"))
    ffMiles = float(input("frequent flier miles earned per year?"))
    iceCream = float(input("listers of ice cream consumed per year?"))
    datingDataMat, datingLabels = file2matrix('datingTestSet2.txt')
    normMat, ranges, minValues = autoNorm(datingDataMat)
    inArr = array([ffMiles, precentTats, iceCream])
    classifierResult = classify0((inArr - minValues) / ranges, normMat, datingLabels, 3)
    print("you will probably like this person :", resultList[classifierResult - 1])


# file2matrix('datingTestSet.txt')
# group, labels = createDataSet()
# classify0([-2, 2], group, labels, 3)
# datingClassTest()
# classifyPerson()
