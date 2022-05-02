import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# 1. 数据展示：了解数据.
years = np.arange(2009, 2020)
sales = np.array([0.52, 9.36, 33.6, 132, 352, 571, 912, 1207, 1682, 2135, 2684])
print(years)
print(sales)

plt.scatter(years, sales,c='red')
plt.show()

# 2. 初步判断：多项式回归(3阶)
'''
y = a*x^3 + b*x^2 + c*x + d
1: 1 1 1
2: 8 4 2
3: 27 9 3
...
'''

model_y = sales
model_x = (years - 2008).reshape(-1,1)
print(model_x)
model_x = np.concatenate([model_x **3,model_x **2,model_x **1],axis=1)
print(model_x)

# 3. 训练模型
model = LinearRegression()
model.fit(model_x,model_y)

print('coef:',model.coef_)
print('intercept:',model.intercept_)

# 4. 添加趋势线：想象成画折线图
trend_x = np.linspace(1, 12, 100) #1-12 之间生成100个点
fun = lambda x: -0.20964258 * x ** 3 + 34.42433566 * x ** 2 + -117.85390054 * x + 90.12060606060629
trend_y = fun(trend_x)

print(trend_x)
print(trend_y)

print('2020年销售额预测：', fun(12))
years_no = years - 2008
plt.scatter(years_no, sales, c='red') #画点
plt.scatter(12, fun(12), c='blue')  #画点
plt.plot(trend_x, trend_y, c='green') #画线


# 5.数据标签
plt.annotate(round(fun(12),1),xy=(12,fun(12)),xytext=(12 + 0.5, fun(12) - 0.5))
for i in range(11):
    plt.annotate(sales[i], xy=(years_no[i], sales[i]),xytext=(years_no[i] + 0.5, sales[i] - 0.5))
plt.show()

