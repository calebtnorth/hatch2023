from flask import Flask, render_template, flash, redirect, request, url_for, make_response
from app import *
from os import listdir
from random import randint

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
                return login()
            else:
                status = "That username already exists."

    return render_template('signup.html', status=status)

@app.route('/login', methods=["GET", "POST"])
def login():
    status = ""
    if request.method == "POST":
        query_result = db.login(
            request.form["Name"], 
            request.form["Password"],
            str(request.remote_addr),
        )
        print(query_result)
        if query_result or request.cookies["account"] == request.form["Name"]:
            res = make_response(redirect("datazone"))
            res.set_cookie("account", request.form["Name"], 60 * 15)
            res.set_cookie("redirect", "true", 15)
            return res
        else:
            status = "An error occured. Try a different username."
    return render_template('login.html', status=status)

@app.route('/datazone', methods=["GET", "POST"])
def datazone():
    file_data=[]
    for file in listdir("genomes"):
        d=randint(1,29)
        m=randint(1,13)
        y=randint(2017,2022)
        file_data.append([file, f"{m}/{d}/{y}"])
    return render_template('datazone.html', username="Caleb North", file_data = file_data)

@app.route('/datatrack')
def datatrack():
    return render_template('datatrack.html')