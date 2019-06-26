import os
from flask import Flask, render_template
from peewee import *
from playhouse.flask_utils import FlaskDB
from .models import Todo

# instantiation of FlaskDB database wrapper
db_wrapper = FlaskDB()


def create_app(test_config=None):
    """

    :rtype:
    """
    app = Flask(__name__, instance_relative_config=True)

    # database assignment at runtime
    app.config['DATABASE'] = 'sqlite:/instance/todo.db'
    # FlaskDB database initialization
    db_wrapper.init_app(app)

    # holds value of actual database
    database = db_wrapper.database
    # bind model to database
    Todo.bind(database)
    #create db tables
    Todo.create_table(fail_silently=True, safe=True)

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
