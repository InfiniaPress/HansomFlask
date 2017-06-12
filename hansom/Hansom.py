from flask import Flask, render_template, request
from cassandra.cluster import Cluster

from hansom.database.db import PyMongoDB_URI

app = Flask(__name__)

dbcluster = Cluster()
dbsess = dbcluster.connect()

app.config['MONGO_URI'] = PyMongoDB_URI


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("main.html")


def note():
    if request.method == "GET":
        return render_template("note.html")
