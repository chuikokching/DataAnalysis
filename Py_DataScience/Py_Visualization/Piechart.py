import Def as pdef
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
movie_stats = pdef.language_tj()
movie_stats = movie_stats.sort_values('tj', ascending=False)


# 绘制饼图
movie_stats = movie_stats.iloc[0:10]
labels = movie_stats.index
sizes = movie_stats['tj'].tolist()

print(movie_stats)

plt.pie(x=sizes, labels=labels, autopct='%1.1f%%', startangle=90)
plt.title(u'电影语种统计')
plt.legend(title="Languages",
           loc="center left",
           bbox_to_anchor=(1, 0, 0.5, 1))
plt.show()
