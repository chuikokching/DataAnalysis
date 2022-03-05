import requests
import execjs
from base64 import b64encode
import hmac
import hashlib

app_secret_key = "bK9jk5dBEtjauy6gXL7vZCPJ1fOy076H"

nonce_func = execjs.compile("""
p = function(e) {
        var t = e || null;
        return null == t && (t = "xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx".replace(/[xy]/g, (function(e) {
            var t = 16 * Math.random() | 0;
            return ("x" === e ? t : 3 & t | 8).toString(16)
        }
        ))),
        t
    }
""")

print(nonce_func.call("p",))
nonce_str = nonce_func.call("p",)

#获取CSDN签名
def gen_signature(nonce_str, url):
    data = ""
    data += "GET\n"
    data += "application/json, text/plain, */*\n"
    data += "\n\n\n"
    data += "x-ca-key:203899271\n"
    data += f"x-ca-nonce:{nonce_str}\n"
    data += url
    appsecret = app_secret_key.encode('utf-8')  # 秘钥
    data = data.encode('utf-8')
    sign = b64encode(hmac.new(appsecret, data, digestmod=hashlib.sha256).digest()).decode()
    return sign


#格式要和浏览器的一样 注意空格问题 非常重要！！！ 会影响Base64等算法运行结果
template="""GET
application/json, text/plain, */*



x-ca-key:203899271
x-ca-nonce:a6844cb6-fcf8-43fd-8a52-8aa6baab11d1
/community-cloud/v1/homepage/community/by/tag?deviceType=PC&tagId=5"""

headers = {
    'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
    'x-ca-signature-headers': 'x-ca-key,x-ca-nonce',
    'x-ca-signature': gen_signature(nonce_str, "/community-cloud/v1/homepage/community/by/tag?deviceType=PC&tagId=5"),
    'x-ca-nonce': nonce_str,
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
    'Accept': "application/json, text/plain, */*",
    'x-ca-key': '203899271',
    'Origin': 'https://bbs.csdn.net',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
}


url = "https://bizapi.csdn.net/community-cloud/v1/homepage/community/by/tag?deviceType=PC&tagId=5"
rsp = requests.get(url, headers=headers)
print(rsp.status_code)
print(rsp.text)

print(gen_signature("a6844cb6-fcf8-43fd-8a52-8aa6baab11d1","/community-cloud/v1/homepage/community/by/tag?deviceType=PC&tagId=5"))
