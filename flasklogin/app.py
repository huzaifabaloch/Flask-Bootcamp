# app.py
from myproject import app, db
from flask import render_template, redirect, request, url_for, flash, abort
from flask_login import login_user, login_required, logout_user
from myproject.models import User
from myproject.forms import LoginForm, RegistrationForm


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/welcome')
@login_required  # In order for user to see this view, they must be logged in.
def welcome_user():
    return render_template('welcome_user.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logout Success!')
    return redirect(url_for('home'))


@app.route('/login', methods=['GET', 'POST'])
def login():

    form = LoginForm()
    
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        user = User.query.filter_by(email=email).first()

        if user.check_password(password) and user is not None:
            login_user(user)
            flash('Login Success!')

            """
                if a user trying to visit a page that requires login, we can
                save that as 'next'. for instance, if a user trying to access
                the welcome_user page and login was reuired, Flask saves that
                actual request for that page as next. we grabbing it from
                request. and redirecting to that page.
            """
            next = request.args.get('next')

            if next == None or not next[0] == '/':
                next = url_for('welcome_user')

            return redirect(next)

    return render_template('login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():

    form = RegistrationForm()

    if form.validate_on_submit():
        user = User(email=form.email.data, username=form.username.data,
                    password=form.password.data)

        db.session.add(user)
        db.session.commit()
        flash('Thank you for registration!')
        return redirect(url_for('login'))
    
    return render_template('register.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
