from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import backref

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:passone@35.242.140.217:3306/testdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
db = SQLAlchemy(app)


# class Users(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     #age = db.Column(db.Integer, nullable=False)
#     first_name = db.Column(db.String(30), nullable=False)
#     last_name = db.Column(db.String(30), nullable=False)

# class Countries(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(30), nullable=False)
#     cities = db.relationship('Cities', backref='country') 

# class Cities(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(30), nullable=False)
#     country_id = db.Column(db.Integer, db.ForeignKey('countries.id'), nullable=False)

class Orders(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(50), nullable = False)
    total_cost = db.Column(db.Float(10,2), nullable = False)
    chosen_items = db.relationship("ChosenItems", backref="order")


class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable = False)
    price = db.Column(db.Float(10,2), nullable = False)
    quantity = db.Column(db.Integer, nullable = False)
    chosen_items = db.relationship("ChosenItems", backref="product")


class ChosenItems(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, foreign_key('orders.id'), nullable = False)
    product_id = db.Column(db.Integer, foreign_key('products.id'), nullable = False)

if __name__=='__main__':
    app.run(debug==True, host='0.0.0.0')