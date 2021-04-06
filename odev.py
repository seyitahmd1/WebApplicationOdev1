import sys
from flask import Flask,render_template,flash,redirect,url_for
from wtforms import TextAreaField,Form,StringField,PasswordField,validators
from functools import wraps
from passlib.hash import sha256_crypt

app = Flask(__name__)

@app.route('/')
def index():
   
   return render_template("index.html")

@app.route('/about')
def hakkimizda():
   return render_template("about.html")

@app.route('/cv')
def cvsayfasi():
   return render_template("cv.html")


if __name__ == "__main__":
    app.run(debug=True)