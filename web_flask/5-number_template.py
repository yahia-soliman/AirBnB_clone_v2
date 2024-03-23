#!/usr/bin/python3
"""This Module starts a python server on all active IPs port 5000"""
from flask import Flask, render_template

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


@app.route('/python/<text>')
@app.route('/python')
def python(text='is cool'):
    """The python page route"""
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>')
def number(n):
    """this route accepts numbers"""
    return '{:d} is a number'.format(n)


@app.route('/number_template/<int:n>')
def number_template(n):
    """this route accepts numbers"""
    return render_template('5-number.html', number=n)


if __name__ == '__main__':
    app.run('0.0.0.0')
