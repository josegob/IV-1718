# -*- coding: utf-8 -*-

import telebot # Librería de la API del bot.
from telebot import types # Tipos para la API del bot.
import time # Librería para hacer que el programa que controla el bot no se acabe.
from funciones_bot import *
import re
import os
import json
import requests





bot = telebot.TeleBot("469787221:AAEXeK_j3K15F8dZoOnmB9al4lQTO8xEo1E") # Creamos el objeto de nuestro bot.

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
    cid = m.chat.id
    juego_busqueda = m.text
    juego_busqueda = re.sub(r'\s+', ' ', juego_busqueda)
    juego_busqueda = juego_busqueda[13:]
    if (juego_busqueda == ''):
        bot.send_message(cid, 'Debes especificar el nombre del juego junto al comando')
    else:
        bot.send_message(cid, 'Un momento, voy a buscar el juego')
        api_url_base = 'http://127.0.0.1:8000/juego/'
        api_url_base += juego_busqueda
        response = requests.get(api_url_base)
        if (response.status_code != 200):
            bot.send_message(cid, 'Illo lo siento. El juego introducido no se encuentra en la base de datos de Metacritic')
        else:
            data = response.json()
            bot.send_message(cid, 'Nombre del juego: ' + data["Nombre"])
            bot.send_message(cid, 'Nota Metacritic: ' + data["Puntuacion Metacritic"])
            bot.send_message(cid, 'Nota media usuarios: ' + data["Puntuacion Usuarios"])
            bot.send_message(cid, 'Fecha de lanzamiento: ' + data["Fecha de lanzamiento"])
            bot.send_message(cid, 'Desarrolladora: ' + data["Desarrolladora"])
            bot.send_message(cid, 'Enlace: ' + data["Enlace"])


@bot.message_handler(commands=['buscarserie'])
def command_buscarserie(m):
    cid = m.chat.id
    serie_busqueda = m.text
    serie_busqueda = re.sub(r'\s+', ' ', serie_busqueda)
    serie_busqueda = serie_busqueda[13:]
    if (serie_busqueda == ''):
        bot.send_message(cid, 'Debes especificar el nombre de la serie junto al comando')
    else:
        bot.send_message(cid, 'Un momento, voy a buscar la serie')
        api_url_base = 'http://127.0.0.1:8000/serie/'
        api_url_base += serie_busqueda
        response = requests.get(api_url_base)
        if (response.status_code != 200):
            bot.send_message(cid, 'Illo lo siento. La serie introducida no se encuentra en la base de datos de Metacritic')

        else:
            data = response.json()
            bot.send_message(cid, 'Nombre de la serie: ' + data["Nombre"])
            bot.send_message(cid, 'Nota Metacritic: ' + data["Puntuacion Metacritic"])
            bot.send_message(cid, 'Nota media usuarios: ' + data["Puntuacion Usuarios"])
            bot.send_message(cid, 'Fecha de lanzamiento: ' + data["Fecha de lanzamiento"])
            bot.send_message(cid, 'Productora: ' + data["Productora"])
            bot.send_message(cid, 'Enlace: ' + data["Enlace"])


@bot.message_handler(commands=['buscarpelicula'])
def command_buscarpelicula(m):
    cid = m.chat.id
    pelicula_busqueda = m.text
    pelicula_busqueda = re.sub(r'\s+', ' ', pelicula_busqueda)
    pelicula_busqueda = pelicula_busqueda[16:]
    if (pelicula_busqueda == ''):
        bot.send_message(cid, 'Debes especificar el nombre de la pelicula junto al comando')
    else:
        bot.send_message(cid, 'Un momento, voy a buscar la pelicula')
        api_url_base = 'http://127.0.0.1:8000/pelicula/'
        api_url_base += pelicula_busqueda
        response = requests.get(api_url_base)
        if (response.status_code != 200):
            bot.send_message(cid, 'Illo lo siento. La pelicula introducida no se encuentra en la base de datos de Metacritic')

        else:
            data = response.json()
            bot.send_message(cid, 'Nombre de la pelicula: ' + data["Nombre"])
            bot.send_message(cid, 'Nota Metacritic: ' + data["Puntuacion Metacritic"])
            bot.send_message(cid, 'Nota media usuarios: ' + data["Puntuacion Usuarios"])
            bot.send_message(cid, 'Fecha de lanzamiento: ' + data["Fecha de lanzamiento"])
            bot.send_message(cid, 'Productora: ' + data["Productora"])
            bot.send_message(cid, 'Enlace: ' + data["Enlace"])


@bot.message_handler(commands=['top20series'])
def command_top20series(m):
    cid = m.chat.id
    bot.send_message(cid, 'Un momento, te paso el top20 de las series del momento')
    api_url_base = 'http://127.0.0.1:8000/top20/series' #Cambiar por la URL de la API desplegada
    response = requests.get(api_url_base)
    data = response.json()
    for i in range(0,20):
        bot.send_message(cid, 'Numero #{}'.format(i))
        bot.send_message(cid, 'Nombre de la series: ' + data['{}'.format(i)]["Nombre"])
        bot.send_message(cid, 'Nota Metacritic: ' + data['{}'.format(i)]["Puntuacion Metacritic"])
        bot.send_message(cid, 'Fecha de lanzamiento: ' + data['{}'.format(i)]["Fecha de lanzamiento"])
        bot.send_message(cid, 'Enlace: ' + data['{}'.format(i)]["Enlace"])

@bot.message_handler(commands=['top20peliculas'])
def command_top20peliculas(m):
    cid = m.chat.id
    bot.send_message(cid, 'Un momento, te paso el top20 de las peliculas del momento')
    api_url_base = 'http://127.0.0.1:8000/top20/peliculas' #Cambiar por la URL de la API desplegada
    response = requests.get(api_url_base)
    data = response.json()
    for i in range(0,20):
        bot.send_message(cid, 'Numero #{}'.format(i))
        bot.send_message(cid, 'Nombre de la pelicula: ' + data['{}'.format(i)]["Nombre"])
        bot.send_message(cid, 'Nota Metacritic: ' + data['{}'.format(i)]["Puntuacion Metacritic"])
        bot.send_message(cid, 'Fecha de lanzamiento: ' + data['{}'.format(i)]["Fecha de lanzamiento"])
        bot.send_message(cid, 'Enlace: ' + data['{}'.format(i)]["Enlace"])


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
