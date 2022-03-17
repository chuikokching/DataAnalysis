#提取html值
from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Chuikokching's story</b></p>
<div id="wrap"><p class="story">Once upon a time there were three little sisters</p><p class="2">2</p><p class="3">3</p>
<div id="post-12345">genshin impact 12345 <p class="four">4</p><p class="5">5</p></div>
</div>

<div id="ckc">genshin impact ckc</div>
<p class="story">chuikokching</p>
</body>
"""

bs = BeautifulSoup(html_doc,"html.parser")
title_tag = bs.title
paragraph_tag = bs.p
# print(paragraph_tag.string)
# print(title_tag.string)


p_tags = bs.findAll("p")
print("{} {}".format(p_tags,len(p_tags)))
for p in p_tags:
    print(p.string)

div_tags = bs.findAll("div")
print("{} : {}".format(div_tags,len(div_tags)))
for div in div_tags:
    print(div.string)

import re
div_tags = bs.find("div", id="ckc")
print("{}".format(div_tags.string))

div_tags = bs.find("div", id=re.compile("post-\d*")) #动态ID
print(div_tags.string)

div_tags = bs.find(string = "chuikokching")
pass
print(div_tags.string)

print("")

div_tags = bs.find("div",id="wrap")
kinder = div_tags.descendants #获取子元素的子元素
kinder = div_tags.contents #获取子元素

for kind in kinder:
    print("{}".format(kind)) #kind.name, kind.string

parent = bs.find("p",{"class":"story"}).parent #获取父元素 or parents
print(parent)

sibling = bs.find("p",{"class":"story"}).next_sibling #获取兄弟元素 or siblings or previous_siblings
print(sibling["class"])
# for s in sibling:
#     print(s["class"]) # s.get("class")

print("------------------Xpath-----------------")

from scrapy import Selector

sel = Selector(text=html_doc)
#同一个元素拥有多种xpath语法
tag_texts = sel.xpath("//div[@id='wrap']/div/p/text()").extract() #返回list
if tag_texts:
    for i in tag_texts:
        print(i," P ")

#能封装到数据库中 方便部署
name_xpath = "//div[@id='wrap']/div/text()"
name = ""

tag = sel.xpath(name_xpath).extract()
if tag:
    name = tag[0]
print(name)

#针对多个class的选择情况可使用contains根据单个来查找
sel.xpath("//div[contains(@class,'info')]/p")
sel.xpath("//div[@class='info big']/p[last()]").extract()
sel.xpath("//p[@class='age']|//p[@class='name']") #同时获取两个tag


print("------------------CSS-----------------")

#CSS选择器
sel = Selector(text=html_doc)
tag = sel.css("#wrap p ::text").extract() #.four::text
print(tag)
