import Def as pdef
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']

movie_stats = pdef.country_year_tj()
print(movie_stats)

movie_stats.plot()
plt.legend(ncol=4)
plt.title('各国电影年产量')
plt.xlabel('年份')
plt.ylabel('数量')
plt.show()

