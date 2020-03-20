from myproject import app, db
from flask import render_template, redirect, url_for, request, flash
from myproject.models import HomeUsers, Admin
from myproject.forms import AddHomeUser, Login, UpdateAdmin
from utils import automation
from flask_login import login_required, login_user, logout_user, user_logged_out
from flask_login import current_user


@app.route('/')
def home():

    return render_template('home.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logout Success')
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    
    # If user is alreay logged in, redirecting him away from login page to 
    # some other page.
    if current_user.is_authenticated:
        return redirect(url_for('add_user'))

    form = Login()  

    if form.validate_on_submit():
        user = Admin.query.filter_by(username=form.username.data).first()
        if user:
            if user.username == form.username.data and user.password == form.password.data:
                login_user(user)
                return redirect(url_for('add_user'))
            else:
                flash('Wrong Username or Password!')
        else:
                flash('Wrong Username or Password!')

    return render_template('login.html', form=form)


@app.route('/add_user', methods=['GET', 'POST'])
@login_required
def add_user():

    form = AddHomeUser()

    if form.validate_on_submit():
        username = form.username.data
        devicename = form.devicename.data
        macaddress = form.macaddress.data

        user = HomeUsers(username, devicename, macaddress)
        db.session.add(user)
        db.session.commit()

        automation(macaddress)

        flash('User added!')

        return redirect(url_for('home'))
    
    return render_template('add_user.html', form=form)


@app.route('/remove_user')
@login_required
def remove_user():
    return render_template('remove_user.html')


@app.route('/list_users')
@login_required
def list_users():

    all_users = HomeUsers.query.all()

    return render_template('listusers.html', all_users=all_users)


@app.route('/settings', methods=['GET', 'POST'])
def settings():

    form = UpdateAdmin()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        if username and password:

            admin = Admin.query.filter_by(username=current_user.username).first()
            
            admin.username = username
            admin.password = password
            db.session.add(admin)
            db.session.commit()

            flash('Username and Password Changed!')

        elif username and not password:

            admin = Admin.query.filter_by(username=current_user.username).first()
            
            admin.username = username
            db.session.add(admin)
            db.session.commit()

            flash('Username Changed!')

        elif password and not username:

            admin = Admin.query.filter_by(username=current_user.username).first()
            
            admin.password = password
            db.session.add(admin)
            db.session.commit()

            flash('Password Changed')

        else:
            flash('Please, fill out username or password to change.')

    return render_template('settings.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)