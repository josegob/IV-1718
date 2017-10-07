# -*- coding: utf-8 -*-

import telebot # Librería de la API del bot.
from telebot import types # Tipos para la API del bot.
import time # Librería para hacer que el programa que controla el bot no se acabe.
from funciones_bot import *
import re

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
        bot.send_message( cid, 'Un momento, voy a buscar el juego')
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
