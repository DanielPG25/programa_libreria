from flask import Flask, render_template, abort
import json
import sys
app = Flask(__name__)

with open('./books.json') as f:
	libreria=json.load(f)
return(datos)

@app.route('/',methods=["GET","POST"])
def inicio():
	return render_template("index.html")
	