import pandas as pd
import numpy as np

# 显示所有列(参数设置为None代表显示所有行，也可以自行设置数字)
pd.set_option('display.max_columns', None)
# 显示所有行
pd.set_option('display.max_rows', None)


def movie_year_amount():
    # 读取数据
    data = pd.read_csv("movie.csv")
    # print(data)

    # 读取日期 release_date
    # print(data['release_date'])

    # 对于年份进行统计：1900-2000，1900 - 10，100
    # resample(时间间隔参数：年、季度、月、周）.count()/sum()/asfreq()
    data['release_date'] = pd.to_datetime(data['release_date'])
    # print(data['release_date'])
    data = data.set_index(data['release_date'])
    # print(data.head(5))
    data_year = data['release_date'].resample('Y').count()
    return pd.DataFrame(data_year)


def country_year_tj():
    data = pd.read_csv("movie.csv",
                       usecols=['title', 'country', 'language', 'release_date', 'average'])
    data = data[['title', 'country', 'language', 'release_date', 'average']]
    # 各国每年的电影产量
    data['country'] = data['country'].str.strip(' ')
    data['country'] = data['country'].fillna(value='')
    country_list = []
    for c in data['country']:
        c_list = c.split(' / ')
        for label in c_list:  # 123,2,3 -> 1,2,3
            country_list.append(label)
    country_list = list(set(country_list))
    country_list.remove('')
    #country_list.remove('美国/澳大利亚')
    #country_list.remove('捷克斯洛伐克/捷克')
    country_list.remove('中国大陆')  # 只统计中国
    country_list.remove('中国香港')
    #country_list.remove('中国台湾')
    data['release_date'] = pd.to_datetime(data['release_date'])
    data = data.set_index(data['release_date'])
    count = 0
    tj = pd.DataFrame(data['release_date'].resample('Y').count())
    tj = tj.drop(columns='release_date')
    for label in country_list:
        temp = data[data['country'].str.contains(label)]
        print("=====================================")
        print("标签=", label)
        print("总频数=", len(temp))
        count += len(temp)
        tj[label] = temp['release_date'].resample('Y').count()
    tj = tj.fillna(value=0)
    return tj


def language_tj():
    data = pd.read_csv("movie.csv",
                       usecols=['title', 'country', 'language', 'release_date', 'average'])
    data = data[['title', 'country', 'language', 'release_date', 'average']]
    # label统计 -> list
    data['language'] = data['language'].str.strip(' ')
    data['language'] = data['language'].fillna(value='')
    lang_list = []
    for l in data['language']:
        l_list = l.split(' / ')
        for label in l_list:  # 123,2,3 -> 1,2,3
            lang_list.append(label)
    lang_list = list(set(lang_list))
    lang_list.remove('')
    lang_list.remove('汉语普通话')
    # 统计每个类型标签对应的电影量/条数/频数
    data_lang_tj = pd.DataFrame(np.zeros([len(lang_list), 1]),
                                index=lang_list, columns=['tj'])  # 2列：标签，统计值tj
    for i in data['language']:
        for label in lang_list:
            if str(i).__contains__(label):
                data_lang_tj.loc[label, 'tj'] += 1
    # # 将小类汇总为大类，并添加至统计df
    # chinese_fy = data_lang_tj.loc['湖南话', 'tj'] + data_lang_tj.loc['北京话', 'tj']
    # # print(chinese_fy)
    # data_lang_tj.loc['中国方言', 'tj'] = chinese_fy
    return data_lang_tj

def averge_votes():
    return pd.read_csv("movie.csv", usecols=['average', 'votes', 'title'])