import requests
from bs4 import BeautifulSoup
import os
from  PIL import Image
from io import BytesIO   #图片是二进制文件所以写入时要用二进制写入方法


# 封装保存图片的函数
def downloadjpg(imgurl, localpath):
    response = requests.get(imgurl,stream = True) # 获取图片的路径
    if response.status_code == 200:  # 图片所在页面请求正常
        with open(localpath,'wb') as f:
            f.write(response.content)

        # 百度到的图片保存方法
        # image = Image.open(BytesIO(response.content))
        # image.save(localpath)

def getImg(url):
    # 获取想要下载图片的连接地址
    response = requests.get(url)
    response.encoding = 'utf-8'         #声明解码方式是utf-8
    soup = BeautifulSoup(response.text, 'lxml')  # 将获取到的页面信息转换为beautifulSoup对象
    # 想要保存的目录.\代表程序文件所在目录
    path = os.path.abspath('.\imag')
    for i in soup.find_all('img'):   #因为img标签不止一个所以循环获取所有标签上的内容
        # if i.get('data-original'):
        #     localpath = os.path.join(path,os.path.basename(i.get('data-original')))
        #     print( '开始下载{}' .format(i.get('data-original')))
        #     downloadjpg( i.get('data-original'), localpath)
        # else:
            localpath = os.path.join(path,os.path.basename(i.get('src')))
            print('开始下载{}'.format(i.get('src')))
            downloadjpg(i.get('src'),localpath)


def main(url,num):
    getImg(url)
    # 翻页下载
    for i in range(2,num):
        a = '{}/index_{}.htm'.format(url,i)  #拼接字符串实现翻页之后网址的更改
        getImg(a)


main('https://wallhaven.cc/toplist',2)




