#!/usr/bin/env python3
""" simple flask app """
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
    """ home page render view """
    return render_template("1-index.html")


if __name__ == "__main__":
    app.run()
