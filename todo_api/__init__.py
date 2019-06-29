import os
from flask import Flask, render_template
from peewee import *

from .models import Todo, db_wrapper


def create_app(test_config=None):
    """

    :rtype:
    """
    app = Flask(__name__, instance_relative_config=True)

    # database assignment at runtime
    app.config.from_mapping(
        DATABASE=SqliteDatabase(os.path.join(app.instance_path, 'todo.db'))
        )
    # FlaskDB database initialization
    db_wrapper.init_app(app)
    # holds value of actual database
    database = db_wrapper.database

    # bind model to database

    with app.app_context():
        Todo.bind(database)
        Todo.create_table(safe=True)
        database.close()

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('dev_config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.update(test_config)

    @app.route('/hello')
    def hello_world():
        """test route"""
        return 'Hello World'

    # this route Angular front end
    @app.route('/')
    def my_todo():
        return render_template('index.html')

    return app
