from flask import Flask, redirect, render_template, request, url_for
from flask.ext.sqlalchemy import SQLAlchemy
app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("main.html")
app.config["DEBUG"] = True

SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username="Hundotte",
    password="Supercat3.14",
    hostname="Hundotte.mysql.pythonanywhere-services.com",
    databasename="Hundotte$Comments",
)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
db = SQLAlchemy(app)

class Note(db.Model):

    __tablename__ = "notes"

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(4096))
