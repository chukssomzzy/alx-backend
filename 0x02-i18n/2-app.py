#!/usr/bin/env python3
"""Internalization enable flask app"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config(object):
    """Configure flask_babel"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


def get_locale():
    """Determine language from request"""
    return request.accept_languages.best_match(app.config["LANGUGES"])


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app, locale_selector=get_locale)


@app.route('/', strict_slashes=False)
def home() -> str:
    """Route to home"""
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)