import pandas as pd

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