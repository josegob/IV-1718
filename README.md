[![Build Status](https://travis-ci.org/josegob/IV-Proyecto.svg?branch=master)](https://travis-ci.org/josegob/IV-Proyecto)
[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/josegob/IV-Proyecto)
# Proyecto Infraestructura Virtual

El proyecto que vamos a realizar consiste en un Bot de Telegram con el cual podremos consultar las valoraciones tanto de los usuarios como de los medios especializados y otros datos como la fecha de lanzamiento o la productora/desarrolladora de juegos, películas y series. Dicha información la obtendremos de la página [Metacritic](http://www.metacritic.com/)

Asimismo el bot contará con una base de datos para mostrar el top 20 de las películas, series y juegos actuales.

Para realizar este proyecto haremos uso de las siguientes herramientas:

- Lenguaje de programación Python, que será la 	base de nuestro proyecto
- pyTelegramBotAPI será la API que utilizaremos para desarrollar nuestro Bot
- Libreria requests para obtener la informacion del sitio
- La libreria BeautifulSoup para analizar el documento HTML obtenido con la libreria requests
- La libreria re para tratar las expresiones regulares que podamos encontrar en el documento HTML
- Un servicio en la nube como Amazon Web Services (AWS)

El Bot podrá ser modificado en el futuro con el objetivo de añadir alguna característica adicional.

Toda la documentación referente a su desarrollo, así como la de las API's que vamos a usar pueden ser consultadas en los enlaces inferiores.

[Documentación del proyecto](https://josegob.github.io/IV-Proyecto/)

[Documentación pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI#pytelegrambotapi)

[Documentación psycopg2](http://initd.org/psycopg/docs/)

[API BOT](https://bot-metacritic-api.herokuapp.com/check_status)

## Requisitos
* pyTelegramBotAPI
* Libreria requests, BeautifulSoup, re y psycopg2 para la base de datos

~~~
1. pip3 install pyTelegramBotAPI
2. pip3 install beautifulsoup4
3. pip3 install psycopg2
~~~

Las librerías **requests** y **re** vienen por defecto con Python por lo que no es necesario hacer nada.
