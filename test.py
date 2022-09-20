# from flask import Flask
# app = Flask(__name__)
# @app.route('/')
# def home():
#     return 'Hi Tom and Alejandro sort of figured it out'
# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def home():
    return render_template("home.html")
if __name__ == '__main__':
    app.run(debug=True)





















