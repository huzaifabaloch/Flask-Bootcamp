from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired
from wtforms.validators import ValidationError


class AddHomeUser(FlaskForm):

    username = StringField('Username', validators=[DataRequired()])
    devicename = StringField('Device Name', validators=[DataRequired()])
    macaddress = StringField('MAC Address', validators=[DataRequired()])
    submit = SubmitField('Add User')


class Login(FlaskForm):

    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


class UpdateAdmin(FlaskForm):

    username = StringField('Username')
    password = PasswordField('Password')
    submit = SubmitField('Save Changes')
