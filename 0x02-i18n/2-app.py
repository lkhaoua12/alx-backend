#!/usr/bin/env python3
""" Python Module """
from flask_babel import Babel
from flask import Flask, render_template

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """ Config class for Babel """

    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route('/', strict_slashes=False)
def hello_world() -> str:
    """ Basic home page view """
    return render_template("2-index.html")


@babel.localeselector
def get_locale() -> str:
    """Select a language to translate """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == "__main__":
    app.run()
