from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import backref

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql@//root:passone@35.242.140.217:3306/testdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Countries(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(30), nullable = False)
    cities = db.relationship('Cities', backref = 'country')

class Cities(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(30), nullable = False)
    country_id = db.Column(db.Integer, db.ForeignKey('countries.id'), nullable = False)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")