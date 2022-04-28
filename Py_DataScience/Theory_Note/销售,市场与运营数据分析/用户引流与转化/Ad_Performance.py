import matplotlib.pyplot as plt
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
    # kmeans_temp = kmeans_model.fit_transform(data) #计算点到centroid距离
    kmeans_temp = kmeans_model.fit_predict(data) #计算点所属centroid
    #print(kmeans_temp)
    score = silhouette_score(data, kmeans_temp) #平均轮廓计算
    if score > max_score:
        max_score = score
        best_k = n
        best_label = kmeans_temp
    score_array.append([n,score]) #每一次的K值和对应轮廓系数
print(score_array)
print(best_k)


#聚类分析结果
#1.合并数据与聚类标签
data = pd.read_csv("ad_performance.csv",index_col=0)
temp = pd.DataFrame(best_label,columns=['clusters'])
merge_data = pd.concat((data,temp),axis=1) #纵向合并
print(merge_data.head(5))

#2.各聚类下的样本量
cluster_counts = pd.DataFrame(merge_data['渠道代号'].groupby(merge_data['clusters']).count()).T.rename({'渠道代号':'counts'})
print(cluster_counts)

#3.各聚类下的样本量占比
cluster_percents = (cluster_counts/len(data)).round(3).rename({'counts':'percentage'})
print(cluster_percents)

features = []
#4.数值类特征的均值
for label in range(best_k):
    label_data = merge_data[merge_data['clusters'] == label]
    p1_data = label_data.iloc[:,1:7] #筛选出数值类特征
    p1_des = p1_data.describe().round(3) #获取描述性统计信息
    p1_mean = p1_des.iloc[1,:] #获取均值数据

    print(p1_mean)

    # 5.字符类特征众数
    p2_data = label_data.iloc[:,8:12]
    p2_des = p2_data.describe()
    p2_mode = p2_des.iloc[2,:]
    print(p2_des)
    print(p2_mode)

    merge_line = pd.concat((p1_mean, p2_mode), axis=0)
    features.append(merge_line)

#6. 数据合拼与展示
print('===============================')
print(pd.DataFrame(features).T)
cluster_pd = pd.DataFrame(features).T
all_cluster = pd.concat((cluster_counts,cluster_percents,cluster_pd),axis=0)
print(all_cluster)

#7. 可视化
# 1.获取数值特征均值, 标准化, Min-Max归一化

nums_data = cluster_pd.iloc[:6,:].T.astype(np.float64) # 获取数据并转换为float
nums_min_max = min_max_model.fit_transform(nums_data) # 获取标准化 (归一化)
print(nums_min_max.round(4))

# 2.绘制画布, 准备数据，x,y,类别颜色
fig = plt.figure() #创建一个画布
ax = fig.add_subplot(111,polar=True) #创建子网格：正中央
angles = np.linspace(0,2*np.pi,6,endpoint=False) #计算角度
angles = np.concatenate((angles,[angles[0]])) #点连接起来 6个点 需要7画 完成X轴设置
# print(len(angles))
# print(angles)


# 3.绘制点线图
# y轴的设置：0 1 2 3
colors = ['b', 'y', 'r', 'g']
labels = p1_data.columns.tolist()
for i in range(len(nums_min_max)):
    temp_list = nums_min_max[i]  # 获得对应簇数值特征数据
    temp = np.concatenate((temp_list, [temp_list[0]]))  # 完成闭合
    ax.plot(angles, temp, 'o-', color=colors[i], label=i)

# 4.Legend,Presentation
#ax.set_thetagrids(angles * 180 / np.pi, labels)  # 设置极坐标
ax.set_rlim(-0.2, 1.2)  # 设置半径刻度
plt.title("Value Comparison")  # 设置标题
plt.legend()  # 类说明标签
plt.show()