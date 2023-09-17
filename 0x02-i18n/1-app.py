#!/usr/bin/env python3

"""
  Module that instantiates a flask and
  Babel translator
"""

from flask import Flask, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """
      Babel config class
    """
    LANGUAGES = ["en", "fr"]


babel.default_locale = Config.LANGUAGES[0]
babel.default_timezone = "UTC"


app.config.from_object(Config)
