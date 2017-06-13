from flask import Flask, render_template, request
from cassandra.cluster import Cluster



app = Flask(__name__)


app.config['MONGO_URI'] = PyMongoDB_URI


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("main.html")
    note.name = request.form["noteName"]
    note.contents = request.form["noteContents"]
    return redirect(url_for('index'))

