import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate('db/practica9-78d87ba5af71.json')
firebase_admin.initialize_app(cred)

def connect():
    conexion = firestore.client()
    return conexion

def seleccionarBaseDeDatos():
    conexion=connect()
    db = conexion.collection('restaurants')
    return db

def buscarTodo():
    resultado = []
    restaurants = seleccionarBaseDeDatos()
    datos = restaurants.stream()
    for res in datos:
        resultado.append(res.to_dict())
    return resultado

def insertar(name, restaurant_id, borough, street, cuisine, coord0, coord1):
    restaurants = seleccionarBaseDeDatos()
    restaurants.add({
                'name' : name,
                'restaurant_id' : restaurant_id,
                'borough' : borough,
                'street' : street,
                'cuisine' : cuisine,
                'coord0' : coord0,
                'coord1' : coord1
            })
    datos = restaurants.stream()
    resultado = []
    for res in datos:
        resultado.append(res.to_dict())
    return resultado

def eliminar(name):
    restaurants = seleccionarBaseDeDatos()
    restos = restaurants.where('name', '==', name).stream()
    for restaurant in restos:
        id=restaurant.id
    restaurants.document(id).delete()

def modificar(name, campo, datoNuevo):
    restaurants = seleccionarBaseDeDatos()
    restos = restaurants.where('name', '==', name).stream()
    for rest in restos:
        id=rest.id
    res = restaurants.document(id)
    res.update({
        campo: datoNuevo
    })    
    datos = restaurants.stream()
    resultado = []
    for res in datos:
        resultado.append(res.to_dict())
    return resultado

def buscar(palabra):
    restaurants = seleccionarBaseDeDatos()
    datos = restaurants.where('cuisine', '==', palabra).stream()
    resultado = []
    for res in datos:
        resultado.append(res.to_dict())
    return resultado

