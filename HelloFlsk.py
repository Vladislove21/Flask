from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'

@app.route('/you')
def you():
    return 'Hi, my love. I`m just learning framework and I need know that everything is fine'

