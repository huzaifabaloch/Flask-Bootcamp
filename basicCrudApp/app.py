from flask import Flask, render_template, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc
from datetime import datetime



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Grocery(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())

    def __repr__(self):
        return '<Grocery %r>' % self.name



@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':
        name = request.form['name']

        new_item = Grocery(name=name)
        
        try:
            db.session.add(new_item)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was a problem adding new item!'

    else:
        groceries = Grocery.query.order_by(desc(Grocery.id)).all()
        return render_template('index.html', groceries=groceries)


@app.route('/delete/<int:id>')
def delete(id):

    item = Grocery.query.get_or_404(id)

    try:
        db.session.delete(item)
        db.session.commit()
        return redirect('/')
    except:
        return 'There was a problem deleting item!'



@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):

    item = Grocery.query.get_or_404(id)

    if request.method == 'POST':
        new_item = request.form['name']
        item.name = new_item
        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'There was a problem updating item!'
    
    else:
        return render_template('update.html', item=item)
    




if __name__ == '__main__':
    app.run(debug=True, port=5434)