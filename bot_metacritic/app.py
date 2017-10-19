##
from flask import Flask, request
from funciones_bot import *
import json
from funciones_top20 import *

app = Flask(__name__)

@app.route("/buscarjuego/<juego>")
def buscarjuego(juego):
    return json.dumps(buscadorJuegos(juego))

@app.route("/buscarpelicula/<pelicula>")
def buscarpelicula(pelicula):
    return json.dumps(buscadorPeliculas(pelicula))

@app.route("/buscarserie/<serie>")
def buscarserie(serie):
    return json.dumps(buscadorSeries(serie))

@app.route("/top20peliculas")
def top20peliculas():
    return json.dumps(top20Peliculas())

@app.route("/top20series")
def top20series():
    return json.dumps(top20Series())

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
