import pandas as pd
from sklearn.preprocessing import MinMaxScaler,OneHotEncoder # 预处理
from sklearn.cluster import KMeans # 聚类算法
from sklearn.metrics import silhouette_score # 用于评估度量的模块
import numpy as np

pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)
pd.set_option('max_colwidth',30)


data = pd.read_csv("ad_performance.csv",index_col=0)
print(data.describe().round(4).T)

#数据预处理
print(data[data.isna().values == True])
m = data['平均停留时间'].mean
print(m)
data = data.fillna(419.77)
print(data[data.isna().values == True])

#计算, 合并相关性 -> 避免聚类算法重复计算 夸大特征表现
print(data.corr().round(4).T)
# pd.DataFrame(data.corr().round(4).T).to_excel('ad_try.xlsx')
data = data.drop(['平均停留时间'],axis=1) # axis=0 删除行，1删除列
print(data.columns)

print("-------------------------------")


#数据标准化: 归一化Min-Max
#print(data.iloc[:,0:7])

#Scikit-Learn-Preprocessing-MinMax
matrix = data.iloc[:,1:7]
min_max_model = MinMaxScaler()
data_rescaled = min_max_model.fit_transform(matrix)
print(data_rescaled.round(2))

#特征数字化: one-hot编码
print(data.iloc[:,7:12])
one_hot_model = OneHotEncoder(sparse=False) #返回列表
one_hot_rescaled = one_hot_model.fit_transform(data.iloc[:,7:12])
print(one_hot_rescaled)

#数据合并
data = np.hstack((data_rescaled,one_hot_rescaled))
print(data.round(2))


#KMeans最佳K值 轮廓系数
score_array = []
max_score = -1
for n in range(2,6):
    kmeans_model = KMeans(n_clusters=n) #建模
    kmeans_temp = kmeans_model.fit_transform(data) #计算点到centroid距离
    kmeans_temp = kmeans_model.fit_predict(data) #计算点所属centroid
    #print(kmeans_temp)
    score = silhouette_score(data, kmeans_temp)
    if score > max_score:
        max_score = score
        best_k = n
    score_array.append([n,score]) #每一次的K值和对应轮廓系数
print(score_array)
print(best_k)





