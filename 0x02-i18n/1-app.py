#!/usr/bin/env python3

"""
  Module that instantiates a flask and
  Babel translator
"""

from flask import Flask
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)

class Config(object):
    """
      Babel config class
    """
    LANGUAGES = ["en", "fr"]
@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(app.config['LANGUAGES'])
