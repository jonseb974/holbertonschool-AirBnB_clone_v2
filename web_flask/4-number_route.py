#!/usr/bin/python3
"""Script that starts a Flask web application:

    Web application must be listening on 0.0.0.0, port 5000
    Routes:
    /: display “Hello HBNB!”
    /hbnb: display “HBNB”

    /c/<text>: display “C ”, followed by the value
    of the text variable (replace underscore _ symbols with a space )

    /python/<text>: display “Python ”, followed by the value
    of the text variable (replace underscore _ symbols with a space )

The default value of text is “is cool”
/number/<n>: display “n is a number” only if n is an integer
You must use the option strict_slashes=False in your route definition
"""
from flask import Flask

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def hello():
    """Display hello message"""

    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Display hbnb"""

    return "HBNB"

@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """Display c"""

    text = text.replace("_", " ")
    return "c " + text

@app.route("/python/<text>", strict_slashes=False)
def python(text= "is cool"):
    """Display python"""

    text = text.replace("_", " ")
    return "python " + text

@app.route("/number/<n>", strict_slashes=False)
def number(n):
    """Display number"""

    n = int(n)
    return "n is " + int(n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
