from flask import Flask, render_template, request
from flask_pymongo import PyMongo

from hansom.database.db import PyMongoDB_URI

app = Flask(__name__)
database = PyMongo(app)

app.config['MONGO_URI'] = PyMongoDB_URI



@app.route("/", methods=["GET", "POST"])

def index():
    if request.method == "GET":
        return render_template("main.html")



