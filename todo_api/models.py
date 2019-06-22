from peewee import *

from flask.cli import with_appcontext
import os

DATABASE = SqliteDatabase('./instance/todos.db')


class Todo(Model):
    name = CharField

    class Meta:
        database = DATABASE


def initialize():
    DATABASE.connect(reuse_if_open=True)
    DATABASE.create_tables([Todo], safe=True)
    DATABASE.close()

