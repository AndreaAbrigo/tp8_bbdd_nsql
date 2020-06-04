import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate('practica9-78d87ba5af71.json')
firebase_admin.initialize_app(cred)

db = firestore.client()


## INSERCION DE DOCUMENTOS
# peliculas = db.collection('peliculas')
# peliculas.add({'title': 'Superman', 'protagonista': "Clark Kent"})
# peliculas.add({'title': 'Spiderman', 'protagonista': "Peter Parker"})
# peliculas.add({'title': 'El increible Hulk', 'protagonista': "Bruce Banner"})
# peliculas.add({'title': 'Capitan America', 'protagonista': "Steve Rogers"})
# peliculas.add({'title': 'Deadpool', 'protagonista': "Wade Wilson"})
# peliculas.add({'title': 'Capitana Marvel', 'protagonista': "Carol Danvers"})


## LECTURA DE DOCUMENTOS
peliculas = db.collection('peliculas')
docs = peliculas.stream()
for doc in docs:
    print(doc.to_dict())
  

## MODIFICACION DE DOCUMENTOS
# pelicula = db.collection('peliculas').document('4spgaBg8834tczC45ync')
# pelicula.update({
#     'title': 'Super Man'
# })


## ELIMINACION DE DOCUMENTOS
# db.collection('peliculas').document('4spgaBg8834tczC45ync').delete()


## CONSULTA DE DOCUMENTOS
# pelicula = db.collection('peliculas').document('tVvXgsmKuBKXwjzuzeIz')
# datos = pelicula.get()
# print(datos.to_dict())

## BUSQUEDA DE DOCUMENTOS
# peliculas = db.collection('peliculas').where('title', '==', 'Deadpool').stream()
# for pelicula in peliculas:
#     print(pelicula.to_dict())
