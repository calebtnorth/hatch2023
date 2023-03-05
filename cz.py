from flask import Flask, render_template, flash, redirect, request, url_for, make_response
from app import *

app = Flask(__name__)

@app.route('/')
def test():
    return render_template('home.html')

@app.route('/signup', methods=["GET", "POST"])
def signup():
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
                login()
            else:
                status = "An error occured. Try a different username."

    return render_template('signup.html', status=status)

@app.route('/login')
def login():
    status = ""
    if request.method == "POST":
        query_result = login(
            request.form["Name"], 
            request.form["Password"],
            str(request.remote_addr),
        )
        if query_result or request.get_cookie("account") == request.form["Name"]:
            res = make_response(redirect("datazone"))
            res.set_cookie("account", request.form["Name"], 60 * 15)
            res.set_cookie("redirect", "true", 15)
        else:
            status = "An error occured. Try a different username."
    return render_template('login.html', status=status)

@app.route('/datazone')
def datazone():

    return render_template('datazone.html')

@app.route('/datatrack')
def datatrack():
    return render_template('datatrack.html')