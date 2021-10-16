from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/data")
def view_data():
    return render_template('data.html') 

@app.route("/hello")
def view_hello():
    return render_template('hello.html')