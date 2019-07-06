from flask import Blueprint, abort, url_for, jsonify
from flask_restful import (
    Api, Resource, fields, inputs, marshal, marshal_with, reqparse
    )
from todo import models

todo_fields = {'id': fields.Integer, 'name': fields.String}


def todo_or_404(todo_id):
    try:
        todo = models.Todo.get(models.Todo.id == todo_id)
    except models.Todo.DoesNotExist:
        abort(404)
    else:
        return todo

# defines logic todos endpoint
class TodoList(Resource):
    def __init__(self):
        # reqparse handles requests in the request response cycle
        # defines sh
        self.parser = reqparse.RequestParser()
        # adding arguments to parser for all fields coming in
        self.parser.add_argument(
            'name',
            required=True,
            # if not present
            help='todo not provided',
            # telling reqparse where to find data last is first place searched

            location=['form', 'json']
            )

        super().__init__()

    def get(self):
        todos = [marshal(todo, todo_fields) for todo in models.Todo.select()]
        return todos

    @marshal_with(todo_fields)
    def post(self):
        args = self.parser.parse_args()
        todo = models.Todo.create(**args)
        return todo, 201


class Todo(Resource):

    def __init__(self):
        self.parser = reqparse.RequestParser()

        self.parser.add_argument(
            'name',
            required=True,
            # if not present
            help='todo not provided',
            # telling reqparse where to find data last is first place searched

            location=['form', 'json']
            )

        super().__init__()

    @marshal_with(todo_fields)
    def get(self, id):
        # calls function add reviews
        # which calls course_or_404
        # which in effect will add review
        # attribute to the course if the course exists
        # otherwise will throw a 404 see notes
        # on each function
        return todo_or_404(id)

    @marshal_with(todo_fields)
    def put(self, id):
        args = self.parser.parse_args()
        query = models.Todo.update(**args).where(models.Todo.id == id)
        query.execute()
        return todo_or_404(id), 201

    @marshal_with(todo_fields)
    def delete(self, id):

        query = models.Todo.delete().where(models.Todo.id == id)
        query.execute()
        return '', 204


todo_api = Blueprint('resources.todos', __name__)
api = Api(todo_api)

# define endpoints

# will output all todos
api.add_resource(
    TodoList,
    '/api/v1/todos',
    endpoint='todos'
    )
# will
api.add_resource(
    Todo,
    '/api/v1/todos/<int:id>',
    endpoint='todo'
    )
