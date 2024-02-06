#!/usr/bin/env python3
"""Internalization enable flask app"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home() -> str:
    """Route to home"""
    return (render_template('0-index.html'))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
