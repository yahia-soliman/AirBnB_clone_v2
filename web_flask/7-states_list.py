#!/usr/bin/python3
"""A script that starts a Flask web application."""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.before_request
@app.teardown_request
def after_any(error):
    """close and refresh the db connection after each request"""
    storage.close()


@app.route('/states_list')
def states_list():
    """get a list of available states"""
    from models.state import State
    states = storage.all(State)
    return render_template('7-states_list.html', states=states.values())


if __name__ == '__main__':
    app.run('0.0.0.0')
