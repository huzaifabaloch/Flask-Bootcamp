# forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError


class LoginForm(FlaskForm):

    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')
    

class RegistrationForm(FlaskForm):

    email = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), 
                EqualTo('confirm_password', message='Passwords must match!')])
    confirm_password = PasswordField('Confirm Password', 
                                    validators=[DataRequired()])
    submit = SubmitField('Register')

    def check_email(self, field):
        # Checking is email is already been registered.
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('This email has already been registered!')

    def check_username(self, field):
        # Checking is username is already been taken.
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username is taken!')