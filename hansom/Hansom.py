from flask import Flask, render_template, request

app = Flask(__name__)


app.config['MONGO_URI'] = PyMongoDB_URI

class Note:
  def __init__(self, name, contents):
    self.name = name
    self.contents = contents
    
note = Note("","")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("main.html")
    note.name = 
    note.contents = 
    return redirect(url_for('index'))
  
@app.route("/saveNote", methods=["POST"])
def save():
    note.name = request.json["name"]
    note.contents = request.json["contents"]
    

