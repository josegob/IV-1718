##
from flask import Flask, request
from bot_metacritic.funciones_bot import *
import json
from bot_metacritic.funciones_top20 import *
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)

@app.route("/")
def welcome():
    return ("API BOT")

class buscarjuego(Resource):
    def get(self, juego):
        return buscadorJuegos(juego)

api.add_resource(buscarjuego, '/juego/<juego>')

class buscarPelicula(Resource):
    def get(self, pelicula):
        return buscadorPeliculas(pelicula)

api.add_resource(buscarPelicula, '/pelicula/<pelicula>')

class buscarSerie(Resource):
    def get(self, serie):
        return buscadorSeries(serie)

api.add_resource(buscarSerie, '/serie/<serie>')

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
