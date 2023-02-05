from flask import Flask, request, jsonify, make_response
from sql import Sql
from flask_cors import *

app = Flask(__name__)
CORS(app, supports_credentials=True)

@app.route('/') 
def fun():
    return 'hello world111'
    
# 登录接口
@app.route('/login', methods=['POST', 'OPTIONS'])
def login():
    # TODO 获取加密数据判断登录状态
    try:
        data = Sql.login(request.get_json(force=True))
        return make_response(jsonify(data))
    except Exception as e:
        data = {
            'result':e.__str__()
        }
        return make_response(data)

# 登录接口
@app.route('/saveFile', methods=['POST', 'OPTIONS'])
def saveFile():
    try:
        f = request.files['file']
        # f = request.form.get('bam')
        # 获取文件名
        print(f.fileName)
        f.save('./uploaded_file.jpg')
        return {
            'aa':123
        }
    except Exception as e:
        print(e)
        data = {
            'result':e.__str__()
        }
        return make_response(data)

if __name__ == '__main__':
    app.run(host= '0.0.0.0',port = 5000 ,debug = True)