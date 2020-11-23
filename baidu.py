# -*- codeing = utf-8 -*-
# @Time ; 2020/11/2213:25
import requests
import json
if __name__ == "__main__":
    #网址
    url = "https://www.baidu.com/s?"
    #浏览器标识
    ua = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36 Edg/87.0.664.41"}
    x = input("输入您要查询的内容\n>>>")
    #搜索参数
    url_1 = {"wd" : x}
    #将获得的数据赋值
    html = requests.get(url=url,params=url_1,headers = ua)
    #以文本格式输出
    html_text = html.text
    print("html_text")
    nex_name = x+".html"
    with open(nex_name,"w",encoding = "utf-8") as fp:
        fp.write(html_text)
        print(html_text,"保存成功")
