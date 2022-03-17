import requests
from scrapy import Selector
from signature import Signature
import re
import json
from urllib.parse import urlparse, parse_qs

def get_last_urls():
    urls=[]
    #获取最终抓取的所有的二级分类url
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"
    }
    resp = requests.get("https://bbs.csdn.net/", headers=headers)
    if resp.status_code != 200:
        raise Exception("爬取失败, 被反爬了!!！ 再想想办法~")
    sel = Selector(text=resp.text)
    c_nodes = sel.css("div.el-tree-node .custom-tree-node")
    for index , c_nodes in enumerate(c_nodes):
        url = f"https://bizapi.csdn.net/community-cloud/v1/homepage/community/by/tag?deviceType=PC&tagId={index+1}"
        sign = Signature()
        code , resp_json = sign.get_html(url)
        if code != 200:
            raise Exception("被反爬了!!！")
        if "data" in resp_json:
            for item in resp_json["data"]:
                url = "{}?category={}".format(item["url"],item["id"])
                urls.append(url)
        break
    return urls

def extract_topic(data_list):



def parse_list(url):
    next_page = 1
    tabid = 0
    total_pages = 0
    page_size = 15
    o = urlparse(url)
    query_dict = parse_qs(o.query) #变成字典
    cate_id = query_dict["category"][0]

    category_rsp = requests.get(url)
    if category_rsp.status_code != 200:
        raise Exception("被反爬了!!！")
    data = re.search("window.__INITIAL_STATE__=(.*});</script>", category_rsp.text, re.IGNORECASE)
    if data:
        data = data.group(1)
        data = json.loads(data)
        total = data["pageData"]["data"]["baseInfo"]["page"]["total"]
        tabid = data["pageData"]["data"]["baseInfo"]["page"]["defaultActiveTab"]

        total_pages = total / page_size
        if total % page_size > 0:
            total_pages += 1

        extract_topic(data["pageData"]["data"]["baseInfo"]["dataList"])
        next_page += 1

        #下一页
        while next_page < total_pages:
            # 注意这里的参数顺序，一定要按照ascii编码排序！！！！！
            #https: // bizapi.csdn.net/community - cloud/v1/ community/listV2?page = 3 & pageSize = 20 & tabId = 1368 & noMore = false & communityId = 209 & type = 1 & viewType = 0
            url = f"https://bizapi.csdn.net/community-cloud/v1/community/listV2?communityId={cate_id}&noMore=false&page={next_page}&pageSize={page_size}&tabId={tabid}&type=1&viewType=0"
            signer = Signature()
            code , resp_json = signer.get_html(url)
            if code != 200:
                raise Exception("被反爬了!!！")

            #next_page +=1


if __name__ == '__main__':
    urls = get_last_urls()
    for url in urls:
        parse_list(url)
