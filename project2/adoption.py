# adoption.py file  # # MAIN APP FILE # #
import os
from forms import AddForm, DelForm, AddOwnerForm
from flask import Flask, render_template, redirect, url_for, flash
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

    owner = db.relationship('Owner', backref='Puppy', uselist=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        if self.owner:
            return f'Puppy name: {self.name} and the owner is {self.owner.name}'
        else:
            return f'Puppy name: {self.name} and has no owner yet!'


class Owner(db.Model):

    __tablename__ = 'owners'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    puppy_id = db.Column(db.Integer, db.ForeignKey('puppies.id'))

    def __init__(self, name, puppy_id):
        self.name = name
        self.puppy_id = puppy_id

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
        pup_id = form.id.data

        puppy_id = Puppy.query.filter_by(id=pup_id).first()

        if not puppy_id:
            flash('There is no such id number associated with a puppy.')
            return redirect(url_for('delete_puppy'))
        else:
            puppy_id = Puppy.query.get(pup_id)
            db.session.delete(puppy_id)
            db.session.commit()
            return redirect(url_for('list_puppy'))

    return render_template('delete.html', form=form)


@app.route('/owner', methods=['GET', 'POST'])
def owner():

    form = AddOwnerForm()

    if form.validate_on_submit():
        name = form.name.data
        pup_id = form.puppy_id.data

        is_puppy = Puppy.query.filter_by(id=pup_id).first()
        if not is_puppy:
            flash('There is no such id number associated with a puppy. Please choose different one.')
            return redirect(url_for('owner'))
        else:
            owner_check = Owner.query.filter_by(puppy_id=pup_id).first()
            if owner_check:
                flash(f'Sorry, but this puppy is already adopted by {owner_check.name}')
                return redirect(url_for('owner'))
            
            owner = Owner(name, pup_id)
            db.session.add(owner)
            db.session.commit()

        return redirect(url_for('list_puppy'))

    return render_template('owner.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)