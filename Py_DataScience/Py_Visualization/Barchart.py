import Def as pdef
import matplotlib.pyplot as plt
import re

movie_stats = pdef.movie_year_amount()
print(movie_stats.index)
# print(re.search("(\d{4})",str(movie_stats.release_date.index[7])).group(1))

movie_stats['year'] = movie_stats.index
# print(movie_stats['year'].dt.year)
years = movie_stats['year'].dt.year
# years=[]
# for i in range(len(movie_stats.index)):
#     years.append(re.search("(\d{4})",str(movie_stats.release_date.index[i])).group(1))

amounts = movie_stats.release_date.tolist()

# 绘制直方图
width = 0.35  # the width of the bars: can also be len(x) sequence
fig, ax = plt.subplots()

ax.bar(years, amounts, width,label='Movie')

ax.set_ylabel('Amount')
# ax.set_xlabel('年份')
ax.set_title('Annual production of films')
ax.legend()

plt.show()
