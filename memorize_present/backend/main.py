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
    try:
        parm = request.get_json(force=True)  
        if bool(parm):
            if(bool(parm['userName'])):
                filter = "AND User_name = '{}'".format(parm['userName'])
            else:
                filter = ''
        else:
            filter = ''
        data = Sql.select('*','User_message',filter)
        return make_response(jsonify(data))
    except:
        return 'null'

if __name__ == '__main__':
    app.run(host= '0.0.0.0',port = 5000 ,debug = True)