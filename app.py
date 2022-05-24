from flask import Flask, render_template, jsonify

# Initialize app
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/news')
def news():
    return render_template("news.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/games')
def games():
    return render_template("games.html")

@app.route('/signup')
def signup():
    return render_template("getinvolved.html")
