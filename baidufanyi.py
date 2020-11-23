# -*- codeing = utf-8 -*-
# @Time ; 2020/11/2213:27
import requests
if __name__ == "__main__":

    post_url = "https://fanyi.baidu.com/v2transapi"
    url_1 = {}
    x=input("输入要翻译的内容：\n>>>")
    date = {"query":"x","from":"en","to":"zh"}
    ua = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36 Edg/87.0.664.41"}

    html = requests.post(post_url,data = date,headers = ua)

    html_json = html.json()
    print(html_json)
