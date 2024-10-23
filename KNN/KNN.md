### 1. 问题详情：

我们生活中会遇到很多决策？比如：今天中午吃什么；我该买什么手机？遇到问题你会怎么解决？

下面是三个选择去辅助你做决策：

1. 随机找一个人问；

   **2. 问问周围人的选择；**

3. 做一份详细的统计，根据自身情况量身定制方案。

回到问题中，当我们在选择手机时，除了极个别人明确手机性能，颜值外，大多人都是根据周围人的手机类型来选择。![1729088633666](C:\Users\houliang wang\AppData\Roaming\Typora\typora-user-images\1729088633666.png)

### 2. 问题分析：

具体可能会经过下面几个步骤：

![1729088831598](C:\Users\houliang wang\AppData\Roaming\Typora\typora-user-images\1729088831598.png)

### 3. 总结：

![1729089152970](C:\Users\houliang wang\AppData\Roaming\Typora\typora-user-images\1729089152970.png)

### 4.距离算法的优化：

1. 欧氏距离
2. **python的广播机制**：比如：预测的维度是5-1024(5个数据，每个数据包含1024个数据点)，训练数据是500-1024，理论上存在5×500的距离矩阵。我们只需要将预测维度为5-1-1024，训练和测试的数据都会广播为5-500-1024，最欧氏距离会得到5×500×1的距离矩阵。![1729095381390](C:\Users\houliang wang\AppData\Roaming\Typora\typora-user-images\1729095381390.png)
3. 当然也可以直接通过维度拓展生成这种广播形式
4. 但是广播机制内部还是会设计1024个数据点之间的运算，如果样本数量多，会存在内存不足的现象
5. **直接利用公式**![1729177020107](C:\Users\houliang wang\AppData\Roaming\Typora\typora-user-images\1729177020107.png)

```
def euclidean_dis(x1, x2):
    """
    x1与x2的距离(x1,x2均为二维矩阵).x1.shape=(N1*M),x2.shape=(N2*M),返回结果为(N1*N2)
    :param x1:
    :param x2:
    :return:
    """
    n1, m1 = x1.shape
    n2, m2 = x2.shape
    if m1 != m2:
        raise ("两个向量维度不相等")
    x1x2 = np.dot(x1, x2.T)  # (n1,n2)
    y1 = np.repeat(np.reshape(np.sum(np.multiply(x1, x1), axis=1), (n1, 1)), repeats=n2, axis=1)
    y2 = np.repeat(np.reshape(np.sum(np.multiply(x2, x2), axis=1), (n2, 1)), repeats=n1, axis=1).T
    dis = y1 + y2 - 2 * x1x2
    return dis
```

