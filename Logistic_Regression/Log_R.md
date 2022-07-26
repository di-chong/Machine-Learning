# logistics回归

## 1.定义
简单来说， 逻辑回归（Logistic Regression）是一种用于解决二分类（0 or 1）问题的机器学习方法，用于估计某种事物的可能性。比如某用户购买某商品的可能性，某病人患有某种疾病的可能性，以及某广告被用户点击的可能性等。 注意，这里用的是“可能性”，而非数学上的“概率”，logisitc回归的结果并非数学定义中的概率值，不可以直接当做概率值来用。该结果往往用于和其他特征值加权求和，而非直接相乘。

## 2.分类还是回归？决策边界？
经典的二分类算法，也可以多分类，非回归。
边界可以是非线性的

## 3.通过sigmoid函数将函数映射到0-1的概率问题上
![sigmoid映射](https://github.com/di-chong/Machine-Learning/blob/main/Logistic_Regression/picture/1.png)

## 4.决策边界函数: g(x)=0
### 1.线性边界
![线性边界](https://github.com/di-chong/Machine-Learning/blob/main/Logistic_Regression/picture/2.png)

### 2.非线性边界
![非线性边界](https://github.com/di-chong/Machine-Learning/blob/main/Logistic_Regression/picture/3.png)

### 3.似然函数：本来找概率最大值，转化为用梯度下降找最小值
![梯度下降](https://github.com/di-chong/Machine-Learning/blob/main/Logistic_Regression/picture/4.png)

### 4.求导：梯度一定是正数，此时下降趋势求导为负数，梯度则要添加负号
![求导-最终函数](https://github.com/di-chong/Machine-Learning/blob/main/Logistic_Regression/picture/5.png)


## 5.参数更新
![更新参数](https://github.com/di-chong/Machine-Learning/blob/main/Logistic_Regression/picture/6.png)

