from flask import Flask, request, jsonify, make_response
from sql import Sql
from flask_cors import *
import smtplib
from email.mime.text import MIMEText
from email.header import Header
 
sender = '1392574566@qq.com'
receivers = ['1392574566@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

app = Flask(__name__)
CORS(app, supports_credentials=True)

# def makeRes(data,code):
#     res = {'data':data,'code':code}
    # res = make_response(jsonify(resCup))
    # res.headers['Access-Control-Allow-Origin'] = '*'
    # res.headers['Access-Control-Allow-Method'] = '*'
    # res.headers['Access-Control-Allow-Headers'] = '*'
    # return res

@app.route('/search', methods=['POST', 'OPTIONS'])
def serach():
    try:
        parm = request.get_json(force=True)  
        if bool(parm):
            if(bool(parm['type'])):
                filter = "AND type = '{}'".format(parm['type'])
            else:
                filter = ''
        else:
            filter = ''
        data = Sql.select('*','dataWarehouse',filter)
        return make_response(jsonify(data))
    except:
        return 'null'

@app.route('/update', methods=['POST', 'OPTIONS'])
def update():
    # try:
    
    parm = request.get_json(force=True) 
    if(int(parm['num']) <= 30):
        sendMai("{}库存不足，仅剩余{}!!".format(parm['type'],parm['num'])) 
    if bool(parm['id']):
        filter = 'AND id = {}'.format(parm['id'])
        data = Sql.update('dataWarehouse','num = {}'.format(parm['num']),filter)
    else:
        data = Sql.insert('dataWarehouse','(type,num) VALUES ("{}",{})'.format(parm['type'],parm['num']))
    return make_response(jsonify(data))
    # except:
    #     return 'fail'

@app.route('/delete', methods=['POST', 'OPTIONS'])
def delete():
    try:
        parm = request.get_json(force=True)  
        filter = 'AND id = {}'.format(parm['id'])
        data = Sql.update('dataWarehouse','isDel = "1"',filter)
        return make_response(jsonify(data))
    except:
        return 'fail'

def sendMai(content):
    # 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
    message = MIMEText(content, 'plain', 'utf-8')
    message['From'] = Header("菜鸟教程", 'utf-8')   # 发送者
    message['To'] =  Header("测试", 'utf-8')        # 接收者
    
    subject = '库存不足'
    message['Subject'] = Header(subject, 'utf-8')
    # try:
    smtpObj = smtplib.SMTP('1392574566@qq.com')
    smtpObj.sendmail(sender, receivers, message.as_string())
    print ("邮件发送成功")
    # except smtplib.SMTPException:
    #     print ("Error: 无法发送邮件")