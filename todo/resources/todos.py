from flask import Blueprint, abort
from flask_restful import (
    Api, Resource, fields, marshal, marshal_with, reqparse
    )
from todo import models

todo_fields = {'id': fields.Integer, 'name': fields.String}


def todo_or_404(todo_id):
    """
    utility function returns model object with correct id

    if resource DoesNotExist then the abort method is called
    which takes a status code as argument and returns a http response
    containing a message and the status code in the response body
    :param todo_id:
    :type todo_id: int
    :return:
    :rtype:
    """
    try:
        todo = models.Todo.get(models.Todo.id == todo_id)
    except models.Todo.DoesNotExist:
        abort(404)
    else:
        return todo


# defines logic /api/v1/todos endpoint
class TodoList(Resource):
    """
    Class defines TodoList resource objects for endpoint /api/v1/todos

    sub classes flask_Restful Resource
    class methods:
    dunder init
    get
    post
    class attr: parser
    """
    def __init__(self):
        """
        defines object attributes
        """

        # reqparse validates http requests data
        self.parser = reqparse.RequestParser()
        # adding arguments to parser
        # defines validation for request data coming to endpoint
        self.parser.add_argument(
            'name',
            required=True,
            # if not present
            help='name not provided',

            # telling reqparse where to find data last is first place searched
            location=['form', 'json']
            )

        super().__init__()

    def get(self):
        """
        method handles logic for http response to GET request multiple resources

        queries the database and gets raw data
        marshals or filters that data based upon fields arguments
        returns the marshaled data

        :rtype: list
        :returns  [OrderedDict([('id', 2), ('name', 'love')])]
        """
        todos = [marshal(todo, todo_fields) for todo in models.Todo.select()]
        return todos

    @marshal_with(todo_fields)
    def post(self):
        """
        method handles logic for http response to post request

        creates new resource in database table and gets raw data of resource
        marshals or filters that data based upon fields arguments
        returns the marshaled data and a 201 status code

        :rtype: object
        :returns  <object: object.id> 201
        """
        args = self.parser.parse_args()
        todo = models.Todo.create(**args)
        return todo, 201


class Todo(Resource):
    """
    Class defines Todos resource objects for endpoint /api/v1/todos/<int:id>

    sub classes flask_Restful Resource
    class methods:
    __init__.
    get
    post

    class attr:
    parser
    """

    def __init__(self):
        """
        defines object attributes

        """
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
        """
        Method handles logic for http response to GET request single resource.

        :param id
        :returns results of function call to todo_or_404 with id as argument
        :rtype: object
        """
        return todo_or_404(id)

    @marshal_with(todo_fields)
    def put(self, id):
        """
        Method handles logic for http response to put request.

        updates resource with matching id in database:
        in database table and returns filtered results of def todo_or_404
        which either returns an objector "if resource not found"
        returns a message and response status code 404
        :param id
        :returns  results of function call to todo_or_404 with id as argument
        :rtype: object
        """
        args = self.parser.parse_args()
        query = models.Todo.update(**args).where(models.Todo.id == id)
        query.execute()
        return todo_or_404(id), 201

    @marshal_with(todo_fields)
    def delete(self, id):
        """
        Method handles logic for http response to delete request.

        deletes resource with matching id in database:
        :param id
        :returns status code 204 empty response
        :rtype: object
        """
        query = models.Todo.delete().where(models.Todo.id == id)
        query.execute()
        return '', 204


# defines blueprint and instantiates blueprint
todo_api = Blueprint('resources.todos', __name__)
# defines and instantiates  API
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
