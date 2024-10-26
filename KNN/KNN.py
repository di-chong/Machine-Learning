# 对轴承的时序信号进行分类

# 1. 导入库
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# 2. 读取数据
x = np.load('../dataset/Save_Data_CWRU/data.npy')
y = np.load('../dataset/Save_Data_CWRU/label.npy')

# 3. 划分数据集，默认打乱顺序
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

# 4. 关键：
#      1. K值的选取
#      2. 距离的度量
#      3. 利用广播机制来求待测点与训练集的距离矩阵,但是该方法有弊端，会存在内存不足的现象，
#         当你尝试计算400个样本与1600个样本之间的距离矩阵时，
#         虽然返回的是 400 * 1600 的矩阵，但数组运算需要大约 400 * 1600 * 1024 的内存

# 5. 方法一：自定义邻近距离
# # 5.1 广播机制求距离矩阵---有弊端
# def euclidean_dis(X_test, X_train):
#     x_test = x_test.reshape(-1,1,1024)
#     # 广播后的形状为 (400, 1600, 1024)，然后我们可以计算每个对应元素之间的差的平方和，再开方，发现内存不足
#     dis = np.sqrt(np.sum((X_test - X_train) ** 2, axis=2))
#     return dis

# 5.2 推荐---直接利用公式
def euclidean_dis(x1, x2):
    """
    返回x1与x2的距离(x1,x2均为二维矩阵).x1.shape=(N1*M),x2.shape=(N2*M2),返回结果为(N1*N2)
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

def predict(x_train, y_train, x_test, k=5):
    """
    返回根据KNN预测的结果
    :param train_x: 训练集x
    :param y: 训练集y
    :param test: 预测集
    :return: 返回test预测的结果
    """
    dis = euclidean_dis(x_test, x_train)
    k_neighbor = np.argsort(dis, axis=1)[:, :k]
    k_neighbor_value = y_train[k_neighbor]
    n = x_test.shape[0]  # 预测结果的个数
    pred = np.zeros(n)
    for i in range(n):
        pred[i] = np.argmax(np.bincount(k_neighbor_value[i]))
    return pred
preds = predict(x_train, y_train, x_test)
print("预测结果的正确率为:", np.sum(preds == y_test)/len(y_test))

# 6. 方法二：利用sk_learn封装的KNN代码
# best_k = 0
# best_accuracy = 0
# for k in range(1, 101, 3):  # 测试从1到20的k值
#     print('k = ', k)
#     knn = KNeighborsClassifier(n_neighbors=k)
#     knn.fit(X_train, y_train)
#     y_pred = knn.predict(X_test)
#     accuracy = accuracy_score(y_test, y_pred)
#     if accuracy > best_accuracy:
#         best_accuracy = accuracy
#         best_k = k
#         print(f"跟新k值: {best_k}, 更新准确率: {best_accuracy:.2f}")
# print(f"最佳k值: {best_k}, 最佳准确率: {best_accuracy:.2f}")

