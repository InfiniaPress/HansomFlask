from flask import Flask, render_template, request, jsonify, abort
from database.db import DBNote, dbsess, getNote, checkNoteExists

app = Flask(__name__)

class Note:
    def __init__(self, name, contents):
        self.name = name
        self.contents = contents


note = Note("","")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("signin.html")


@app.route("/ajax/openNote", methods=["POST"])
def open():
    note.name = request.json["name"]

    # get note from DB and check if exists

    if checkNoteExists(note.name):
        note.contents = getNote(note.name)
        return render_template("note.html", note=note)
    else:
        return "The note does not exist!"


@app.route("/ajax/saveNote", methods=["POST"])
def save():
    note.name = request.json["name"]
    note.contents = request.json["contents"]
    notes = DBNote(note.name, note.contents, dbsess)
    notes.updateDB()
    return "Saved"


@app.route("/ajax/newNote", methods=["POST"])
def newNote():
    note.name = request.json["name"]
    note.contents = ""
    if checkNoteExists(note.name):
        return "A note with that name already exists!"
    else:
        return render_template("note.html", note=note)


if __name__ == "__main__":
    app.run()