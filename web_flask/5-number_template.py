#!/usr/bin/python3
"""Script that starts a Flask web application:

Your web application must be listening on 0.0.0.0, port 5000
Routes:
    /: display “Hello HBNB!”
    /hbnb: display “HBNB”
/c/<text>: display “C ”, followed by the value
of the text variable (replace underscore _ symbols with a space )

/python/<text>: display “Python ”,
followed by the value of the text variable
(replace underscore _ symbols with a space )

The default value of text is “is cool”
/number/<n>: display “n is a number” only if n is an integer
/number_template/<n>: display a HTML page only if n is an integer:
H1 tag: “Number: n” inside the tag BODY
You must use the option strict_slashes=False in your route definition
"""

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """Display a hello message"""

    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Display a hello message"""

    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """Display C followed by text
    replace underscore _ symbols with
    space.
    """
    text = text.replace("_", " ")

    return "C {}" .format(text)


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """Display Python followed by text
    replace underscore _ symbols with
    space.
    """
    text = text.replace("_", " ")

    return "Python {}".format(text)


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """Display n is a  number
    only if n is an integer
    """
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """Display html page
    only if n is an integer:
    H1 tag: “Number: n” inside the tag BODY
    """
    return render_template("5-number.html", n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
