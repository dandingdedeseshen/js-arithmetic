from flask import Flask,request,redirect,render_template,url_for,jsonify
from bilibilidata import main,Bili_anlyze
import json
from sql import Sql
from spider import Spider
import time


app = Flask(__name__)

# 全局保存id以便跨页面获取id
aid = 0
# 全局保存登录的用户账号
user = ''
# 全局保存爬取数量
num = 0

# 首页登录
@app.route('/', methods = ['POST','GET'])
def fun():
    # 注册之后的跳转需要接受数据
    if request.method == 'POST':
        try:
            userId = request.form['userId']
            userPassWord = request.form['userPassWord']
            Sql.insert(1,("user","userid","password",userId,userPassWord))
            registerState = 'success'
            return render_template('login.html',registerState = registerState)
        except:
            registerState = 'fail'
            return render_template('login.html',registerState = registerState)
    # 首次登录不接受数据
    else:
            return render_template('login.html')

    

#搜索首页
@app.route('/index/', methods = ['POST','GET'])
def index():
    if request.method == 'POST':
        userId = request.form['userId']
        userPassWord = request.form['userPassWord']
        try:
            if (userPassWord == Sql.select(1,'password','user','userid',userId)[0]['password']):
                global user 
                user = userId
                return render_template('index.html')
            else:
                loginState = 'fail'
                return render_template('login.html',loginState = loginState)
        except:
            loginState = 'fail'
            return render_template('login.html',loginState = loginState)
    else:
        loginState = 'skip'
        return render_template('index.html',loginState = loginState)


#搜索后进入的展示搜索结果的页面
@app.route('/data/' ,methods=['POST','GET'])
def data():
    # post请求
    if request.method == 'POST':
        # 地址是否带参数影响到数据的获取使用状态区分一下地址是否带参数
        state = 'no'

        # 使用全局变量aid
        global aid,user,num
        aid = request.form['aid']
        num = request.form['num']
        # 获取数据的时间 可以放到循环中将获取时间精确到秒
        timer = time.strftime("%Y-%m-%d", time.localtime())
        
        # 保存用户搜索记录
        if user != '':
            Sql.insert(1, ("history", "mid", "userid",'num','time', aid, user,num))
        
        # 爬取数据
        main(aid,num)

        # up主视频分类
        up_data = Bili_anlyze(aid,num).get_class()
        data = insert_data(aid,num)
        return render_template('data.html',data = data,up_data = up_data,state = state)
    else:
        return render_template('notFound.html')

@app.route('/data/<str>' ,methods=['POST','GET'])
def data1(str):
    state = str
    
    global aid,num
    if len(str)< 20:
        str1 = "'" + str[0:-8] + "'"
        str2 = str[-8:]
        data = Sql.select2(1,'*','video',str1,'class_name',str2,'mid')
        # data = Sql.select(1,'*','video',str1,'class_name')        
    else:
        aid = str[0:-19]
        time = '"' + str[-19:-4] +'%'+'"'
        str = 'SELECT * FROM `video` where mid = {} AND timer like {}'
        data = Sql.special_sql(1,str,aid,time)
    up_data = Bili_anlyze(aid,num).get_class()
    return render_template('data.html',data = data,up_data = up_data,state = state,aid = aid)



@app.route('/history/')
def history():
    global user
    user = "'" + user + "'"
    data = Sql.select(1,'*','history','userid',user)
    return render_template('history.html',data = data)


# 视频信息统计图页面
@app.route('/chart/',)
def chart():
    global aid,user,num
    data = insert_data(aid,num)
    data_json = json.dumps(data)
    return render_template('chart.html',data_json = data_json)

@app.route('/chart/<str>')
def chart1(str):

    global aid,num
    if len(str)< 20:
        str1 = "'" + str[0:-8] + "'"
        str2 = str[-8:]
        data = Sql.select2(1,'*','video',str1,'class_name',str2,'mid')
    else:
        aid = str[0:-19]
        time = '"' + str[-19:-3] +'%'+'"'
        str = 'SELECT * FROM `video` where mid = {} AND timer like {}'
        data = Sql.special_sql(1,str,aid,time)
    data_json = json.dumps(data)
    return render_template('chart.html',data_json = data_json)


# 数据库中查找用来在页面中展示的数据
def insert_data(aid,num):
    str = 'SELECT * FROM `video` where mid = {} ORDER BY timer asc LIMIT {}'
    data = Sql.special_sql(1,str,aid,num)
    return data

if __name__ == '__main__':
    app.run(host= '0.0.0.0',port = 8000 ,debug = True)