#!/usr/bin/env python3
""" Python Module """
from flask import Flask, render_template, request
from flask_babel import Babel


class Config(object):
    """
    babel config class
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """
    babel local config
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index():
    """
    home page view
    """
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run()
