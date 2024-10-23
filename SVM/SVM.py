# 对轴承的时序信号进行分类

# 1. 导入库
import numpy as np
from sklearn.decomposition import PCA
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import make_pipeline
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# 2. 读取数据
x = np.load('../dataset/Save_Data_CWRU/data.npy')
y = np.load('../dataset/Save_Data_CWRU/label.npy')

# 3. 划分数据集，默认打乱顺序：(8000 + 2000) * 1024
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

# 4.训练模型
# 4.1 由于数据维度太高，我们先对数据降维----SVM不适应与高纬度
pca = PCA(n_components=150, random_state=0)
svm = SVC(kernel='rbf', random_state=0)
model = make_pipeline(pca, svm)
# 4.2 用网络搜索交叉检验来寻找最优参数组合
param_gird = {'svc__C': [1,5,10,50], 'svc__gamma': [0.0001,0.0005,0.001,0.005]}
grid = GridSearchCV(model, param_gird, cv=5)   # cv=5表示交叉验证的折数
# 4.2 模型训练，最优参数代入模型
grid.fit(x_train, y_train)
print(grid.best_params_)
model = grid.best_estimator_
# 4.3 模型评估
y_pred = model.predict(x_test)
acc = accuracy_score(y_test, y_pred)
print(f"accuracy: {acc: .4f}")
# 4.4 报告输出
print(classification_report(y_test, y_pred))




