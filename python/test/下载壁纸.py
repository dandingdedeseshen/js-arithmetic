import requests
from bs4 import BeautifulSoup
import os
import time


# 封装保存图片的函数
def downloadjpg(imgurl, localpath):
    # 这里传过来的图片地址是缩略图 需要转换为图片页面的地址之后在获取图片div
    r2 = requests.get(os.path.join('https://wallhaven.cc/w/',os.path.basename(imgurl)[:-4]))
    soup2 = BeautifulSoup(r2.text,'lxml')

    # 进入图片正确页面后再次获取到高清晰的图片的地址
    imag = soup2.find(id = 'wallpaper').get('src')
    response = requests.get(imag) # 获取图片的路径
    if response.status_code == 200:  # 图片所在页面请求正常
        # 保存图片
        with open(localpath,'wb') as f:
            f.write(response.content)

def getImg(url):
    time.sleep(0.5)
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')

    # 本地存储路径
    if not os.path.exists('..\imag'):
        os.makedirs('..\imag')
    lpath = os.path.abspath('..\imag')


    for j in soup.find(id='thumbs'):
        for i in j.find_all('img'):
            # 图片名称
            localpath = os.path.join(lpath,os.path.basename(i.get('data-src')))
            print('开始下载{}'.format(os.path.basename(i.get('data-src'))))
            downloadjpg(i.get('data-src'),localpath)

def main(url,start,end):
        # getImg(url)
    for i in range(start,end + 1):
        if i == 1:
            getImg(url)
        else:
            url2 = url + '?page={}'.format(i)
            getImg(url2)


start = int(input("开始页数"))
end = int(input("结束页数"))
main('https://wallhaven.cc/toplist',start,end)




