import matplotlib.pyplot as plt
import matplotlib as mpl

# linux根据fname查不到matplotlib的文件夹，只能直接查到matplotlibrc，改里面的文件无法有效修改中文显示
# 索性直接用英文了。。
# mpl.rcParams['font.sans-serif'] = ["Droid Sans Fallback"]
decisionNode = dict(boxstyle="sawtooth", fc="0.8")
leafNode = dict(boxstyle="round4", fc="0.8")
arrow_args = dict(arrowstyle="<-")


def plotNode(nodeTxt, centerPt, parentPt, nodeType):
    createPlot.ax1.annotate(nodeTxt, xy=parentPt, xycoords='axes fraction',
                            xytext=centerPt, textcoords='axes fraction', va="center", ha="center", bbox=nodeType,
                            arrowprops=arrow_args)


def createPlot():
    fig = plt.figure(1, facecolor='white')
    fig.clf()
    createPlot.ax1 = plt.subplot(111, frameon=False)
    plotNode(U'decisionNode', (0.5, 0.1), (0.1, 0.5), decisionNode)
    plotNode(U'treeNode', (0.8, 0.1), (0.3, 0.8), leafNode)
    plt.show()


def getNumLeafs(myTree):
    numLeafs = 0
    firstStr = list(myTree.keys())
    secondDict = myTree[firstStr[0]]
    for key in secondDict.keys():
        if type(secondDict[key]) == dict:
            numLeafs += getNumLeafs(secondDict[key])
        else:
            numLeafs += 1
    return numLeafs


def getTreeDepth(myTree):
    maxDepth = 0
    thisDepth = 0
    firstStr = list(myTree.keys())
    secondDict = myTree[firstStr[0]]
    for key in secondDict.keys():
        if type(secondDict[key]) == dict:
            thisDepth += getTreeDepth(secondDict[key])
        else:
            thisDepth += 1
        if thisDepth > maxDepth:
            maxDepth = thisDepth
    return maxDepth


def retrieveTree(i):
    listOfTrees = [{'no surfacing': {0: 'no', 1: {'flippers': {0: 'no', 1: 'yes'}}}},
                   {'no surfacing': {0: 'no', 1: {'flippers': {0: {'head': {0: 'no', 1: 'yes'}}, 1: 'no'}}}}]
    return listOfTrees[i]
