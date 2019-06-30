from peewee import *
from playhouse.flask_utils import FlaskDB


class NewFlaskDb(FlaskDB):
    def connect_db(self):
        self.database.connect(reuse_if_open=True)


db_wrapper = NewFlaskDb()


class Todo(db_wrapper.Model):
    name = CharField()
