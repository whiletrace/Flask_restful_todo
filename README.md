# **Todo Restful API** 
[![Build Status](https://travis-ci.org/whiletrace/Flask_restful_todo.svg?branch=master)](https://travis-ci.org/whiletrace/Flask_restful_todo)



## **summary**
This project is a well tested restful API in this Instance the API is consumed by a Angular Front End
which was provided by a second party but included in this repository The API and front end are not tightly coupled and the Front end can be swapped out for another solution or make a custom solution for your self

### built on:
 * python  3.7.1
 * Flask 1.1.0
 * Flask_Restful 0.3.7
 * PEEWEE ORM
 * Sqlite
 * Pytest
 
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
