from flask import Flask, render_template
from flask_wtf import FlaskForm # For creating our own forms
from wtforms import StringField, SubmitField  # Allow us to use fields like string, submit and others in our form


app = Flask(__name__)

# It generates a CSRF Token/key built-in the flask. 
app.config['SECRET_KEY'] = 'mysecretkey'

class InfoForm(FlaskForm):

    # String field with label 
    breed = StringField('What breed are you?')
    # Submit field to submit form
    submit = SubmitField('Submit')


# Get and Post methods for passing the form to html template.
@app.route('/', methods=['GET', 'POST'])
def index():

    breed = False

    form = InfoForm()
    
    # if submit is validated
    if form.validate_on_submit():
        breed = form.breed.data  # Getting breed data 
        form.breed.data = ''     # Clear field
    
    return render_template('flaskform.html', form=form, breed=breed)


if __name__ == '__main__':
    app.run(debug=True)