from flask import Blueprint, render_template

views = Blueprint('views', __name__)


@views.route('/')
def home():
    return render_template("home.html")
    
@views.route('/survey')
def survey():
    return render_template("user.html")

@views.route('/managementsignup')
def signup():
    return render_template("management.html")

@views.route('/managementlogin')
def login():
    return render_template("managementLogin.html")

@views.route('/surveypt1')
def surveypt1():
    return render_template("survey1.html")

@views.route('/surveypt2')
def surveypt2():
    return render_template("survey2.html")

@views.route('/thankyou')
def ty():
    return render_template("ty.html")