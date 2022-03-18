import pandas as pd
import numpy as np

"""
Pandas DataFrame基本操作
"""


def pd_basis():
    s = pd.Series(np.random.randn(5), index=list('abcde'))
    d = {'one': pd.Series([1., 2., 3.], index=['a', 'b', 'c']),
         'two': s,
         'three': 'go'}

    df = pd.DataFrame(d)
    print(df)
    print("========================")
    # 按行的索引输出
    print(df.iloc[2])
    print(df.loc['e'])
    # 按列的索引输出
    print(df['two'])
    print(df[['two', 'one']])
    # 按行列的索引输出
    print("========================")
    print(df['two'].loc['b'])
    print(df[['two', 'one']].loc['b'])
    # 模糊查询 大于0的所有数据
    print("========================")
    print(df[df['one'] > 0])
    print(df[(df['one'] > 0) & (df['two'] > 0)])
    # 精准查询
    print("========================")
    print(df[df['one'] == 1.0])
    print(df[(df['one'] == 1.0) & (df['two'] < 0)])


"""
Pandas 数据生成和读取操作
"""


def data_read_create():
    s1 = pd.Series(['楚门的世界', '泰坦尼克号', '霸王别姬', '你的名字', '楚门的世界', '泰坦尼克号', '霸王别姬', '你的名字'])
    s2 = pd.Series(['8.3', '9.5', '9.1', '8.7', '8.3', '9.5', '9.1', '8.7'])
    s3 = pd.Series(['672586', '1521451', '1538556', '1001049', '672586', '1521451', '1538556', '1001049'])
    s4 = pd.Series(['剧情', '爱情', '爱情', '动画', '剧情', '爱情', '爱情', '动画'])

    # 组成电影数据表
    df = pd.DataFrame(list(zip(s1, s2, s3, s4)), columns=['title', 'average', 'votes', 'genre'])
    print(df)

    df.to_csv("file_movie.csv")
    df.to_excel("file_movie.xlsx")
    # load CSV file
    test = pd.read_csv("file_movie.csv");

    # load Excel file
    test_xlsx = pd.read_excel("file_movie.xlsx");

    # load Txt file
    # test_txt=pd.read_csv('Test_Dataset.txt',delimiter='\t');

    print(test);
    print(test_xlsx);


"""
Pandas 查重,去重,缺失值,分列
"""

def data_operation():
    # 显示所有列(参数设置为None代表显示所有行，也可以自行设置数字)
    pd.set_option('display.max_columns', None)
    # 显示所有行
    pd.set_option('display.max_rows', None)
    # 设置数据的显示长度，默认为50
    pd.set_option('max_colwidth', 13)

    data = pd.read_csv("movie_info.csv", usecols=['average', 'genre', 'country', 'language', 'release_date', 'title', 'votes'])

    print(data)

    print("=================================")
    #查重
    replication1 = data.duplicated('average')

    print(replication1)

    print("=================================")
    #去重
    replication2 = data.drop_duplicates('average')

    print(replication2)
    print(len(replication1), "  ",len(replication2))

    #处理缺失值
    nan_df = pd.isna(replication2) #查看哪里缺失
    print(nan_df)
    replication2['average'] = replication2['average'].fillna(value=replication2['average'].mean().round(2)) #填充缺失值
    print(replication2['average'].mean())
    print(replication2)

    #分列
    print(replication2['release_date'].str.split('(',expand=True)[0])
    replication2['release_date'] = replication2['release_date'].str.split('(',expand=True)[0] #True表示拆分成独立的两列
    print(replication2)

"""
Pandas 数据运算 按年统计,时间聚合
"""

