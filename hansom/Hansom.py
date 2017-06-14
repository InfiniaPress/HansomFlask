from flask import Flask, render_template, request
from hansom.database.db import DBNote, dbsess, getNote, checkNoteExists

app = Flask(__name__)


app.config['MONGO_URI'] = PyMongoDB_URI

class Note:
  def __init__(self, name, contents):
    self.name = name
    self.contents = contents
    
#DBnote = DBNote("name","contents", dbsess)
note = Note("","")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("signin.html")
      
@app.route("/openNote",methods=["POST"])   
def open():
    note.name = request.json["name"]
    
    #get note from DB and check if exists
    if checkNoteExists(note.name):
      note.contents = getNote(note.name)
      return render_template("note.html",note=note)
    else:
      return render_template("signin.html",notExists="yes")
  
@app.route("/saveNote", methods=["POST"])
def save():
    note.name = request.json["name"]
    note.contents = request.json["contents"]
    notes = Note(note.name, note.contents, dbsess)
    #notes.

    
@app.route("/newNote", methods=["POST"])
def newNote():
  if checkNoteExists(note.name):
    return render_template("signin.html",exists="yes")
  else:
    note.contents = getNote(note.name)
    return render_template("note.html",note=note)