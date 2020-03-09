from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def index():
    name = 'The world make some noisy funny faces'
    mylist = list(name)
    mydict = {'name': 'flask-web-app'}
    return render_template('home.html', name=name, mylist=mylist,
                            mydict=mydict)

@app.route('/puppy/<name>')
def puppy_name(name):
    return render_template('puppy.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)