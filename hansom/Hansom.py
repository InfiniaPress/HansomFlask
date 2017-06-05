from flask import Flask, redirect, render_template, request, url_for
from hansom.hansom.database import db
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])

def index():
    if request.method == "GET":
        return render_template("main.html")
app.config["DEBUG"] = True

app.config["SQLALCHEMY_POOL_RECYCLE"] = 299


#class Note(db.Model):
#
 #   __tablename__ = "notes"
#
 #   id = db.Column(db.Integer, primary_key=True)
  #  content = db.Column(db.String(4096))
