from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def test():
    return render_template('home.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/datazone')
def datazone():
    return render_template('datazone.html')

@app.route('/datatrack')
def datatrack():
    return render_template('datatrack.html')