import flask
app = flask.Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return flask.render_template('test.html')

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')