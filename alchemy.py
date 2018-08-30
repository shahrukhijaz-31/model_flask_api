from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://ijaz:1997@localhost/school'
SQLALCHEMY_TRACK_MODIFICATIONS = False
db = SQLAlchemy(app)


class Student(db.Model):
    id = db.Column('student_id', db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100))
    city = db.Column(db.String(50))

    def __repr__(self):
        return '<User %r>' % self.username

    def __init__(self, name, city):
        self.name = name
        self.city = city