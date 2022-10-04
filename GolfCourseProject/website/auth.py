from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)

@auth.route('/survey')
def survey():
    return render_template("user.html")

@auth.route('/home')
def home():
    return render_template("home.html")
