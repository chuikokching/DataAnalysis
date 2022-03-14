import requests
import json
from scrapy import Selector
from bs4 import BeautifulSoup
import pandas as pd
import openpyxl

"""
豆瓣电影Rating
"""


all_movie = []

my_headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36",
}


def get_movie_infos(url):
    movie_dict = {}
    url_movie = url
    res = requests.get(url_movie, headers=my_headers)
    if res.status_code != 200:
        raise Exception("我们被反爬了,想想办法~~")
    # print(res.headers)
    # print(res.text)

    sel = Selector(text=res.text)
    bs = BeautifulSoup(res.text, "html.parser")

    try:
        title = sel.xpath("//*[@id='content']/h1/span[1]/text()").extract()
        movie_dict['title'] = title[0]

        director = sel.xpath("//*[@id='info']//a[@rel='v:directedBy']/text()").extract()[0]
        movie_dict['director'] = director

        # actor = sel.xpath("//*[@id='info']//a[@rel='v:starring']/text()").extract()
        # movie_dict['actor'] = actor

        genre = sel.xpath("//*[@id='info']//span[@property='v:genre']/text()").extract()
        movie_dict['genre'] = genre

        language = bs.find(text="语言:").next_element
        movie_dict['language'] = language

        releaseDate = sel.xpath("//*[@id='info']//span[@property='v:initialReleaseDate']/text()").extract()
        movie_dict['releaseDate'] = releaseDate

        rate = sel.xpath("//*[@id='interest_sectl']//strong[@property='v:average']/text()").extract()
        movie_dict['rate'] = rate[0]

        rating_people = sel.xpath("//*[@id='interest_sectl']//span[@property='v:votes']/text()").extract()
        movie_dict['rating_people'] = rating_people[0]
        # print(movie_dict)
        all_movie.append(movie_dict)
        movie_dict={}
        # for key in movie_dict:
        #     print(key, ":", movie_dict.get(key))
    except AttributeError:
        print("电影已下架或不存在某个字段~~~")


def get_all_movie_url_of_250():
    page = 0;
    max_page = 25;
    while page <= max_page:
        url_movie = "https://movie.douban.com/top250?start=" + page.__str__() + "&filter="
        res = requests.get(url_movie, headers=my_headers)
        if res.status_code != 200:
            raise Exception("我们被反爬了,想想办法~~")

        sel = Selector(text=res.text)
        # bs = BeautifulSoup(res.text, "html.parser")

        li_tag = sel.xpath("//ol[@class='grid_view']//li//div[@class='pic']//a/@href").extract()
        # li_tag = sel.xpath("//ol[@class='grid_view']//li//div[@class='pic']//a//img/@alt | //ol[@class='grid_view']//li//div[@class='pic']//a/@href").extract()

        for url in li_tag:
            get_movie_infos(url)

        # exit()
        page += 25


if __name__ == '__main__':
    get_all_movie_url_of_250()

    print(all_movie)

    data = pd.DataFrame(all_movie) #转为二维表
    data.to_excel("电影Top250.xlsx")

    # get_movie_infos("https://movie.douban.com/subject/1292052/")

# requests.post(url, json=json.dumps())

# res = requests.get(url, headers=my_headers)
