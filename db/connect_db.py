from pymongo import MongoClient
import os

def connect():
    conexion = MongoClient(
    os.environ['DB_PORT_27017_TCP_ADDR'],
    27017)
    return conexion

def seleccionarBaseDeDatos():
    conexion=connect()
    db = conexion.lugares
    return db

def buscarTodo():
    db = seleccionarBaseDeDatos()
    collection = db.restaurants
    resultado=collection.find()
    return resultado

def insertar(name, restaurant_id, borough, street, cuisine, coord0, coord1):
    db = seleccionarBaseDeDatos()
    collection = db.restaurants
    collection.insert({
                "name" : name,
                "restaurant_id" : restaurant_id,
                "borough" : borough,
                "street" : street,
                "cuisine" : cuisine,
                "coord0" : coord0,
                "coord1" : coord1
            })
    resultado=collection.find()
    return resultado

def eliminar(name):
    db = seleccionarBaseDeDatos()
    collection = db.restaurants
    collection.remove({'name':name})

def modificar(name, campo, datoNuevo):
    db = seleccionarBaseDeDatos()
    collection = db.restaurants
    collection.update({'name':name},{'$set':{campo:datoNuevo}})
    resultado=collection.find()
    return resultado

def buscar(palabra):
    db = seleccionarBaseDeDatos()
    collection = db.restaurants
    resultado=collection.find({'cuisine':{'$regex':palabra}})
    return resultado
