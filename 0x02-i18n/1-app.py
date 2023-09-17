#!/usr/bin/env python3

"""
  Module that instantiates a flask and
  Babel translator
"""

from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)


class Config(object):
    """
      Babel config class
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
babel = Babel(app)


@app.route('/')
def index():
    """Index page"""
    return render_template('1-index.html')


if __name__ == '___main__':
    app.run()
