from flask import Blueprint, request, jsonify, make_response, Response
import os
from sql.sql import Sql

file = Blueprint('file', __name__)

# 上传文件接口
@file.route('/saveFile', methods=['POST', 'OPTIONS'])
def saveFile():
    try:
        f = request.files['file']
        userName = request.form.get('userName')
        print(userName)
        # 获取文件名
        data = {
            'userName':userName,
            'fileName':f.filename
        }
        # 本地存储路径
        if not os.path.exists('./uploadImg'):
            os.makedirs('./uploadImg')
        lpath = os.path.abspath('./uploadImg')
        localpath = os.path.join(lpath,os.path.basename(data['fileName']))
        # 保存图片
        with open(localpath,'wb') as p:
            p.write(f.stream.read())

        # 文件存入数据库
        res = Sql.uploadFile(data)
        return make_response(jsonify(res))
    except Exception as e:
        data = {
            'result':e.__str__()
        }
        return make_response(jsonify(data)), 500

# 查看文件列表接口
@file.route('/findFile', methods=['POST'])
def findFile():
    try:
        parm = request.get_json(force=True)
        if parm['user']['userName'] == 'xiaoliu' or parm['user']['userName'] == 'xiaocao' :
            data = Sql.findFile({})
        else:
            data = Sql.findFile({'identity':False})
        return make_response(jsonify(data))
    except Exception as e:
        data = {
            'result':e.__str__()
        }
        return make_response(jsonify(data)), 500

# 获取文件接口
@file.route('/getFile', methods=['POST'])
def getFile():
    try:
        data = request.get_json(force=True)
        lpath = os.path.abspath(r'uploadImg')
        localpath = os.path.join(lpath,os.path.basename(data['fileName']))
        with open(localpath,'rb') as f:
            str = f.read()
        response = Response(str, content_type='application/octet-stream')
        response.headers['Content-disposition'] = 'attachment; filename=' + data['fileName']
        return response
    except Exception as e:
        data = {
            'result':e.__str__()
        }
        return make_response(jsonify(data)), 500
