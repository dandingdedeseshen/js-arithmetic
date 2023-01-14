import flask
app = flask.Flask(__name__)
@app.route('/') 
def fun():
    return 'hello world'
if __name__ == '__main__':
    app.run(host = '0.0.0.0',debug = True)