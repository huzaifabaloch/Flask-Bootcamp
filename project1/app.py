from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/report')
def report():
    user_name = request.args.get('username')
    upper = 0
    lower = 0
    digit = 0

    for u in user_name:
        if u.isdigit():
            digit += 1
        elif u == u.upper():
            upper += 1
        elif u == u.lower():
            lower += 1
    
    return render_template('report.html', upper=upper, lower=lower,
                             digit=digit)

 
if __name__ == '__main__':
    app.run(debug=True)