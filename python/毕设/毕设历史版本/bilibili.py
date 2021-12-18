import requests
import time
import pymysql
import random
from multiprocessing import Pool
from bs4 import BeautifulSoup

# 链接数据库
# conn = pymysql.connect(host = 'localhost' , port =3306 , user = 'root' , passwd = 'cdy1113' , db = 'bilibili')
# cur = conn.cursor()
# result = []
video_list = []
# 解析HTML地址
def getHtmlInfo(url):
    headers = {
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Host': 'api.bilibili.com',
        'Origin': 'https://www.bilibili.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko),'
                      'Chrome/80.0.3987.149 Safari/537.36'
    }
    # 请求数据
    try:
        response = requests.get(url, headers=headers, timeout=6).json()
        data = response['data']
        video = (
            data['bvid'], data['aid'], data['view'], data['danmaku'],
            data['reply'], data['favorite'], data['coin'], data['share'],
            data['like'])
        # video = ( bv号，aid,播放量，弹幕数，评论量，收藏，投币，分享，点赞 )
        video_list.append(video)
        print(video_list)
        save_db()
        time.sleep(0.4)
    except:
        print("----")
        time.sleep(0.4)

def save_db():
    print('11111111111111111111111111111111111111')
    conn = pymysql.connect(port = 3306,user = 'root' ,password = 'jhtxdy123' ,database = 'bili' ,charset = 'utf8')
    cur = conn.cursor()
    # 将数据保存至本地
    global video_list
    sql = "insert into bili_data values(%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    for row in video_list:
        try:
            cur.execute(sql, row)
        except:
            conn.rollback()
    conn.commit()
    # video_list = []
    

if __name__ == '__main__':
    pool = Pool()
    for i in range(1,2000):
        elem = (i-1)*10000
        urls = ['https://api.bilibili.com/x/web-interface/archive/stat?aid={}'.format(j) for j in range(elem,elem+10000)]
        pool.map(getHtmlInfo, urls)
        pool.close()
        pool.join()

    conn.close()
