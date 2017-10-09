# -*- coding: utf-8 -*-

import telebot # Librería de la API del bot.
from telebot import types # Tipos para la API del bot.
import time # Librería para hacer que el programa que controla el bot no se acabe.
from funciones_bot import *
import re
import os
from funciones_top20 import *


bot = telebot.TeleBot(os.environ["token_bot"]) # Creamos el objeto de nuestro bot.

def listener(messages):
    for m in messages:
        if m.content_type == 'text': # Filtramos mensajes que sean tipo texto.
            cid = m.chat.id # Almacenaremos el ID de la conversación.
            print ("[" + str(cid) + "]: " + m.text)
            # Y haremos que imprima algo parecido a esto -> [42133876]: /start

bot.set_update_listener(listener)
# Así, le decimos al bot que utilice como función escuchadora nuestra función 'listener'
#declarada arriba.

@bot.message_handler(commands=['buscarjuego'])
def command_buscarjuego(m):
    resultado_busqueda = []
    cid = m.chat.id
    juego_busqueda = m.text
    juego_busqueda = re.sub(r'\s+', ' ', juego_busqueda)
    juego_busqueda = juego_busqueda[13:]
    if (juego_busqueda == ''):
        bot.send_message(cid, 'Debes especificar el nombre del juego junto al comando')
    else:
        bot.send_message(cid, 'Un momento, voy a buscar el juego')
        resultado_busqueda = buscadorJuegos(juego_busqueda)
        if (resultado_busqueda == -1):
            bot.send_message(cid, 'Illo lo siento. El juego introducido no se encuentra en la base de datos de Metacritic')


        else:
            bot.send_message(cid, 'Nombre del juego: ' + resultado_busqueda[0])
            bot.send_message(cid, 'Nota Metacritic: ' + resultado_busqueda[1])
            bot.send_message(cid, 'Nota media usuarios: ' + resultado_busqueda[2])
            bot.send_message(cid, 'Fecha de lanzamiento: ' + resultado_busqueda[3])
            bot.send_message(cid, 'Desarrolladora: ' + resultado_busqueda[4])
            bot.send_message(cid, 'Enlace: ' + resultado_busqueda[5])
            resultado_busqueda[:] = []


@bot.message_handler(commands=['buscarserie'])
def command_buscarserie(m):
    resultado_busqueda_serie = []
    cid = m.chat.id
    serie_busqueda = m.text
    serie_busqueda = re.sub(r'\s+', ' ', serie_busqueda)
    serie_busqueda = serie_busqueda[13:]
    if (serie_busqueda == ''):
        bot.send_message(cid, 'Debes especificar el nombre de la serie junto al comando')
    else:
        bot.send_message(cid, 'Un momento, voy a buscar la serie')
        resultado_busqueda_serie = buscadorSeries(serie_busqueda)
        if (resultado_busqueda_serie == -1):
            bot.send_message(cid, 'Illo lo siento. La serie introducida no se encuentra en la base de datos de Metacritic')

        else:
            bot.send_message(cid, 'Nombre de la serie: ' + resultado_busqueda_serie[0])
            bot.send_message(cid, 'Nota Metacritic: ' + resultado_busqueda_serie[1])
            bot.send_message(cid, 'Nota media usuarios: ' + resultado_busqueda_serie[2])
            bot.send_message(cid, 'Fecha de lanzamiento: ' + resultado_busqueda_serie[3])
            bot.send_message(cid, 'Productora: ' + resultado_busqueda_serie[4])
            bot.send_message(cid, 'Enlace: ' + resultado_busqueda_serie[5])
            resultado_busqueda_serie[:] = []


@bot.message_handler(commands=['buscarpelicula'])
def command_buscarpelicula(m):
    resultado_busqueda_pelicula = []
    cid = m.chat.id
    pelicula_busqueda = m.text
    pelicula_busqueda = re.sub(r'\s+', ' ', pelicula_busqueda)
    pelicula_busqueda = pelicula_busqueda[16:]
    if (pelicula_busqueda == ''):
        bot.send_message(cid, 'Debes especificar el nombre de la pelicula junto al comando')
    else:
        bot.send_message(cid, 'Un momento, voy a buscar la pelicula')
        resultado_busqueda_pelicula = buscadorPeliculas(pelicula_busqueda)
        if (resultado_busqueda_pelicula == -1):
            bot.send_message(cid, 'Illo lo siento. La serie introducida no se encuentra en la base de datos de Metacritic')

        else:
            bot.send_message(cid, 'Nombre de la pelicula: ' + resultado_busqueda_pelicula[0])
            bot.send_message(cid, 'Nota Metacritic: ' + resultado_busqueda_pelicula[1])
            bot.send_message(cid, 'Nota media usuarios: ' + resultado_busqueda_pelicula[2])
            bot.send_message(cid, 'Fecha de lanzamiento: ' + resultado_busqueda_pelicula[3])
            bot.send_message(cid, 'Productora: ' + resultado_busqueda_pelicula[4])
            bot.send_message(cid, 'Enlace: ' + resultado_busqueda_pelicula[5])
            resultado_busqueda_pelicula[:] = []


@bot.message_handler(commands=['top20series'])
def command_top20series(m):
    cid = m.chat.id
    bot.send_message(cid, 'Un momento, te paso el top20 de las series del momento')
    resultado_top20series = []
    resultado_top20series = top20Series()
    for i in range(0,20):
        bot.send_message(cid, '''Numero #{}
                                \nNombre de la serie: {}
                                \nPuntuacion de la serie: {}
                                \nEnlace de la serie: {}
                                \nFecha de lanamiento: {}'''
                                .format(i,resultado_top20series[0][i],resultado_top20series[1][i],
                                resultado_top20series[2][i], resultado_top20series[3][i]))

    del resultado_top20series

@bot.message_handler(commands=['top20peliculas'])
def command_top20peliculas(m):
    cid = m.chat.id
    bot.send_message(cid, 'Un momento, te paso el top20 de las peliculas del momento')
    resultado_top20peliculas = []
    resultado_top20peliculas = top20Peliculas()
    for i in range(0,20):
        bot.send_message(cid, '''Numero #{}
                                \nNombre de la pelicula: {}
                                \nPuntuacion de la pelicula: {}
                                \nEnlace de la pelicula: {}
                                \nFecha de lanamiento: {}'''
                                .format(i,resultado_top20peliculas[0][i],resultado_top20peliculas[1][i],
                                resultado_top20peliculas[2][i], resultado_top20peliculas[3][i]))

    del resultado_top20peliculas

@bot.message_handler(commands=['help', 'ayuda'])
def command_help(m):
    cid = m.chat.id
    mensaje = '''\n/buscarjuego 'nombre del juego'
    \n/buscarserie 'nombre de serie\n\n/buscarpelicula 'nombre de pelicula'
    \nLos comandos /top20peliculas y /top20series no necesitan informacion adicional"'''

    bot.send_message(cid,mensaje)

@bot.message_handler(commands=['start'])
def command_help(m):
    cid = m.chat.id
    mensaje = '''
    \nComandos disponibles:
    \n/buscarjuego\n\n/buscarserie\n\n/buscarpelicula\n\n/top20peliculas\n\n/top20series'''

    bot.send_message(cid,mensaje)

@bot.message_handler(commands=['contacto'])
def command_contacto(m):
    cid = m.chat.id
    mensaje="Para cualquier duda, problema o sugerencia.\nEmail: jose.gob@gmail.com"
    bot.send_message(cid,mensaje)



bot.polling(none_stop=True)
# Con esto, le decimos al bot que siga funcionando incluso si encuentra algún fallo.
