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
		return f"<Welcome to the profile of {self.username}>"

db.create_all()
db.session.commit()
		
# create instances of user
new_user1 = User(id=1, username="Hannah", email="HappyHannah@gmail.com", about_me="I love snacks, running, and sassy attitudes!")
new_user2 = User(id=2, username="Jeorge", email="HappyGeorge@gmail.com", about_me="I love eating bananas, climing trees")

# Create
db.session.add(new_user1)
db.session.add(new_user2)
db.session.commit()

# Read
all_users = User.query.all()
print(all_users)

# Delete
user = User.query.filter_by(username="Hannah").first()
if user:
	db.session.delete(user)
	db.session.commit()

all_users = User.query.all()
print(all_users)

@app.route('/')
def index():
    return "Welcome to User App"

app.run(host='0.0.0.0', port=8000)