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
        resultado = buscadorJuegos(juego)
        schema = {
            "Nombre": resultado[0],
            "Puntuacion Metacritic": resultado[1],
            "Puntuacion Usuarios": resultado[2],
            "Fecha de lanzamiento": resultado[3],
            "Desarrolladora": resultado[4],
            "Enlace": resultado[5]
        }
        resultado[:] = []
        return jsonify(schema)

api.add_resource(buscarjuego, '/juego/<juego>')

class buscarPelicula(Resource):
    def get(self, pelicula):
        resultado = buscadorPeliculas(pelicula)
        schema = {
            "Nombre": resultado[0],
            "Puntuacion Metacritic": resultado[1],
            "Puntuacion Usuarios": resultado[2],
            "Fecha de lanzamiento": resultado[3],
            "Productora": resultado[4],
            "Enlace": resultado[5]
        }
        resultado[:] = []
        return jsonify(schema)

api.add_resource(buscarPelicula, '/pelicula/<pelicula>')

class buscarSerie(Resource):
    def get(self, serie):
        resultado = buscadorSeries(serie)
        schema = {
            "Nombre": resultado[0],
            "Puntuacion Metacritic": resultado[1],
            "Puntuacion Usuarios": resultado[2],
            "Fecha de lanzamiento": resultado[3],
            "Productora": resultado[4],
            "Enlace": resultado[5]
        }
        resultado[:] = []
        return jsonify(schema)

api.add_resource(buscarSerie, '/serie/<serie>')

class checkStatus(Resource):
    def get(self):

        schema = {
           "status": "OK"
        }

        return jsonify(schema)

api.add_resource(checkStatus, '/')

class checkStatusDocker(Resource):
    def get(self):

        schema = {
           "status": "OK"
        }

        return jsonify(schema)

api.add_resource(checkStatusDocker, '/status')


@app.route('/top20/peliculas')
def devuelveTop20Peliculas():
    lista_p = top20Peliculas()
    total = {}
    for i in range(0,20):
        schema = {
            "Nombre": lista_p[0][i],
            "Puntuacion Metacritic": lista_p[1][i],
            "Enlace": lista_p[2][i],
            "Fecha de lanzamiento": lista_p[3][i]
        }
        total[i] = schema

    return jsonify(total)

@app.route('/top20/series')
def devuelveTop20Series():
    lista_s = top20Series()
    total = {}
    for i in range(0,20):
        schema = {
            "Nombre": lista_s[0][i],
            "Puntuacion Metacritic": lista_s[1][i],
            "Enlace": lista_s[2][i],
            "Fecha de lanzamiento": lista_s[3][i]
        }
        total[i] = schema

    return jsonify(total)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
