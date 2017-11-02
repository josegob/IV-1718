##
from flask import Flask, request, jsonify
from bot_metacritic.funciones_bot import *
import json
from bot_metacritic.funciones_top20 import *
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)

class buscarjuego(Resource):
    def get(self, juego):
        juego = buscadorJuegos(juego)
        schema = {
            "Nombre": juego[0],
            "Puntuacion Metacritic": juego[1],
            "Puntuacion Usuarios": juego[2],
            "Fecha de lanzamiento": juego[3],
            "Desarrolladora": juego[4],
            "Enlace": juego[5]
        }
        return jsonify(schema)

api.add_resource(buscarjuego, '/juego/<juego>')

class buscarPelicula(Resource):
    def get(self, pelicula):
        pelicula = buscadorPeliculas(pelicula)
        schema = {
            "Nombre": pelicula[0],
            "Puntuacion Metacritic": pelicula[1],
            "Puntuacion Usuarios": pelicula[2],
            "Fecha de lanzamiento": pelicula[3],
            "Productora": pelicula[4],
            "Enlace": pelicula[5]
        }
        return jsonify(schema)

api.add_resource(buscarPelicula, '/pelicula/<pelicula>')

class buscarSerie(Resource):
    def get(self, serie):
        serie = buscadorSeries(serie)
        schema = {
            "Nombre": serie[0],
            "Puntuacion Metacritic": serie[1],
            "Puntuacion Usuarios": serie[2],
            "Fecha de lanzamiento": serie[3],
            "Productora": serie[4],
            "Enlace": serie[5]
        }
        return jsonify(schema)

api.add_resource(buscarSerie, '/serie/<serie>')

class test_ruta(Resource):
    def get(self, juego):
        juego = buscadorJuegos(juego)
        schema = {"Nombre": juego[0]}

        return jsonify(schema)

api.add_resource(test_ruta, '/test_ruta/<juego>')

class checkStatus(Resource):
    def get(self):

        schema = {
           "status": "OK"
        }

        return jsonify(schema)

api.add_resource(checkStatus, '/')


@app.route('/top20/peliculas')
def devuelveTop20Peliculas():
    lista_p = top20Peliculas()
    return '{} {} {} {}'.format((lista_p[0]), (lista_p[1]), (lista_p[2]), (lista_p[3]))

@app.route('/top20/series')
def devuelveTop20Series():
    lista_s = top20Series()
    return '{} {} {} {}'.format((lista_s[0]), (lista_s[1]), (lista_s[2]), (lista_s[3]))

if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
