"""this is a flask app"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/hbnb_filters')
def filters():
    """get the filters page"""
    from models.state import State
    from models.amenity import Amenity
    states = storage.all(State).values()
    am = storage.all(Amenity).values()
    return render_template('10-hbnb_filters.html', states=states, amenities=am)


if __name__ == '__main__':
    app.run('0.0.0.0')
