import re


info = "姓名:CKC2000 生日:1994-03-03 本科:2022-03-03"

#match()從字符串的最開始処匹配
result = re.match(".*生日.*?(\d{4}[-]\d{2}).*本科.*?(\d{4}[-]\d{2})", info)

print(result.group(1))
print(result.group(2))

result = re.sub("\d{4}","2020",info)
print(info)
print(result)


result = re.search(".*生日.*?(\d{4}[-]\d{2}).*本科.*?(\d{4}[-]\d{2})", info)
print(result.group(1))
print(result.group(2))

#有回车换行符建议用search(), 或者 re.match("ckc", name,re.DOTALL).group()
name = "my name is CKC"
print(re.search("ckc", name,re.IGNORECASE).group())

name1 = """ my name is
CKC
"""
print(re.match(".*(CKC)", name1,re.DOTALL).group(1))


