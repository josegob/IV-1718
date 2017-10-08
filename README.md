# Proyecto Infraestrucutra Virtual

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


## Motivación para el uso de la Integración Continua (CI) y de los sistemas de Tests

Muchas veces nos hemos encontramos en la siguiente situacion:

Pocos días antes a la entrega de un proyecto probamos a compilar la última versión de nuestro código y nos encontramos con que no compila.

Otra situación que nos solemos encontrar es que al compilar nuestro proyecto en otra máquina distinta a la nuestra, normalmente en el entorno donde se quiere desplegar el programa, falla.
Ambas situaciones traen unos dolores de cabeza enorme.

Pero todas estas situaciones y otras similares tienen una solución sencilla: la Integración Continua. Esta práctica consiste en tener un proceso que detecta cuando hay un nuevo cambio en nuestro código, y que dichos cambios pasen por una serie de tests predefinidos. Estos sistemas de tests son programas que lo que hacen simplemente es comprobar que el código nuevo que hemos subido cumple con los requisitos que hemos establecido previamente nosotros.

La ventaja de la **Integración Continua** es que cada vez que cambiamos algo en nuestro código y lo subimos a GitHub (en este caso), tenemos un proceso que va a verificar mediante una serie de tests si la integración del nuevo código es válida.

Otra ventaja es la de que este conjunto de pruebas se realiza en un entorno limpio por lo que nos asegura que si el resultado es válido, nuesto proyecto podrá ser compilado en cualquier entorno.


## Despliegue en Heroku

El PaaS elegido para el despliegue ha sido Heroku. Esta elección se ha debido a la facilidad de uso así como la posibilidad de integrar una base de datos basada en Postgres. Además de lo anterior Heroku nos permite alojar nuestra aplicación de forma gratuita aunque eso si, con algunas limitaciones.
Asimismo la gran documentación que posee Heroku y su interfaz han hecho que junto con lo mencionado anteriormente me decante por este servicio.

Para el despliegue de nuestra aplicación en Heroku necesitaremos hacer uso de varios ficheros. El primero sera el archivo **Procfile** que debe situarse en el directorio raíz del proyecto. Dicho fichero contendrá el comando necesario para ejecutar el bot una vez haya pasado el test de Integración Continua. El contenido del fichero será el siguiente:

~~~
worker: python3 bot_metacritic/bot_metacritic.py
~~~

El segundo fichero será el **runtime.txt** que contendrá la versión de python que se usará para ejecutar nuestro programa. El contenido del fichero será el siguiente:

~~~
python-3.5.2
~~~

Posteriormente necesitaremos crear la aplicación en Heroku y para ello ejecutaremos desde la terminal el comando `heroku create --region eu -a 'nombre de la app'` y el comando `heroku addons:create heroku-postgresql:hobby-basic -a 'nombre de la app'` para crear una base de datos para la app. A continuación entramos en nuestro dashboard de Heroku y enlazamos la aplicacion con nuestro repositorio de GitHub donde se encuentra el bot.
Asimismo configuramos las variables de entorno `DATABASE_URL` y `token_bot` desde la pestaña de ajustes.

Por último debemos activar la opción de despliegue automático en Heroku una vez que haya pasado los tests de Integración Continua. Dicha tarea se realiza desde la pestaña `Deploy`

En esta imagen podemos ver como la base de datos se ha creado correctamente y le hemos metido alguna información.

![base de datos](https://raw.githubusercontent.com/josegob/IV-Proyecto/gh-pages/assets/db_heroku.png)

Variables de entorno añadidas a nuestra aplicación.

![variables entorno](https://raw.githubusercontent.com/josegob/IV-Proyecto/gh-pages/assets/Vars_entorno.png)

Podemos comprobar que nuestra app esta enlazada correctamente con nuestro repositorio

![enlace GitHub](https://raw.githubusercontent.com/josegob/IV-Proyecto/gh-pages/assets/App_enlazada.png)

Y el despliegue automático está activado

![despliegue auto](https://raw.githubusercontent.com/josegob/IV-Proyecto/gh-pages/assets/Despliegue_auto.png)

Por último cuando nuestra aplicación pase los tests unitarios se desplegara automáticamente
![dashboard heroku](https://raw.githubusercontent.com/josegob/IV-Proyecto/gh-pages/assets/dashboard_heroku.png)

Una vez desplegado el bot podremos probarlo desde Telegram buscando el bot por el nombre @MetaClippy_bot y ver los logs mediante el comando `heroku logs --tails -a 'nombre de la app'` desde nuestra terminal.

El enlace al despliegue de nuestra aplicación es el [siguiente](https://bot-metacritic.herokuapp.com/ "siguiente")

Sin embargo  al tratarse de una aplicación que se aloja en Telegram y no muestra nada por pantalla nos dará un error al intentar acceder a ella.
