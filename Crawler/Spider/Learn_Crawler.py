import requests
import json


my_headers={
    "user-agent":"requests",
    "uid":"321"
}


url = "https://www.baidu.com"
res = requests.get(url)
print(res.encoding)
print(res.status_code)
print(res.headers)
# print(res.text)

requests.post(url, json=json.dumps())

res = requests.get(url, headers=my_headers)