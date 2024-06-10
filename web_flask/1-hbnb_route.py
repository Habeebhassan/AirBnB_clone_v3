#!/usr/bin/python3
"""
Hello HBNB Flask App

This script starts a simple Flask web application that listens on all IP addresses
(0.0.0.0) on port 5000. It has two routes:
- /: Displays "Hello HBNB!"
- /hbnb: Displays "HBNB"

How to use this script:
1. Save this file as `app.py`.
2. Make it executable with the command `chmod +x app.py`.
3. Ensure Flask is installed (`pip install Flask`).
4. Run the script with `./app.py`.
5. Open your web browser and go to `http://0.0.0.0:5000` for "Hello HBNB!" or `http://0.0.0.0:5000/hbnb` for "HBNB".

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

if __name__ == "__main__":
    # Run the Flask app
    app.run(host="0.0.0.0", port=5000)
