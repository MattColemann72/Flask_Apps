from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import backref

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:passone@35.242.140.217:3306/todo_list'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
db = SQLAlchemy(app)

class TodoList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(50), nullable = False)
    complete = db.Column(db.Boolean, default=False)

@app.route('/')
def home():
    return 'This is a TODO App'

@app.route('/todos')
def todos():
    returnallTODO = TodoList.query.all()
    return str(returnallTODO)

    #return 'Show all the todos in the DB here.'


if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')