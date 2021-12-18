from spider import Spider
from sql import Sql 

class Bili_anlyze(Spider):
    def __init__(self,mid = 40430723,num = 3):
        # up主id
        self.mid = mid
        # 想要获取到的视频数量
        self.num = num
        # 存储up主的视频编号,以及评论数
        self.dict = {}


    #获取up主的视频av号返回到一个字典中
    def get_video(self, tid , num):

        # B站的用户空间页面为通过js动态获取数据的页面，需要爬取接口数据才能获取到用户的视频数据
        url = 'https://api.bilibili.com/x/space/arc/search?mid={}&ps={}&tid={}&pn={}&keyword=&order=pubdate&jsonp=jsonp'

        #翻页获取数据
        for pn in range(0,num // 30 + 1):
            #最后一页时获取不足一页条数的数据
            pn += 1
            print('爬取第{}页数据'.format(pn))
            ps = num % 30 if pn == num // 30 + 1 else 30   #当最后一页时（pn）ps取0或者是剩下不足一页的条数
            if ps == 0:     #当页数为0没有多余的页数直接退出循环
                break
            data = self.get_url(url.format(self.mid , ps , tid , pn))
            vlist = data['data']['list']['vlist']
            for j in vlist:
                #以视频id为键 包含视频评论数和视频名称的列表为值
                self.dict[j['aid']] = [j['title'],j['comment'],j['mid']]

    # 获取视频数据
    def get_data(self):
        timer = ''
        # 视频详情接口地址
        url = 'https://api.bilibili.com/x/web-interface/archive/stat?aid={}'
        for i in self.dict:
            print('正在获取av号为{}的视频信息'.format(i))
            data = self.get_url(url.format(i))
            #分别将视频的播放数，弹幕数 ，点赞数，收藏数，硬币,获取时间数存入字典
            self.dict[i][3:] = [timer,data['data']['view'],data['data']['danmaku'],data['data']['like'],data['data']['favorite'],data['data']['coin']]

    # 获取up主的视频分类
    def get_class(self):
        url = 'https://api.bilibili.com/x/space/arc/search?mid={}&ps={}&tid=0&pn={}&keyword=&order=pubdate&jsonp=jsonp'
        #  mid：用户id   ps：一页显示的内容   tid：不太清楚 pn：页数
        return Spider.get_url(1,url.format(self.mid,30 , 1))['data']['list']['tlist']

    #将数据存入数据库
    def save_data(self):
        url = 'https://api.bilibili.com/x/space/arc/search?mid={}&ps={}&tid={}&pn={}&keyword=&order=pubdate&jsonp=jsonp'
        #  mid：用户id   ps：一页显示的内容   tid：视频分类 pn：页数
        video_count = self.get_url(url.format(self.mid, 30, 0, 1))['data']['page']['count']  # 该up主的视频总数

        if self.num > video_count:
            print('爬取视频数量超过了up主的上传数量！将默认爬取up主的所有视频')
            self.num = video_count

        num = self.num

        data = self.get_class()
        for i in data:
            if num > data[i]['count']:
                self.get_video(i,data[i]['count'])
                self.get_data()
                str = data[i]['name']
                # 处理一下字典，将数据存入数据库
                # list = [(data[i][2],i, data[i][0], data[i][1], data[i][3], data[i][4], data[i][5], data[i][6],data[i][7]) for i in data]
                list = [(i, self.dict[i][0], self.dict[i][1],self.dict[i][2] , self.dict[i][4], self.dict[i][5], self.dict[i][6], self.dict[i][7],self.dict[i][8],str) for i in self.dict]
                self.dict = {}
                Sql.save_data(self,'video',list)
                num -= data[i]['count']
            else:
                self.get_video(i, num)
                self.get_data()
                str = data[i]['name']
                # 处理一下字典，将数据存入数据库
                list = [(i, self.dict[i][0], self.dict[i][1],self.dict[i][2] , self.dict[i][4], self.dict[i][5], self.dict[i][6], self.dict[i][7],self.dict[i][8],str) for i in self.dict]
                self.dict = {}
                Sql.save_data(self,'video',list)
                break



def main(aid,num):
    try :
        aid1 = int(aid)
        num1 = int(num)
    except:
        print('Error : 请输入数字！！')
    a = Bili_anlyze(aid1,num1)
    a.save_data()

if __name__ == '__main__':
    main(16794231,5)



