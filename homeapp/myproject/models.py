from myproject import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return Admin.query.get(user_id)



class Admin(db.Model, UserMixin):

    __tablename__ = 'admin'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text)
    password = db.Column(db.Text)

    def __init__(self, username, password):
        self.username = username
        self.password = password



class HomeUsers(db.Model):

    __tablename__ = 'homeusers'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64))
    devicename = db.Column(db.String(64))
    macaddress = db.Column(db.String(17), unique=True, index=True)

    def __init__(self, username, devicename, macaddress):
        self.username = username
        self.devicename = devicename
        self.macaddress = macaddress

    def __repr__(self):
        return f'{self.username} {self.devicename} {self.macaddress}'
