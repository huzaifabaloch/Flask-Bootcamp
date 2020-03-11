from flask import Flask, render_template, flash, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


app = Flask(__name__)

app.config['SECRET_KEY'] = 'freddy'

class SimpleForm(FlaskForm):

    breed = StringField('What Breed are you?')
    submit = SubmitField('Save')


@app.route('/', methods=['GET', 'POST'])
def index():

    form = SimpleForm()
    if form.validate_on_submit():
        breed = form.breed.data
        flash('You just saved your breed as, {}'.format(breed))

        return redirect(url_for('index'))

    return render_template('flashexer.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)