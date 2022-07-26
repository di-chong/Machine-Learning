# K-MEANS：

## 1.聚类概念：
    无监督：无标签
    聚类：相似的聚在一起
    难点
        无标签：没有标准答案
        如何评估，如何调参


## 2.K-MEANS算法：
    1.聚类的其中一种，并且简单实用
    2.要得到簇的个数，需要指定K值
    3.质心：均值，即向量各维取平均
    4.距离的量度：常用欧几里得距离和余弦相似度（先标准化）
    5.目标函数--1.簇内的点到簇的距离之和
                2.各个簇的距离总和
   ![目标](https://github.com/di-chong/Machine-Learning/blob/main/K_Means/picture/1.png)

## 3.具体步骤
![步骤](https://github.com/di-chong/Machine-Learning/blob/main/K_Means/picture/2.png)
## 4.优缺点:
    难以区分簇的3种情况：
        1.环绕的，交叉的难以区分簇
   ![环绕型](https://github.com/di-chong/Machine-Learning/blob/main/K_Means/picture/4.png)
   
        2.初值的选取对结果影响巨大
   ![初值的影响](https://github.com/di-chong/Machine-Learning/blob/main/K_Means/picture/5.png)
   
        3.不清楚应该分为几个簇
   ![簇值无法确定](https://github.com/di-chong/Machine-Learning/blob/main/K_Means/picture/6.png)
   
   ### 总结：
   
![总结](https://github.com/di-chong/Machine-Learning/blob/main/K_Means/picture/3.png)
        



