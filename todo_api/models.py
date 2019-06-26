from peewee import *
from flask import current_app, g
from playhouse.flask_utils import FlaskDB
import os

db_wrapper = FlaskDB()

DATABASE = SqliteDatabase(None)


class Todo(db_wrapper.Model):
    name = CharField()

    class Meta:
        database = DATABASE








