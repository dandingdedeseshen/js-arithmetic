from flask import Blueprint, request, jsonify, make_response
from flask_cors import *
from sql.sql import Sql

login = Blueprint('login', __name__)

# 登录接口
@login.route('/login', methods=['POST', 'OPTIONS'])
def login1():
  # TODO 获取加密数据判断登录状态
  try:
    data = Sql.login(request.get_json(force=True))
    return make_response(jsonify(data))
  except Exception as e:
    data = {
      'result':e.__str__()
    }
    return make_response(jsonify(data)), 500


