from flask import Flask 


app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Welcome to Puppy Palace, Goto /puppy_latin/name to see your name in puppy latin!</h1>'

@app.route('/information')
def information():
    return '<b>I AM BOLD</b>'

@app.route('/user/<name>')
def profile(name):
    return '<h1>Hello {}</h1>'.format(name.title())

@app.route('/puppy_latin/<name>')
def puppy_latin(name):
    if name[-1] == 'y':
        return '<h2>Hello {}, your puppy latin name is {}</h2>'.format(name, name.replace(name[-1], 'iful'))
    else:
        return '<h2>Hello {}, your puppy latin name is {}</h2>'.format(name, name+'y')

if __name__ == '__main__':
    app.run(debug=True)