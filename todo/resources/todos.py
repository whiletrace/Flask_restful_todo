from flask import Blueprint, abort, url_for, jsonify
from flask_restful import (
    Api, Resource, fields, inputs, marshal, marshal_with, reqparse
    )


# defines logic todos endpoint
class TodoList(Resource):
    def __init__(self):
        # reqparse handles requests in the request response cycle
        # defines sh
        self.reqparse = reqparse.RequestParser()
        # adding arguments to parser for all fields coming in
        self.reqparse.add_argument(
            'name',
            required=True,
            # if not present
            help='todo not provided',
            # telling reqparse where to find data last is first place searched

            location=['form', 'json']
            )

        super().__init__()

    def get(self):
        return jsonify({'todo': [{'name': 'digging'}]})


todo_api = Blueprint('resources.todos', __name__)
api = Api(todo_api)

# define endpoints

# will output all todos
api.add_resource(
    TodoList,
    '/api/v1/todos',
    endpoint='todos'
    )
