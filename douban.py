# -*- codeing = utf-8 -*-
# @Time ; 2020/11/2214:07
import json
import requests
if __name__ == "__main__":
    url = "https://movie.douban.com/j/search_subjects"
    parm = {'type':'movie',
        'tag':'热门',
        'sort':'recommend',
        'page_limit':'60',# 一次出多少信息
        'page_start':'0',} # 从第几个开始获取
    ua = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36 Edg/87.0.664.41"}
    html = requests.get(url,params = parm,headers = ua)
    list_data = html.json()
    with open('douban.json',"w",encoding="utf-8") as fp:
        json.dump(list_data,fp = fp,ensure_ascii = False)
        print("完成")