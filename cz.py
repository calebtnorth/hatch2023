from flask import Flask, render_template, flash, redirect, request, url_for
from app import *

app = Flask(__name__)

@app.route('/')
def test():
    return render_template('home.html')

@app.route('/signup', methods=["GET", "POST"])
def signup():
    print(url_for("datazone"))
    status = ""
    if request.method == "POST":
        if request.form["Password"] !=  request.form["Confirm"]:
            status = "Passwords must match"
        else:
            query_result = create(
                request.form["Name"], 
                request.form["Email"],
                request.form["Password"],
                str(request.remote_addr),
                request.form["file"]
            )
            if query_result:
                print("redireft")
                return redirect("datazone")
            else:
                status = "An error occured. Try a different username."


    return render_template('signup.html', status=status)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/datazone')
def datazone():
    return render_template('datazone.html')

@app.route('/datatrack')
def datatrack():
    return render_template('datatrack.html')