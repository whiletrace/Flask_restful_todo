from flask import Flask, render_template
from todo_api import config
import os
from todo_api import models


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY=config.SECRET_KEY,
        ),

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    models.initialize()

    @app.route('/')
    def my_todos():
        return render_template('index.html')

    return app
