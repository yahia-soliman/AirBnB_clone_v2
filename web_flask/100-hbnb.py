"""this is a flask app"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/hbnb')
def hbnb_home():
    """get the home page of hbnb"""
    from models.state import State
    from models.amenity import Amenity
    from models.place import Place
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    places = storage.all(Place).values()
    return render_template('100-hbnb.html',
                           states=states, amenities=amenities, places=places)


if __name__ == '__main__':
    app.run('0.0.0.0')
