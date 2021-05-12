from flask import Flask, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import backref
from sqlalchemy.sql.schema import RETAIN_SCHEMA

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:passone@35.242.140.217:3306/todo_list'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
db = SQLAlchemy(app)

class TodoList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(50), nullable = False)
    complete = db.Column(db.Boolean, default=False)

@app.route('/')
def index():
    all_todos = TodoList.query.all()
    todos_string = ""
    for todo in all_todos:
        todos_string += "<br>" + str(todo.id) + todo.task + str(todo.complete)

    return todos_string
    
    # all_todos = TodoList.query.all()
    # todos_string = ""
    # for todo in all_todos:
    #     todos_string += "<br>" + str(TodoList.id) + " " + TodoList.task + " " + str(TodoList.complete)
    # return todos_string

@app.route('/complete/<int:todo_id>')
def completetodo(todo_id): 
    completeme = TodoList.query.get(todo_id)
    completeme.complete = True
    db.session.commit()
    return "Completed Todo"

@app.route('/incomplete/<int:todo_id>')
def incompletetodo(todo_id): 
    completeme = TodoList.query.get(todo_id)
    completeme.complete = False
    db.session.commit()
    return "Incompleted Todo"

# @app.route('/delete/<int:todo_id')
# def delete(todo_id):
#     deleteme = TodoList.query.get(todo_id)
#     db.session.delete(deleteme)
#     db.session.commit()
#     #return redirect(url_for("index"))
#     return ""

@app.route('/add')
def add():
    addme = TodoList(task = "New ToDo")
    db.session.add(addme)
    db.session.commit()
    return addme.task

@app.route('/delete/<int:id>')
def delete(id):
    deleteme = TodoList.query.get(id)
    db.session.delete(deleteme)
    db.session.commit()
    return redirect(url_for("index"))



'''
Create Routes that Adds a new Todo with the value "New Todo" everytime
	Create 2 routes, one that completes the todo specified in the path ie. /complete/1 would complete todo with ID 1, it should return a message saying "Completed todo 1"
	
    Create a route that deletes the todo in the path i.e. /delete/1 will delete todo with ID 1
	
    Create templates, a layout.html (That will have the layout) and index.html (which displays all todos)
	
    Change your template to show this "&#9989" if the todo is complete 
	
    Create a form that will allow users to enter todos and put this form in a new template called add.html
	(Stretch Goal) Add buttons at the top of every page to the home and add pages to make it easier to navigate
'''





    #return 'Show all the todos in the DB here.'


if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')