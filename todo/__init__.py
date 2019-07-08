import os
from flask import Flask, render_template
from peewee import *

from todo.models import Todo, db_wrapper
from todo.resources.todos import todo_api


def create_app(test_config=None):
    """
    This is an application factory pattern

    essentially a function that defines the application,
    loads defined configurations initializes the database file,
    and registers blue printsthat hold logic for api endpoints,
    :var
    app: flask application
    database: Sqlite database object

    :rtype: object: Flask application,
    """
    # Flask app defined
    # config files are relative to the instance folder
    app = Flask(__name__, instance_relative_config=True)

    # register blueprints for that hold logic for endpoints
    app.register_blueprint(todo_api)

    # database assignment at runtime
    app.config.from_mapping(
        DATABASE=SqliteDatabase(os.path.join(app.instance_path, 'todo.db'))
        )

    # holds value of actual database
    database = db_wrapper.database

    # FlaskDB database initialization
    # bind models and create tables
    # close the database connection
    with app.app_context():
        db_wrapper.init_app(app)
        database.connect(reuse_if_open=True)
        Todo.bind(database)
        Todo.create_table(safe=True)

        database.close()

    try:
        # creates instance dir
        os.makedirs(app.instance_path)
    except OSError:
        pass

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('dev_config.py', silent=True)
    else:
        # load the test config if passed in this case test/conftest
        app.config.update(test_config)


    #test route and route to angular app
    @app.route('/hello')
    def hello_world():
        """test route"""
        return 'Hello World'

    # this route Angular front end
    @app.route('/')
    def my_todo():
        return render_template('index.html')

    return app
