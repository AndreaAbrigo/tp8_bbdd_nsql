import os
from flask import Flask, redirect, url_for, request, render_template
from pymongo import MongoClient
import urllib.request
import urllib.parse
import http.client
import json
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
from db import connect_db


app = Flask(__name__)

@app.route('/cargarDatos')
def cargarDatos():
    with open('db/restaurants.json') as file:
        data = json.load(file)
        for rest in data['restaurants']:
            resultado = connect_db.insertar(rest['name'], rest['restaurant_id'], rest['borough'], rest['address']['street'], rest['cuisine'], rest['address']['coord'][0], rest['address']['coord'][1])       
    return render_template('index.html', datos=resultado)

# @app.route('/prueba')
# def prueba():
#     resultado = connect_db.buscar("Parrilla")
#     return render_template('prueba.html', datos=resultado)

@app.route('/')
def todo():
    resultado = connect_db.buscarTodo()
    return render_template('index.html', datos=resultado)

@app.route('/agregar')
def agregar():
    return render_template("agregar.html")
    
@app.route('/altaRestaurant', methods=["POST"])
def altaRestaurant():
    if request.method == 'POST':
        name = request.form['name']
        restaurant_id = request.form['name']
        borough = request.form['borough']
        street = request.form['street']
        cuisine= request.form['cuisine']
        coord1 = request.form['coord1']
        coord0 = request.form['coord0']
    resultado = connect_db.insertar(name, restaurant_id, borough, street, cuisine, coord0, coord1)
    return render_template('index.html', datos=resultado)

@app.route('/quitar', methods=["POST"])
def quitar():
    if request.method == 'POST':
        name = request.form['name']
    return render_template('confirmarEliminacion.html', nombre=name)

@app.route('/siEliminar', methods=["POST"])
def siEliminar():
    if request.method == 'POST':
        name = request.form['name']
    resultado=connect_db.eliminar(name)
    return render_template('eliminado.html', nombre=name)

@app.route('/editar', methods=["POST"])
def editar():
    if request.method == 'POST':
        name = request.form['name']
    return render_template('editar.html', nombre=name)

@app.route('/modificar', methods=["POST"])
def modificar():
    if request.method == 'POST':
        name = request.form['name']
        nuevoName = request.form['nuevoName']
        nuevoBorough = request.form['nuevoBorough']
        nuevoStreet = request.form['nuevoStreet']
        nuevoCuisine = request.form['nuevoCuisine']
        nuevoCoord1 = request.form['nuevoCoord1']
        nuevoCoord0 = request.form['nuevoCoord0']   
    if nuevoName != "":
        campo = "name"
        resultado=connect_db.modificar(name, campo, nuevoName)
    if nuevoBorough != "":
        campo = borough
        resultado=connect_db.modificar(name, campo, nuevoBorough)
    if nuevoStreet != "":
        campo = "street"
        resultado=connect_db.modificar(name, campo, nuevoStreet)
    if nuevoCuisine != "":
        campo = "cuisine"
        resultado=connect_db.modificar(name, campo, nuevoCuisine)
    if nuevoCoord1 != "":
        campo = "coord1"
        resultado=connect_db.modificar(name, campo, nuevoCoord1)
    if nuevoCoord0 != "":
        campo = "coord0"
        resultado=connect_db.modificar(name, campo, nuevoCoord0)
    return render_template('index.html', datos=resultado)


@app.route('/buscar', methods=["POST"])
def buscar():
    if request.method == 'POST':
        palabra = request.form['palabra']
    resultado=connect_db.buscar(palabra)
    return render_template('index.html', datos=resultado)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)