from flask import Flask, render_template, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField, DateTimeField, SelectField,
                    RadioField, TextField, TextAreaField, SubmitField)
from wtforms.validators import DataRequired


app = Flask(__name__)

app.config['SECRET_KEY'] = 'mykey'

class InfoForm(FlaskForm):

    breed = StringField('What breed are you?', validators=[DataRequired()])
    neutered = BooleanField('Have you been neutered?')
    mood = RadioField('Please choose your mood:', 
                        choices=[('Happy', 'Happy'),
                                 ('Excited', 'Excited')])
    food_choice = SelectField('Pick your favourite food:',
                                choices=[('chi', 'Chicken'), ('bf', 'Beef'), 
                                        ('fish', 'Fish')])
    feedback = TextAreaField()
    submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def index():

    form = InfoForm()
    if form.validate_on_submit():
        # Storing the data into sessions to show them in thankyou.html page.
        session['breed'] = form.breed.data
        session['neutered'] = form.neutered.data
        session['mood'] = form.mood.data
        session['food'] = form.food_choice.data
        session['feedback'] = form.feedback.data

        return redirect(url_for('thankyou'))

    return render_template('flaskformfield.html', form=form) 

@app.route('/thankyou')
def thankyou():
    # The Session will automatically show all the data to the thankyou.html
    # page due to built-in session feature in the flask.
    return render_template('thankyou.html')


if __name__ == '__main__':
    app.run(debug=True)