## Motivación para el uso de la Integración Continua (CI) y de los sistemas de Tests

Muchas veces nos hemos encontramos en la siguiente situacion:

Pocos días antes a la entrega de un proyecto probamos a compilar la última versión de nuestro código y nos encontramos con que no compila.

Otra situación que nos solemos encontrar es que al compilar nuestro proyecto en otra máquina distinta a la nuestra, normalmente en el entorno donde se quiere desplegar el programa, falla.
Ambas situaciones traen unos dolores de cabeza enorme.

Pero todas estas situaciones y otras similares tienen una solución sencilla: la Integración Continua. Esta práctica consiste en tener un proceso que detecta cuando hay un nuevo cambio en nuestro código, y que dichos cambios pasen por una serie de tests predefinidos. Estos sistemas de tests son programas que lo que hacen simplemente es comprobar que el código nuevo que hemos subido cumple con los requisitos que hemos establecido previamente nosotros.

La ventaja de la **Integración Continua** es que cada vez que cambiamos algo en nuestro código y lo subimos a GitHub (en este caso), tenemos un proceso que va a verificar mediante una serie de tests si la integración del nuevo código es válida.

Otra ventaja es la de que este conjunto de pruebas se realiza en un entorno limpio por lo que nos asegura que si el resultado es válido, nuesto proyecto podrá ser compilado en cualquier entorno.
