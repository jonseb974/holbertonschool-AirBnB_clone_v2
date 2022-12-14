#!/usr/bin/python3
"""Script that starts a Flask web application:
Web application must be listening on 0.0.0.0, port 5000
Routes:
    /states_list: display a HTML page
"""
from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """Display html page with list of states.
    States are stored by name
    """
    states = storage.all("State")
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def teardown(exc):
    """Remove current SQLAlchemy session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
