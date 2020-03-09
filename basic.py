from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def index():
    name = 'The world make some noisy funny faces'
    mylist = list(name)
    mydict = {'name': 'flask-web-app'}
    return render_template('basic.html', name=name, mylist=mylist,
                            mydict=mydict)


if __name__ == '__main__':
    app.run(debug=True)