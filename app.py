from flask import Flask, render_template, abort
import json
import sys
import os
app = Flask(__name__)

with open('./books.json') as f:
	libreria=json.load(f)


@app.route('/',methods=["GET","POST"])
def inicio():
	return render_template("index.html",libreria=libreria)




port=os.environ["PORT"]
app.run('0.0.0.0',int(port), debug=True)
	