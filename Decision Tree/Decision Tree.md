# 决策树

## （1）决策树是一种基本的分类与回归方法。

## （2）决策树通常有三个步骤：
    特征的选择优先级；
    决策树的生成；
    决策树的修剪。


## （3）不纯度函数(impurity function)：
1.决策树最重要的概念就是不纯函数(I)的概念. 当一个节点需要分割的时候, 实际上就是找到一个合适的特征的一个合适的取值作为阈值(thresh)进行分割. 那么问题来了, 怎么找到那个合适的特征的合适的取值呢? 主要的依据就是不纯度的变化(delta I). 首先我们给出不纯度函数的定义. 不纯度函数不是一个具体的函数, 它是满足一系列约束的函数的总称.

2.两个常用不纯度函数, 信息熵(info entropy)和基尼指数(gini index).

## （4）信息熵(info entropy)：
表示状态的混乱程度，熵越大越混乱。

![](https://github.com/di-chong/Machine-Learning/blob/main/Decision%20Tree/picture/1.png)

## （5）条件熵(Conditional entropy)

![](https://github.com/di-chong/Machine-Learning/blob/main/Decision%20Tree/picture/2.png)

## （6）信息增益，ID3算法构建决策树（最基本的模型，简单实用，但在某些场合有缺陷）
信息增益就是信息熵与条件熵的差值：

![](https://github.com/di-chong/Machine-Learning/blob/main/Decision%20Tree/picture/3.png)

ID3算法：递归构建过程中，使用信息增益的方法进行特征选择

![](https://github.com/di-chong/Machine-Learning/blob/main/Decision%20Tree/picture/4.png)

## （7）C4.5

## （8）基尼指数：生成的是二叉树

## （9）剪枝技术：
1.预剪枝

2.后剪枝

## （10）处理连续值与缺失值
连续值（比如工资薪水）：二分法将n个连续值划分为离散的，从小到大依次循环迭代二分（可以划分n-1个），找到使熵值最小的一组划分

缺失值：
1.计算整个熵值时不包含缺失值

2.计算某个特征的熵值时，给缺失值一个权重，其他的非确实值默认为1个数量，缺失值看在该特征在各个类别中的比例
举例：现在有年龄特征，分为青年中年老年三个类别，总共15给样本，其中该特征缺失了两个数据，导致青年样本为4，中年样本为4，老年样本为5，所有缺失值在青年，中年的权重为4/15，在老年的权重为5/15

3.缺失值可以归为各个类别，但是加了权重，比如青年就是：1+1+1+1+4/15+4/15

