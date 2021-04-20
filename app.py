from flask import Flask, render_template, abort
import json
import sys
import os
app = Flask(__name__)

with open('./books.json') as f:
	libreria=json.load(f)


@app.route('',methods=["GET","POST"])
def inicio():
	return render_template("index.html",libreria=libreria)

@app.route('/libro/<isbn>',methods=["GET","POST"])
def libros(isbn):
	ind=True
	dicc={}
	for i in libreria:
		if i.get('isbn')==isbn:
			dicc['titulo']=i.get('title')
			dicc['imagen']=i.get('thumbnailUrl')
			dicc['numpag']=i.get('pageCount')
			dicc['descrl']=i.get('longDescription')
			dicc['descrc']=i.get('shortDescription')
			dicc['autor']=i.get('authors')
			dicc['categoria']=i.get('categories') 
			dicc['estado']=i.get('status')
			ind=False
	if ind:
		abort(404)
	return render_template("libros.html",dicc=dicc)

@app.route('/categoria/<categoria>',methods=["GET","POST"])
def categorias(categoria):
	lista=[]
	for i in libreria:
		if categoria in i.get('categories'):
			dicc2={}
			dicc2['titulo']=i.get('title')
			dicc2['isbn']=i.get('isbn')
			lista.append(dicc2)
	return render_template("categorias.html",categoria=categoria,lista=lista)	

port=os.environ["PORT"]
app.run('0.0.0.0',int(port), debug=True)
	