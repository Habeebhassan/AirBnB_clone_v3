#!/usr/bin/python3
"""
Hello HBNB Flask App

This script starts a simple Flask web application that listens on all IP addresses
(0.0.0.0) on port 5000. It has three routes:
- /: Displays "Hello HBNB!"
- /hbnb: Displays "HBNB"
- /c/<text>: Displays "C " followed by the value of the text variable, with underscores replaced by spaces

How to use this script:
1. Save this file as `app.py`.
2. Make it executable with the command `chmod +x app.py`.
3. Ensure Flask is installed (`pip install Flask`).
4. Run the script with `./app.py`.
5. Open your web browser and go to:
   - `http://0.0.0.0:5000/` for "Hello HBNB!"
   - `http://0.0.0.0:5000/hbnb` for "HBNB"
   - `http://0.0.0.0:5000/c/<text>` for "C <text>"

You should see the respective messages on the pages.
"""

from flask import Flask

# Initialize the Flask application
app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Route handler for the root URL.
    
    Returns:
        str: A greeting message "Hello HBNB!".
    """
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Route handler for the /hbnb URL.
    
    Returns:
        str: A simple message "HBNB".
    """
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
    Route handler for the /c/<text> URL.
    
    Args:
        text (str): The text to display.
        
    Returns:
        str: A message "C " followed by the text variable with underscores replaced by spaces.
    """
    return "C " + text.replace('_', ' ')

if __name__ == "__main__":
    # Run the Flask app
    app.run(host="0.0.0.0", port=5000)
