from peewee import *
from playhouse.flask_utils import FlaskDB

db_wrapper = FlaskDB()


class Todo(db_wrapper.Model):
    name = CharField()
