from flask import Flask, render_template, request
from hansom.database.db import DBNote, dbsess, getNote

app = Flask(__name__)


app.config['MONGO_URI'] = PyMongoDB_URI

class Note:
  def __init__(self, name, contents):
    self.name = name
    self.contents = contents
    
#DBnote = DBNote("name","contents", dbsess)
note = Note("name","contents")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("main.html",note=note)
    note.name = #user input
    note.contents = getNote(note.name)
    return redirect(url_for('index'))
  
@app.route("/saveNote", methods=["POST"])
def save():
    note.name = request.json["name"]
    note.contents = request.json["contents"]
    notes = Note(note.name, note.contents)
    #notes.

    
@app.route("/newNote", methods=["POST"])
def newNote():
  if 