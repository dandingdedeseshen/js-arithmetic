from flask import Flask
from flask_cors import *
from core.login import login
from core.file import file
from sql.sql import Sql

app = Flask(__name__)
CORS(app, supports_credentials=True)

@app.route('/') 
def fun():
    return '欢迎来到淡定的得瑟神的秘密基地!!!!!!!'

app.register_blueprint(login)
app.register_blueprint(file)
Sql.tl.start()

if __name__ == '__main__':
    # app.run(host= '0.0.0.0',port = 5000 ,debug = True)
    app.run(host= '0.0.0.0',port = 5000 ,debug = True, use_debugger=False, use_reloader=False)