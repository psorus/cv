from flask import Flask
app = Flask(__name__)

# from gohtml import *
from smartml import *
from helper import *

@app.route('/')
def index():
  return texmodify(smartml("index"))
  from content import q
  return texmodify(visualise(q,"test1"))


@app.route('/tex/<what>')
def tex(what):
  # return "routing"+what
  return texmodify(texload(what))
  
@app.route('/s/<what>')
def smart(what):
  # return "routing"+what
  return texmodify(smartml(what))
  

