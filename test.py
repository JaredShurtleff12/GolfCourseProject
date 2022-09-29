# this is how I figured out to put an html online 
# locally

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///friends.db'
#Initialize the database
db = SQLAlchemy(app)

# create db model
class Friends(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    name2 = db.Column(db.String(200), nullable=True)
#Create function to return a string
    def __repr__(self):
        return '<Name %r>' % self.id

@app.route('/')
def home():
    return render_template("index.html")
if __name__ == '__main__':
    app.run(debug=True)





















