import flask
app = flask.Flask(__name__)
@app.route('/') 
def fun():
    return 'hello world111'
if __name__ == '__main__':
    app.run(host= '127.0.0.1',port = 8000 ,debug = True)