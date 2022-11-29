#!/usr/bin/python2
"""Script that starts a Flask web application
web application must be listening on 0.0.0.0, port 5000
Routes:
    /: display “Hello HBNB!”
    /hbnb: display “HBNB”
    /c/<text>:
    display “C ” followed by the value
    of the text variable (replace underscore _ symbols with a space )
You must use the option strict_slashes=False in your route definition
"""

from flask import Flask
# from flask_cors import CORS
# from flask_socketio import SocketIO
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
# from flask_login import LoginManager
# from flask_bcrypt import Bcrypt

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """Display a hello message"""

    return "Hello HBNB!"


@app.route("/hbnh", strict_slashes=False)
def hbnb():
    """Display HBNH"""

    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """Display C ” followed by the value of the text"""

    return "C " + text


if __name__ == "__main__":
    # app.run(debug=True)
    app.run(host='0.0.0.0', port=5000, debug=True)
