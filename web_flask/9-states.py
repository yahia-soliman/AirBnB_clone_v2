#!/usr/bin/python3
"""A script that starts a Flask web application."""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def after_any(error):
    """close and refresh the db connection after each request"""
    storage.close()


@app.route('/states')
def states():
    """get a list of available states"""
    from models.state import State
    states = storage.all(State)
    return render_template('7-states_list.html', states=states.values())


@app.route('/states/<id>')
def cities_in_state(id):
    """get a list of available states"""
    from models.state import State
    states = storage.all(State)
    state = states.get('State.{}'.format(id))
    return render_template('9-states.html', state=state)


if __name__ == '__main__':
    app.run('0.0.0.0')
