from flask import Flask, render_template, flash, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


app = Flask(__name__)

app.config['SECRET_KEY'] = 'tuna123'

class MyForm(FlaskForm):

    submit = SubmitField('Click Me')


@app.route('/', methods=['GET', 'POST'])
def index():

    myform = MyForm()
    if myform.validate_on_submit():
        flash('Hey tuna, how is your life going?')

        return redirect(url_for('index'))
    
    return render_template('flaskflash.html', myform=myform)


if __name__ == "__main__":   
    app.run(debug=True)
