import pandas as pd
from sklearn.preprocessing import MinMaxScaler

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

#计算，合并相关性 -> 避免聚类算法重复计算 夸大特征表现
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



