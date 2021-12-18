from flask import Flask,request,redirect,render_template,url_for
from bilibilidata import main
import json
from sql import Sql
from spider import Spider

app = Flask(__name__)

# 全局保存id以便跨页面获取id
aid = 0

@app.route('/(.*?)')
def fun():
    return redirect(url_for('/index/'))

#首页
@app.route('/index/')
def index():
    return render_template('index.html')


#搜索后进入的展示搜索结果的页面
@app.route('/data/' ,methods=['POST','GET'])
def data():
    # post请求
    if request.method == 'POST':
        # 使用全局变量aid
        global aid
        aid = request.form['aid']
        num = request.form['num']
        data = main(aid,num)
        if data == 'not found':
           return render_template('notFound.html')
        up_data = get_uper()
        return render_template('data.html',data = data,up_data = up_data)
        
    if request.method == 'GET':
        return render_template('notFound.html')

# 视频信息统计图页面
@app.route('/chart/',)
def chart():
    global aid
    data = Sql.select(1,aid)
    data_json = json.dumps(data)
    return render_template('chart.html',data_json = data_json)

def get_uper():
    global aid
    url = 'https://api.bilibili.com/x/space/arc/search?mid={}&ps={}&tid=0&pn={}&keyword=&order=pubdate&jsonp=jsonp'
    #  mid：用户id   ps：一页显示的内容   tid：不太清楚 pn：页数
    return Spider.get_url(1,url.format(aid,30 , 1))['data']   

if __name__ == '__main__':
    app.run(host= '0.0.0.0',port = 8000 ,debug = True)