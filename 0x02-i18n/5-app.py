#!/usr/bin/env python3

"""
  Module that instantiates a flask and
  Babel translator
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel

app = Flask(__name__)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config(object):
    """
      Babel config class
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """Chooses the best match for supported languages"""
    locale = request.args.get('locale')
    if locale:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user():
    """Gets a user_id and return a locale based on the info"""
    user_id = request.args.get('login_as')

    if user_id:
        user_info = users.get(int(user_id))
        return user_info
    return None


@app.before_request
def before_request():
    """Function before request"""
    user = get_user()
    g.user = user


@app.route('/')
def index():
    """Index page"""
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run(port="5000", host="0.0.0.0", debug=True)
