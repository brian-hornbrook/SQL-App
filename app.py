from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask("app")

# create a place to store the database
app.config["SQLALCHEMY_DATABASE_URL"] = "sqlite:///test.db"

# create a database object by creating a SQLAlchemy class
db = SQLAlchemy(app)

# holds all the columns for the users
class User(db.Model):
	# sets id to be a column
	# set to Interger or String for data type
	# unique sets whether the data must be unique from the other data
	# nullable=False means each of these must be completed
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(120), unique=True, nullable=False)
	email = db.Column(db.String(120), unique=True, nullable=False)
	about_me = db.Column(db.String(500), unique=False, nullable=False)

def __repr__(self):
	return "<Welcome to the profile of Brian >"

@app.route('/')
def index():
    return 'Hello from Flask!'

app.run(host='0.0.0.0', port=8000)