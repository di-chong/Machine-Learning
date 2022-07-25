import numpy as np
from .normalize import normalize
from .generate_sinusoids import generate_sinusoids
from .generate_polynomials import generate_polynomials

# normalize_data 归一化
# polynomial_degree 多项式
# sinusoid_degree 正弦曲线
"""数据预处理"""
def prepare_for_training(data, polynomial_degree=0, sinusoid_degree=0, normalize_data=True):

    # 计算样本总数
    num_examples = data.shape[0]
    #np.copy()深拷贝，地址不同，=浅拷贝
    data_processed = np.copy(data)

    # 预处理
    features_mean = 0  # 均值
    features_deviation = 0  #偏差
    data_normalized = data_processed

    # 执行标准化，归一化
    if normalize_data:
        (
            data_normalized,
            features_mean,
            features_deviation
        ) = normalize(data_processed)

        data_processed = data_normalized

    # 特征变换sinusoid
    if sinusoid_degree > 0:
        sinusoids = generate_sinusoids(data_normalized, sinusoid_degree)
        data_processed = np.concatenate((data_processed, sinusoids), axis=1)

    # 特征变换polynomial
    if polynomial_degree > 0:
        polynomials = generate_polynomials(data_normalized, polynomial_degree, normalize_data)
        data_processed = np.concatenate((data_processed, polynomials), axis=1)

    # 加一列1，hstack()把两个数组水平合并，即行相同
    # 加一列是为了保障x0,x(i)与theta(i)相乘
    data_processed = np.hstack((np.ones((num_examples, 1)), data_processed))

    return data_processed, features_mean, features_deviation



