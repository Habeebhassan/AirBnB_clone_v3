#!/usr/bin/python3

"""
Flask Web Application

This script starts a Flask web application that listens on 0.0.0.0, port 5000.
Routes:
/: Displays “Hello HBNB!”
/hbnb: Displays “HBNB”
/c/<text>: Displays “C ”, followed by the value of the text variable (replace underscore _ symbols with a space)
/python/<text>: Displays “Python ”, followed by the value of the text variable (replace underscore _ symbols with a space)
The default value of text is “is cool”
/number/<n>: Displays “n is a number” only if n is an integer
The option strict_slashes=False is used in route definitions
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Display 'Hello HBNB!'."""
    return render_template('hello.html')

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Display 'HBNB'."""
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """Display 'C ' followed by the value of text variable."""
    return 'C ' + text.replace('_', ' ')

@app.route('/python/<text>', strict_slashes=False)
@app.route('/python/', strict_slashes=False, defaults={'text': 'is cool'})
def python_text(text):
    """Display 'Python ' followed by the value of text variable."""
    return 'Python ' + text.replace('_', ' ')

@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """Display 'n is a number' if n is an integer."""
    return '{} is a number'.format(n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
