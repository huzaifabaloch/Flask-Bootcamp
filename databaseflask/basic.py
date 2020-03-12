import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate  # MIGRATION


#####################################
# line 12, 18, 19, 21
# SETTING UP SQLITE DATABASE USING ONLY PYTHON CODE.
#################################################

# Getting the current directory path to store database file.
base_dir = os.path.abspath(os.path.dirname(__file__))

# Creating Flask application instance.
app = Flask(__name__)

# Connect flask app to our database.     Using SQLITE DATABASE and storing the database to base location.
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(base_dir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

db = SQLAlchemy(app)

Migrate(app, db)  # This connects the DB with app to do migrations.
######################################################

# Creating our first MODEL  ->   TABLE in SQL Database
class Puppy(db.Model):

    # Manually naming table.
    __tablename__ = 'puppies'


    # Creating columns.
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    age = db.Column(db.Integer)
    breed = db.Column(db.Text)

    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    # String representation
    def __repr__(self):
        return f'Puppy {self.name} is {self.age} year/s old'