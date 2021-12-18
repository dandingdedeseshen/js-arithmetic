import requests
import json
import time


class Spider():
    def __init__(self):
        pass


    # 获取数据
    def get_url(self,url):
        #设置延时操作防止频繁操作被封ip
        time.sleep(0.5)
        # 伪装为浏览器的请求头
        head = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
        }
        respond_json = requests.get(url,headers = head )
        respond_dict = json.loads(respond_json.text)
        return respond_dict


        
if __name__ == '__main__':
    a = Spider()
    a.get_url('https://api.bilibili.com/x/space/arc/search?mid=16794231&ps=1&tid=0&pn=30&keyword=&order=pubdate&jsonp=jsonp')





