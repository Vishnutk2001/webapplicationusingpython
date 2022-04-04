
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template("welcome.html")

@app.route('/contact')
def Contact_page():
    return render_template("contact.html")

@app.route('/home')
def Home_page():
    return "home page"

@app.route('/gallery')
def Gallery_page():
    return "gallery page"

if __name__== "__main__":
    app.run()