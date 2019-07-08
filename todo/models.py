from peewee import *
from playhouse.flask_utils import FlaskDB


class NewFlaskDb(FlaskDB):
    """ subclass of FlaskDB as workaround for db connection leakage"""
    def connect_db(self):
        """overridden method now reuses db connection if already open"""
        self.database.connect(reuse_if_open=True)


#  instantiation of Database proxy obj
db_wrapper = NewFlaskDb()


class Todo(db_wrapper.Model):

    """ database model definition with one field sub classes Model class"""
    name = CharField()
