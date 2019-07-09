# **Todo Restful API** 
[![Build Status](https://travis-ci.org/whiletrace/Flask_restful_todo.svg?branch=master)](https://travis-ci.org/whiletrace/Flask_restful_todo)



## **summary**
This project is a well tested restful API in this Instance the API is consumed by a Angular Front End
which was provided by a second party but included in this repository The API and front end are not tightly coupled and the Front end can be swapped out for another solution or make a custom solution for your self

### built on:
 * python  3.7.1
 * Flask 1.1.0
 * Flask_Restful 0.3.7
 * PEEWEE 3.9.6
 * Sqlite 
 * Pytest 4.6.3
 
 ### to run locally:
 * clone repo and cd to root dir
 * suggested that you run virtualenv
 * pip install **-r requirements.txt** within virtualenv shell
 
  ### start server and run application
 *  cd to root dir
 
 * in your terminal: export FLASK_APP=todo
 
 * flask run
 
#### application:
* application will be running on  http://127.0.0.1:5000/ to use application  
* click on new task and a new task will appear click on task created to give it a name, type a name and click save your task will be saved 
* checkmark your saved task to mark complete 
* update your task by clicking task and type something new and  click save 
* to delete task hit delete


 ## to run tests:
 *  cd to root dir
 
 * in your terminal: pytest

## ApI Documentation
There are two endpoints in this version. One endpoint for multiple resource operations and an endpoint for single resource operations this will expanded upon in the rest of the documentation.

### URL and Methods
#### multiple resources

###### URL

* /api/v1/todos

###### Methods

* `GET` |`POST`

###### params
* request body params
* accepted: JSON and x-wwww-form-urlencoded
* data type: object
* example `{"name": "something here"}` 

###### `GET`Success Response:
* Code: 200
* Content: `[ { "id": 1, "name": "cleaning the hippos" }, { "id": 2, "name": "love" }]`

###### `GET`Error Response
* This endpoint in general will not error for requests for multiple resources If there are no resources will output an empty array `[]`
###### `POST` Success Response
* Code: 201
* Content:`{ "id": 21, "name": "see you later" }`

###### `POST` Error Response
* Code: 400
* Content:`{ "message": "name not provided" }`

###### Other Error Responses
* methods != `GET`, `Post`
* Code: 405
* Content: `{"message": "The method is not allowed for the requested URL"}`



#### single resource
###### URL

* /api/v1/todos/int(id)

###### Methods

* `GET` |`PUT`| `DELETE`

###### params
* request body params
* accepted: JSON and x-wwww-form-urlencoded
* data type: object
* example `{"name": "something here"}` 

###### Path variable
* data type: integer
* required `id:integer`
* ex `/api/v1/todos/14`

###### `GET`Success Response:
* Code: 200
* Content: `[ { "id": 1, "name": "cleaning the hippos" }, { "id": 2, "name": "love" }]`

###### `GET`Error Response
* CODE:404
* Content: `{ "message": "The requested URL was not found on the server.
            If you entered the URL manually please check your spelling and try again." }`
###### `PUT` Success Response
* Code: 201
* Content:`{ "id": 21, "name": "see you later" }`

###### `PUT` Error Response
* Code: 400
* Content:`{ "message": "name not provided" }`
* CODE:404
* Content: `{ "message": "The requested URL was not found on the server.````
            If you entered the URL manually please check your spelling and try again." }`
###### `DELETE` Success Response
* Code: 204

###### `DELETE` Error Response
* CODE:404
* Content: `{ "message": "The requested URL was not found on the server.
            If you entered the URL manually please check your spelling and try again." }`

###### Other Error Responses
* methods != `GET`, `PUT`, `DELETE`
* Code: 405
* Content: `{"message": "The method is not allowed for the requested URL"}`






