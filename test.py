# from flask import Flask
# app = Flask(__name__)
# @app.route('/')
# def home():
#     return 'Hi Tom and Alejandro sort of figured it out'
# if __name__ == '__main__':
#     app.run(debug=True)

# this is how I figured out to put an html online 
# locally

from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def home():
    return render_template("home.html")
if __name__ == '__main__':
    app.run(debug=True)





















