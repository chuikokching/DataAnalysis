import execjs
import requests
from base64 import b64encode
import hmac
import hashlib
from urllib.parse import urlparse

class Signature():
    def __init__(self):
        self.nonce_func = execjs.compile("""
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

    def get_path(self, url ):
        parse_result = urlparse(url)
        path = f"{parse_result.path}?{parse_result.query}"
        return path

    def gen_signature(self,url, accept, nonce_string, cakey, secretkey):
        url_path = self.get_path(url)
        data = ""
        data += "GET\n"
        data += f"{accept}\n"
        data += "\n\n\n"
        data += f"x-ca-key:{cakey}\n"
        data += f"x-ca-nonce:{nonce_string}\n"
        data += url_path
        appsecret = secretkey.encode('utf-8')  # 秘钥
        data = data.encode('utf-8')
        sign = b64encode(hmac.new(appsecret, data, digestmod=hashlib.sha256).digest()).decode()
        return sign

    def get_html(self, url):
        nonce_str = self.nonce_func.call("p",)
        accept = "application/json, text/plain, */*"
        cakey = "203899271"
        app_secret = "bK9jk5dBEtjauy6gXL7vZCPJ1fOy076H"
        headers = {
            'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
            'x-ca-signature-headers': 'x-ca-key,x-ca-nonce',
            'x-ca-signature': self.gen_signature(url, accept, nonce_str, cakey, app_secret),
            'x-ca-nonce': nonce_str,
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Accept': accept,
            'x-ca-key': cakey,
            'Origin': 'https://bbs.csdn.net',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
        }
        rsp = requests.get(url, headers=headers)
        return rsp.status_code , rsp.json()

#格式要和浏览器的一样 注意空格问题 非常重要！！！ 会影响Base64等算法运行结果
template="""GET
application/json, text/plain, */*



x-ca-key:203899271
x-ca-nonce:a6844cb6-fcf8-43fd-8a52-8aa6baab11d1
/community-cloud/v1/homepage/community/by/tag?deviceType=PC&tagId=5"""

if __name__ == '__main__':
    signer = Signature()
    code , data = signer.get_html("https://bizapi.csdn.net/community-cloud/v1/homepage/community/by/tag?deviceType=PC&tagId=5")
    print(code)
    print(data)