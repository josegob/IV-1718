[![Build Status](https://travis-ci.org/josegob/IV-Proyecto.svg?branch=master)](https://travis-ci.org/josegob/IV-Proyecto)
[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
![](https://dockerbuildbadges.quelltext.eu/status.svg?organization=josegob&repository=iv-proyecto)

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/josegob/IV-Proyecto)

[Documentación del proyecto](https://josegob.github.io/IV-Proyecto/)

[Documentación pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI#pytelegrambotapi)

[Documentación psycopg2](http://initd.org/psycopg/docs/)

Despliegue https://bot-metacritic-api.herokuapp.com/

Contenedor: https://iv-proyecto-fttvcjqigj.now.sh

## Requisitos
* pyTelegramBotAPI
* Libreria requests, BeautifulSoup, re y psycopg2 para la base de datos

~~~
1. pip3 install pyTelegramBotAPI
2. pip3 install beautifulsoup4
3. pip3 install psycopg2
~~~

Las librerías **requests** y **re** vienen por defecto con Python por lo que no es necesario hacer nada.


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

También podemos hacer uso de la API de nuesto bot mediante el siguiente el siguiente enlace
 [https://bot-metacritic-api.herokuapp.com/](https://bot-metacritic-api.herokuapp.com/)

Las direcciones disponibles que tenemos en la API son:
* /juego/"nombre del juego"
* /pelicula/"nombre de la pelicula"
* /serie/"nombre de la serie"
* /top20/series
* /top20/peliculas

## Despliegue del proyecto en Docker


Para el despliegue de nuestra app en Docker:

Crearemos un repositorio en Docker y lo enlazaremos con nuestro GitHub como se puede ver en la siguiente imagen:

![Imagen Repo Docker](https://raw.githubusercontent.com/josegob/IV-Proyecto/gh-pages/assets/Docker_img.png)

Una vez hecho esto comprobamos que está correctamente enlazado con nuestro repositorio y con la rama en la que tenemos nuestro proyecto.

![Repo enlazado Docker](https://raw.githubusercontent.com/josegob/IV-Proyecto/gh-pages/assets/Docker_img_2.png)

Por otro lado necesitaremos hacer uso de un archivo Dockerfile que incluiremos en nuestro repositorio. El contenido de dicho archivo será el siguiente:
```
FROM ubuntu:16.04

MAINTAINER Jose Gomez Baena

# Variables de entorno para la conexion a la BD
ARG DATABASE_URL
ARG token_bot

ENV DATABASE_URL=$DATABASE_URL
ENV token_bot=$token_bot


RUN apt-get update
RUN apt-get install -y python3-pip
RUN apt-get install -y git
RUN git clone https://github.com/josegob/IV-Proyecto.git
RUN cd IV-Proyecto/ && pip3 install -r requirements.txt
```

Si todo está correctamente configurado, una vez subamos el fichero Dockerfile a nuestro repositorio, Docker empezará a construir un contenedor con los comandos que le hemos especificado.
Una vez terminé si no ha habido ningún error veremos la siguiente imagen en nuesto repositorio de Docker:

![Docker build](https://raw.githubusercontent.com/josegob/IV-Proyecto/gh-pages/assets/Docker_img_3.png)


Una vez tengamos el contenedor listo abrimos la consola y ejecutamos el siguiente comando:

```
sudo docker run -e "DATABASE_URL=MI_URL" -e "token_bot=MI_TOKEN" -i -t josegob/bot-metacritic
```
Una vez descargue nuestro contenedor, nos dará acceso a él y podremos ejecutar nuestra aplicación desde Docker

El repositorio de Docker es accesible desde en el siguiente:

https://hub.docker.com/r/josegob/iv-proyecto/

## Despliegue en AWS con Vagrant

Para el despliegue en AWS vamos a crear un archivo Vagrant con el siguiente contenido:

~~~
Vagrant.configure("2") do |config|
  config.vm.box = "dummy"

  config.vm.define "bot-metacritic-aws" do |host|
    host.vm.hostname = "bot-metacritic-aws"
  end
  config.vm.provider :aws do |aws, override|
    aws.access_key_id = "access_key_id"
    aws.secret_access_key = "secret_access_key"
    aws.session_token = "session_token"
    aws.keypair_name = "FINAL_KEY"
    aws.region= "us-west-2"
    aws.security_groups = [ 'botgrupo2' ]
    aws.instance_type= 't2.micro'

    aws.ami = "ami-19e92861"

    override.ssh.username = "ubuntu"
    override.ssh.private_key_path = "FINAL_KEY.pem"
  end

    config.vm.provision :ansible do |ansible|
    	ansible.playbook = "ansible_metacritic.yml"
    	ansible.force_remote_user= true
    	ansible.host_key_checking=false
  end


end
~~~

Como vemos al final del archivo Vagrant incluimos un archivo Ansible que se va a encargar de aprovisionar nuestro IaaS. El contenido de dicho archivo será:

~~~
---
- hosts: bot-metacritic-aws
  user: ubuntu
  gather_facts: no
  vars:
   token_bot: "{{ lookup('env','token_bot') }}"
   DATABASE_URL: "{{ lookup('env','DATABASE_URL')}}"

  pre_tasks:
    - name: Instalar Python
      become: yes
      raw: apt-get -y install python-simplejson

  tasks:
  - name: Actualizar sistema
    become: yes
    command: apt-get update

  - name: Instalar essential
    become: yes
    command: apt-get install -y build-essential

  - name: Instalar Git
    become: yes
    command: apt-get install -y git

  - name: Instalar pip3
    become: yes
    command: apt-get install -y python3-pip

  - name: Clonar GitHub
    become: yes
    git: repo=https://github.com/josegob/IV-Proyecto  dest=home/ubuntu/IV-Proyecto clone=yes force=yes

  - name: Instalar requirements
    become: yes
    command: pip3 install -r home/ubuntu/IV-Proyecto/requirements.txt
~~~

Una vez que se ejecute el archivo Vagrant nuestro IaaS estará listo para poder acceder mediante ssh con el comando ssh -i KEY.pem ubuntu@DNS

Donde KEY.pem es el fichero necesario para la autenticación.

## Uso de Fabric

Para automatizar el proceso de despliegue vamos a hacer uso de Fabric. Este fichero contendrá una serie de comandos que nos permitirá ejecutar de manera sencilla una serie de comandos.

El contenido de este fichero es el siguiente:

~~~
from fabric.api import *


def instalar_bot():
	run('sudo git clone https://github.com/josegob/IV-Proyecto')
	run('cd ./IV-Proyecto && sudo pip3 install -r requirements.txt')

def bot_up():
    with shell_env(token_bot='token_bot', DATABASE_URL='DATABASE_URL'):
        run('nohup sudo -E python3 ./IV-Proyecto/bot_metacritic/bot_metacritic.py', pty=False)

def delete_bot():
	run('sudo rm -rf ./IV-Proyecto')

def kill_bot():
    run('sudo pkill python3')
~~~

Para ejecutar estas funciones haremos uso de los siguientes comandos:

```fab -i KEY.pem -H ubuntu@DNS funcion_disponible```

Donde KEY.pem es el archivo comentado anteriormente y funcion_disponible es una de las funciones que hay en el archivo Fabric.

## Script automatización

Por últimos hemos creado un pequeño script que nos permite automatizar tanto el proceso de creacion y aprovisionamiento de nuestro IaaS en AWS como de la instalación y despliegue de nuestro Bot en Telegram.

~~~
vagrant up --provider=aws

fab -i KEY.pem -H ubuntu@DNS instalar_bot
fab -i KEY.pem -H ubuntu@DNS bot_up

#Cambiar KEY.pem por el archivo correspondiente de AWS
#Cambiar DNS por el correspondiente de la instancia creada con Vagrant
~~~
