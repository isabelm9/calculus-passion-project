from flask import Flask, render_template, jsonify

# Initialize app
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/0')
def news():
    return render_template("news.html")
