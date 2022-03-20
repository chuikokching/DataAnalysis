import Def as pdef
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']


movie_stats = pdef.averge_votes()
print(movie_stats)


# 绘制图表
plt.scatter(x=movie_stats['average'], y=movie_stats['votes'],marker='*')
title = len(movie_stats).__str__() + " 部电影评分分值与人数"
plt.title(title)
plt.xlabel('评分分值')
plt.ylabel('评价人数')
plt.grid()
plt.show()

# 筛选、排序 -> 结合图表，观察数据
print("====================高分热门电影====================")
print(movie_stats.sort_values(['votes', 'average'], ascending=False).head(10))