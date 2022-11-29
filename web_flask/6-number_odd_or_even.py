#!/usr/bin/python3
"""Script that starts a Flask web application:

Web application must be listening on 0.0.0.0, port 5000
Routes:
    /: display “Hello HBNB!”
    /hbnb: display “HBNB”

    /c/<text>: display “C ”, followed by the value
    of the text variable (replace underscore _ symbols with a space )
    /python/<text>: display “Python ”,
    followed by the value of
    the text variable (replace underscore _ symbols with a space )

The default value of text is “is cool”
    /number/<n>: display “n is a number” only if n is an integer
    /number_template/<n>: display a HTML page only if n is an integer:

H1 tag: “Number: n” inside the tag BODY
    /number_odd_or_even/<n>: display a HTML page only if n is an integer:
H1 tag: “Number: n is even|odd” inside the tag BODY
You must use the option strict_slashes=False in your route definition
"""
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """Display message Hello HBNB"""

    return "Hello HBNB !"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Display message HBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """Disaplay C
    followed by the value
    of the text variable (replace underscore _ symbols with a space
    """
    text = text.replace("_", " ")

    return "C {}" .format(text)


@app.route("/python/<text>", strict_slashes=False)
def python(text):
    """Display message Python
    followed by the value of the text variable
    replace underscore _ symbols with a space
    """
    text = text.replace("_", " ")

    return "Python {}".format(text)


@app.route("/number/<n>", strict_slashes=False)
def number(text="is cool"):
    """Display message Number: n is a number
    display “n is a number” only if n is an integer
    """

    return "Number: {}".format(text)


@app.route("/number_template/<n>", strict_slashes=False)
def number_template(text="is cool"):
    """Display message Number: n is a number
    display a HTML page only if n is an integer:
    """

    return render_template("number_template.html", text=text)