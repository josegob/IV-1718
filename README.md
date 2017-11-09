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


## Motivación para el uso de la Integración Continua (CI) y de los sistemas de Tests

Muchas veces nos hemos encontramos en la siguiente situacion:

Pocos días antes a la entrega de un proyecto probamos a compilar la última versión de nuestro código y nos encontramos con que no compila.

Otra situación que nos solemos encontrar es que al compilar nuestro proyecto en otra máquina distinta a la nuestra, normalmente en el entorno donde se quiere desplegar el programa, falla.
Ambas situaciones traen unos dolores de cabeza enorme.

Pero todas estas situaciones y otras similares tienen una solución sencilla: la Integración Continua. Esta práctica consiste en tener un proceso que detecta cuando hay un nuevo cambio en nuestro código, y que dichos cambios pasen por una serie de tests predefinidos. Estos sistemas de tests son programas que lo que hacen simplemente es comprobar que el código nuevo que hemos subido cumple con los requisitos que hemos establecido previamente nosotros.

La ventaja de la **Integración Continua** es que cada vez que cambiamos algo en nuestro código y lo subimos a GitHub (en este caso), tenemos un proceso que va a verificar mediante una serie de tests si la integración del nuevo código es válida.

Otra ventaja es la de que este conjunto de pruebas se realiza en un entorno limpio por lo que nos asegura que si el resultado es válido, nuesto proyecto podrá ser compilado en cualquier entorno.