def data_stats_date():
    # 显示所有列(参数设置为None代表显示所有行，也可以自行设置数字)
    pd.set_option('display.max_columns', None)
    # 显示所有行
    pd.set_option('display.max_rows', None)
    data = pd.read_csv("movie_info.csv",usecols=['average', 'genre', 'country', 'language', 'release_date', 'title', 'votes'])
    data['release_date'] = data['release_date'].str.split('(', expand=True)[0]
    print(data['release_date'])

    data['release_date'] = pd.to_datetime(data['release_date'])
    #print(data['release_date'])

    data = data.set_index(data['release_date'])
    #print(data['release_date'])

    # 按年份聚合 需要将列转换为date时间格式
    print((data['release_date'].resample('Y').count()))
    print(pd.DataFrame(data['release_date'].resample('Y').count()).max())
    #print(data['release_date'].resample('M').count())


"""
Pandas 数据运算 Genre类型统计
"""

def data_stats_genre():
    # 显示所有列(参数设置为None代表显示所有行，也可以自行设置数字)
    pd.set_option('display.max_columns', None)
    # 显示所有行
    pd.set_option('display.max_rows', None)

    data = pd.read_csv("movie_info.csv",usecols=['average', 'genre', 'country', 'language', 'release_date', 'title', 'votes'])

    #print(data['genre'])

    #去除'[' ']'
    data['genre'] = data['genre'].str.strip('[')
    data['genre'] = data['genre'].str.strip(']')

    genre_list = []

    for g in data['genre']:
        g_list = g.split(", ")
        for tag in g_list:
            genre_list.append(tag)

    genre_list = list(set(genre_list))
    print(genre_list)

    # 统计每个类型标签对应的电影量/条数/频数
    data_genre_stats = pd.DataFrame(np.zeros([len(genre_list), 1]),
                                 index=genre_list, columns=['count'])  # 2列：标签，统计值count

    for g in data['genre']:
        for tag in genre_list:
            if(str(g).__contains__(tag)):
                data_genre_stats.loc[tag,'count'] += 1

    print(data_genre_stats)


"""
Pandas 数据运算 评分区间
"""

def data_stats_average():
    # 显示所有列(参数设置为None代表显示所有行，也可以自行设置数字)
    pd.set_option('display.max_columns', None)
    # 显示所有行
    pd.set_option('display.max_rows', None)

    data = pd.read_csv("movie_info.csv",usecols=['average', 'genre', 'country', 'language', 'release_date', 'title', 'votes'])

    data['average'].fillna(value=data['average'].mean().round(2))

    # 获取当前数据区间：最大值、最小值
    print(data['average'].describe())

    x = 7.1
    rate_list = []
    while x <= 9.7:
        rate_list.append(x)
        x += 0.1
        x = x.__round__(1)

    print(rate_list)

    # 构建二维表
    data_rate_count = pd.DataFrame(np.zeros([len(rate_list), 1]),
                                index=rate_list, columns=['count'])

    for g in data['average']:
        for tag in rate_list:
            if(g == tag):
                data_rate_count.loc[tag,'count'] += 1
                continue

    print(data_rate_count)


"""
Pandas 数据筛选和排序
"""

def data_stats_find_and_sort():
    # 显示所有列(参数设置为None代表显示所有行，也可以自行设置数字)
    pd.set_option('display.max_columns', None)
    # 显示所有行
    pd.set_option('display.max_rows', None)
    # 设置数据的显示长度，默认为50
    pd.set_option('max_colwidth', 10)

    data = pd.read_csv("movie_info.csv",usecols=['average', 'genre', 'country', 'language', 'release_date', 'title', 'votes'])

    # 排序
    print(data.sort_values('average',ascending=False))
    print(data[['average','votes']].sort_values(['average','votes'], ascending=False)) #分数相同则按照votes来排序

    # 筛选
    print(data.iloc[1:20]) # 1-20行数据
    print(data.loc[data['average'] > 9.0])  # 条件筛选要用loc()
    print(data.loc[(data['average'] > 9.0) & (data['average'] < 9.5), ['title','average']])

if __name__ == '__main__':
    # pd_basis()
    # data_read_create()
    # data_operation()
    # data_stats_date()
    # data_stats_genre()
    #data_stats_average()
    data_stats_find_and_sort()
