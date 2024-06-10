#!/usr/bin/python3
"""
A simple Flask web application with multiple routes.

Routes:
/                       - Display “Hello HBNB!”
/hbnb                  - Display “HBNB”
/c/<text>              - Display “C ” followed by the value of the text variable 
                         (replace underscore _ symbols with a space)
/python/               - Display “Python is cool” by default
/python/<text>         - Display “Python ” followed by the value of the text variable 
                         (replace underscore _ symbols with a space)
/number/<n>            - Display “n is a number” only if n is an integer
/number_template/<n>   - Display an HTML page only if n is an integer:
                         H1 tag: “Number: n” inside the tag BODY

The application listens on 0.0.0.0, port 5000.
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Return a greeting message 'Hello HBNB!'."""
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Return a message 'HBNB'."""
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """Return 'C ' followed by the value of the text variable 
    with underscores replaced by spaces."""
    return "C " + text.replace('_', ' ')

@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text="is cool"):
    """Return 'Python ' followed by the value of the text variable 
    with underscores replaced by spaces. Default is 'is cool'."""
    return "Python " + text.replace('_', ' ')

@app.route('/number/<int:n>', strict_slashes=False)
def number_n(n):
    """Return '<n> is a number' only if n is an integer."""
    return f"{n} is a number"

@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Return an HTML page only if n is an integer with the H1 tag 'Number: n'."""
    return render_template('number_template.html', n=n)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
