import pandas as pd
import numpy as np

def load_data():
    # 显示所有列(参数设置为None代表显示所有行，也可以自行设置数字)
    pd.set_option('display.max_columns', None)
    # 显示所有行
    pd.set_option('display.max_rows', None)
    # 设置数据的显示长度，默认为50
    pd.set_option('max_colwidth', 13)

    # df_empty = []
    # data = pd.read_excel("Test_Dataset_Excel_1.xlsx")

    # 显示
    # print(data[['ID','Name','Det.']])
    # print(data.iloc[1:4])

    #查询筛选
    # print(data.loc[data['Name']=='ckc'])
    # print(len(data.loc[data['Name']=='ckc']))

    #新增列
    # data['Total']= data['HP']*2
    # print(data)

    #删除列
    # data = data.drop(columns= ['Total'])
    # print(data)

    print("===================================")

    # concat()合并多个Excel文件
    # for f in ('Test_Dataset_Excel_1.xlsx','Test_Dataset_Excel_2.xlsx','Test_Dataset_Excel_3.xlsx'):
    #     df_empty.append(pd.read_excel(f))

    # ignore_index=True,索引累加
    # df = pd.concat(df_empty,ignore_index=True)
    # print(df)

    # 删除列和行
    # df = df.drop(columns=['ID'])
    # print(df)
    # df = df[~(df['Name'].isin(['Klee']) | df['Name'].isin(['chuikokching']))]
    # print(len(df))

    #df.to_excel('Result.xlsx',index=True)

    data = pd.read_excel("Excel1.xlsx")
    df = pd.read_excel("Excel3.xlsx")
    # print(data)

    # 分组Groupby
    #print(df.groupby('Det.')['Det.'].count().sort_values(ascending=True).reset_index(name = 'count'))
    #print(df.groupby(['Name','Det.'])['Det.'].count().sort_values(ascending=True).reset_index(name='count'))

    # 双表连接join
    df = df.join(data.set_index('Det.'),on = 'Det.',how='inner')
    print(df[['Name','Det.','Department']])


if __name__ == '__main__':
    load_data()