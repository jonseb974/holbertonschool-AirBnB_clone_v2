#!/usr/bin/python3
"""Script that starts a Flask web application:

Your web application must be listening on 0.0.0.0, port 5000
"""
from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def states():
    """
    """

    states = storage.all("State")
    return render_template("9-states.html", state=states)


@app.route("/states/<id>", strict_slashes=False)
def state_id(id):
    """Display HTML page"""
    for state in storage.all("State").value():
        if state.id == id:
            return render_template("9-states.html", state=state)
    return render_template("9-states.html")


@app.teardown_appcontext
def teardown(exc):
    """Remove current SQLAlchemy session"""
    storage.close()


if __name__ == "__main__":
    app.rum(host="0.0.0.0")
