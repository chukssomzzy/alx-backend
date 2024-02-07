#!/usr/bin/env python3
"""Internalization enable flask app"""
from typing import Dict, Union
from flask import Flask, g, render_template, request
from flask_babel import Babel

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config(object):
    """Configure flask_babel"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


def get_user() -> Union[None, Dict]:
    """Check if a user exit and returns the user"""
    id = request.args.get("login_as")
    if id is None or int(id) not in users:
        return None
    return users[int(id)]


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale() -> Union[str, None]:
    """Determine language from request"""
    locale = request.args.get("locale")
    if locale in app.config["LANGUAGES"]:
        return locale
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.before_request
def before_request() -> Union[Dict, None]:
    """logins a users"""
    user = get_user()
    if user:
        g.user = user
    else:
        g.user = None


@app.route('/', strict_slashes=False)
def home() -> str:
    """Route to home"""
    print(g.user)
    return render_template('5-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
