from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "asdf"

@app.route('/')
def test():
    return render_template('home.html')

@app.route('/signup', methods=["GET", "POST"])
def signup():
    company = request.form["Company Name"]
    email = request.form["Email"]
    flash("You are a goofy foober. ", "error")

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