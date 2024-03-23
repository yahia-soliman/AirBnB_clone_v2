#!/usr/bin/python3
"""This Module starts a python server on all active IPs port 5000"""
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello():
    """The home page route"""
    return b'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """The hbnb page route"""
    return b'HBNB'


@app.route('/c/<text>')
def c(text):
    """The C page route"""
    return 'C ' + text.replace('_', ' ')


if __name__ == '__main__':
    app.run('0.0.0.0')
