#!/usr/bin/python3
"""Flask web application
web application must be listening on 0.0.0.0, port 5000
Routes:
    /cities_by_states;
"""
from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=Flask)
def cities_by_states():
    """Display HTML page
    Staes/cities are stored.
    """

    states = storage.all("State")
    return render_template("8-cities_by_states.html", states=states)


@app.teardown_appcontext
def teardown(exc):
    """Remove current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
