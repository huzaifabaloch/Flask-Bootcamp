# adoption.py file  # # MAIN APP FILE # #
import os
from forms import AddForm, DelForm
from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'

#################################################
#### SQL DATABASE SECTION #######################
#################################################

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 
                                                'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)

########################
####### MODELS #########
########################

class Puppy(db.Model):

    __tablename__ = 'puppies'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'Puppy name: {self.name}'

######################################################

#################################
##### VIEW FUNCTIONS - Have Forms
#################################

@app.route('/')
def index():

    return render_template('index.html')


@app.route('/add', methods=['GET', 'POST'])
def add_puppy():

    form = AddForm()

    if form.validate_on_submit():
        name = form.name.data

        new_pup = Puppy(name)
        db.session.add(new_pup)
        db.session.commit()

        return redirect(url_for('list_puppy'))
    
    return render_template('add.html', form=form)


@app.route('/list')
def list_puppy():

    puppies = Puppy.query.all()

    return render_template('list.html', puppies=puppies)


@app.route('/delete', methods=['GET', 'POST'])
def delete_puppy():

    form = DelForm()

    if form.validate_on_submit():
        id = form.id.data

        puppy_id = Puppy.query.get(id)
        db.session.delete(puppy_id)
        db.session.commit()

        return redirect(url_for('list_puppy'))

    return render_template('delete.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)