from numpy import *
import matplotlib as mpl
import kNN
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

print(mpl.matplotlib_fname())
mpl.rcParams['font.sans-serif'] = ["Droid Sans Fallback"]
# mpl.rcParams['axes.unicode_minus'] = False
datingDataMat, datingLabels = kNN.file2matrix('datingTestSet2.txt')
fig1 = plt.figure()

ax = fig1.add_subplot(2, 2, 1)
ax.scatter(datingDataMat[:, 1], datingDataMat[:, 2])
plt.xlabel(u'x  玩视频游戏所耗时间半分比')
plt.ylabel(u'y  每周消费的冰淇淋公升数')
plt.title(u'图一(2&&3)')

# 定义三个类别的空列表
type1_x = []
type1_y = []
type2_x = []
type2_y = []
type3_x = []
type3_y = []

# 第二个子图 是第2个特征和第3个特征的散点图
ax = fig1.add_subplot(2, 2, 2)

# 循环获得每个列表中的值
for i in range(len(datingLabels)):
    # 不喜欢
    if datingLabels[i] == 1:
        type1_x.append(datingDataMat[i][1])
        type1_y.append(datingDataMat[i][2])
    # 魅力一般
    if datingLabels[i] == 2:
        type2_x.append(datingDataMat[i][1])
        type2_y.append(datingDataMat[i][2])
    # 极具魅力
    if datingLabels[i] == 3:
        type3_x.append(datingDataMat[i][1])
        type3_y.append(datingDataMat[i][2])

type1 = ax.scatter(type1_x, type1_y, s=20, c='red')
type2 = ax.scatter(type2_x, type2_y, s=40, c='green')
type3 = ax.scatter(type3_x, type3_y, s=50, c='blue')
ax.legend((type1, type2, type3), (u'不喜欢', u'魅力一般', u'极具魅力'), loc=2)  # 显示图例  1 右上  2左上 3左下 4 右下 逆时针
# ax.scatter(datingDataMat[:,1],datingDataMat[:,2],15.0*array(datingLabels),15.0*array(datingLabels))
plt.xlabel(u'x  玩视频游戏所耗时间半分比')
plt.ylabel(u'y  每周消费的冰淇淋公升数')
plt.title(u'图二(2&&3)')

# 第三个子图 是第1个特征和第2个特征的散点图
ax = fig1.add_subplot(2, 2, 3)  # 代表创建1行1列从上到下的第三块的子图
# 循环获得每个列表中的值
for i in range(len(datingLabels)):
    # 不喜欢
    if datingLabels[i] == 1:
        type1_x.append(datingDataMat[i][0])
        type1_y.append(datingDataMat[i][1])
    # 魅力一般
    if datingLabels[i] == 2:
        type2_x.append(datingDataMat[i][0])
        type2_y.append(datingDataMat[i][1])
    # 极具魅力
    if datingLabels[i] == 3:
        type3_x.append(datingDataMat[i][0])
        type3_y.append(datingDataMat[i][1])

type1 = ax.scatter(type1_x, type1_y, s=20, c='red')
type2 = ax.scatter(type2_x, type2_y, s=40, c='green')
type3 = ax.scatter(type3_x, type3_y, s=50, c='blue')
ax.legend((type1, type2, type3), (u'不喜欢', u'魅力一般', u'极具魅力'), loc=2)  # 显示图例  1 右上  2左上 3左下 4 右下 逆时针
ax.scatter(datingDataMat[:,0],datingDataMat[:,1],15.0*array(datingLabels),15.0*array(datingLabels))
plt.xlabel(u'x  每年获取的飞行常客里程数')
plt.ylabel(u'y  玩视频游戏所耗时间半分比')
plt.title(u'图三(1&&2)')

# 第四个子图 是第1个特征和第3个特征的散点图
# 代表创建1行1列从上到下的第四块的子图
ax = fig1.add_subplot(2, 2, 4)
# 循环获得每个列表中的值
for i in range(len(datingLabels)):
    # 不喜欢
    if datingLabels[i] == 1:
        type1_x.append(datingDataMat[i][0])
        type1_y.append(datingDataMat[i][2])

    # 魅力一般
    if datingLabels[i] == 2:
        type2_x.append(datingDataMat[i][0])
        type2_y.append(datingDataMat[i][2])

    # 极具魅力
    if datingLabels[i] == 3:
        type3_x.append(datingDataMat[i][0])
        type3_y.append(datingDataMat[i][2])

type1 = ax.scatter(type1_x, type1_y, s=20, c='red')
type2 = ax.scatter(type2_x, type2_y, s=40, c='green')
type3 = ax.scatter(type3_x, type3_y, s=50, c='blue')
ax.legend((type1, type2, type3), (u'不喜欢', u'魅力一般', u'极具魅力'), loc=2)  # 显示图例  1 右上  2左上 3左下 4 右下 逆时针
# ax.scatter(datingDataMat[:,0],datingDataMat[:,2],15.0*array(datingLabels),15.0*array(datingLabels))
plt.xlabel(u'x  每年获取的飞行常客里程数')
plt.ylabel(u'y  每周消费的冰淇淋公升数')
plt.title(u'图四(1&&3)')

# 三维
# 第二个图 是第1个特征和第2个特征和第3个特征的散点图
fig2 = plt.figure()
ax = fig2.add_subplot(111)
ax = Axes3D(fig2)
ax.scatter(datingDataMat[:, 0], datingDataMat[:, 1], datingDataMat[:, 2], 15.0 * array(datingLabels),
           15.0 * array(datingLabels), 15.0 * array(datingLabels))
ax.set_xlabel(u'x  每年获取的飞行常客里程数')
ax.set_ylabel(u'y  玩视频游戏所耗时间半分比')
ax.set_zlabel(u'z  每周消费的冰淇淋公升数')

plt.title(u'图四(1&&2&&3)')
plt.show()
