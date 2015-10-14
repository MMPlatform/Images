#-*- coding:utf-8 -*-
#!/usr/bin/env python
import web
import requests
import sys
from sys import argv
from bs4 import BeautifulSoup

reload(sys)
sys.setdefaultencoding("utf-8")

urls = (
        '/index/(.*)', 'index'
)

class index:
        def GET(self,name):
                url = name
                url1 = 'http://stu.baidu.com/n/pc_search?rn=10&appid=0&tag=1&isMobile=0&queryImageUrl=http://'+url+'&querySign=&fromProduct=&productBackUrl=&fm=&uptype=plug_in'
                result = ""
                headers = { "Accept":"text/html,application/xhtml+xml,application/xml;",
            "Accept-Encoding":"gzip",
            "Accept-Language":"zh-CN,zh;q=0.8",
            "Referer":"http://www.example.com/",
            "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36"
                }
                res2 = requests.get(url1, headers=headers)
                html_doc = res2.text
                soup = BeautifulSoup(html_doc, 'html.parser')
                for each_div in soup.find_all('a', class_="guess-info-word-link"):
                        result += each_div.get_text()
                        result += " "
                return  result.decode('UTF-8').encode('GBK');



if __name__ == "__main__":
        print sys.getdefaultencoding()
        app = web.application(urls, locals())
        app.run()
