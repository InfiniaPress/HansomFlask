from flask import Flask, render_template, request, jsonify
from hansom.database.db import DBNote, dbsess, getNote, checkNoteExists

app = Flask(__name__)

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



@app.route("/openNote", methods=["POST"])
def open():
    note.name = request.json["name"]
    #get note from DB and check if exists
    if checkNoteExists(note.name):
        note.contents = getNote(note.name)
        print(note.contents)
        return jsonify(name=note.name, contents=note.contents)


@app.route("/saveNote", methods=["POST"])
def save():
    note.name = request.json["name"]
    note.contents = request.json["contents"]
    notes = DBNote(note.name, note.contents, dbsess)
    #notes.


@app.route("/newNote", methods=["POST"])
def newNote():
    note.name = request.json["name"]
    if checkNoteExists(note.name):
        return render_template("signin.html",exists="yes")
    else:
        note.contents = getNote(note.name)
        return render_template("note.html",note=note)


if __name__ == "__main__":
    app.run()