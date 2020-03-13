# forms.py file #
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired


class AddForm(FlaskForm):

    name = StringField('Name of Puppy: ', validators=[DataRequired()])
    submit = SubmitField('Add Puppy')


class DelForm(FlaskForm):

    id = IntegerField('ID number of Puppy to Remove: ', validators=[DataRequired()])
    submit = SubmitField('Remove Puppy')


class AddOwnerForm(FlaskForm):

    name = StringField('Enter Owner Name: ', validators=[DataRequired()])
    puppy_id = IntegerField('Enter Puppy ID: ', validators=[DataRequired()])
    submit = SubmitField('Add Owner')