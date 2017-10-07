from lxml import html
import requests
from bs4 import BeautifulSoup
import re

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

def top20Peliculas():

    url_peliculas = requests.get("http://www.metacritic.com/browse/movies/score/metascore/90day/filtered", headers=headers)
    #Obtenemos la informacion html de la pagina solicitada. Añadimos el parametro headers
    #para que no nos devuelva un error Forbidden 403.

    soup = BeautifulSoup(url_peliculas.content, 'html.parser')
    #Hacemos uso de la libreria Soup para parsear el contenido HTML

    nombre_peliculas = [] #Creamos las listas donde añadiremos la informacion que
    puntuacion_peliculas = [] #vamos a sacar de la página
    info_peliculas = []
    release_date_peliculas = []

    for i in range(0,20): #Iteramos sobre cada pelicula de la lista para obtener posteriormente la info que necsitamos
        contenedor = soup.find_all('tr', class_='summary_row')[i]
        tmp = contenedor.find_all('div', class_='title')[0].get_text()
        tmp = re.sub(r'\s+', ' ', tmp)
        tmp = tmp[1:]
        nombre_peliculas.append(tmp)


    for j in range(0,20):
        contenedor = soup.find_all('tr', class_='summary_row')[j]
        tmp = contenedor.find_all('div', class_='metascore_w large movie positive')[0].get_text()
        tmp = re.sub(r'\s+', ' ', tmp)
        puntuacion_peliculas.append(tmp)


    for p in range(0,20):
        contenedor = soup.find_all('tr', class_='summary_row')[p]
        tmp = contenedor.find_all('a', href=True)[0]
        tmp_pelicula = "http://www.metacritic.com" + tmp['href']
        info_peliculas.append(tmp_pelicula)


    for h in range(0,20):
        contenedor = soup.find_all('tr', class_='summary_row')[h]
        tmp = contenedor.find_all('td', class_='date_wrapper')[0].get_text()
        tmp = re.sub(r'See More', '', tmp)
        tmp = re.sub(r'\s+', ' ', tmp)
        tmp = tmp[1:-1]
        release_date_peliculas.append(tmp)

    return nombre_peliculas, puntuacion_peliculas, info_peliculas, release_date_peliculas


def top20Series():

        url_series = requests.get("http://www.metacritic.com/browse/tv/score/metascore/90day/filtered", headers=headers)
        #Obtenemos la informacion html de la pagina solicitada. Añadimos el parametro headers
        #para que no nos devuelva un error Forbidden 403.

        soup = BeautifulSoup(url_series.content, 'html.parser')
        #Hacemos uso de la libreria Soup para parsear el contenido HTML

        nombre_series = [] #Creamos las listas donde añadiremos la informacion que
        puntuacion_series = [] #vamos a sacar de la página
        info_series = []
        release_date_series = []


        for i in range(-1,19): #Iteramos sobre cada pelicula de la lista para obtener posteriormente la info que necsitamos
            if i == -1:
                contenedor = soup.find_all('div', class_='product_row season first')[0]
                tmp = contenedor.find_all('div', class_='product_item product_title')[0].get_text()
                tmp = re.sub(r'\s+', ' ', tmp)
                tmp = tmp[1:-1]
                nombre_series.append(tmp)
            else:
                contenedor = soup.find_all('div', class_='product_row season')[i]
                tmp = contenedor.find_all('div', class_='product_item product_title')[0].get_text()
                tmp = re.sub(r'\s+', ' ', tmp)
                tmp = tmp[1:-1]
                nombre_series.append(tmp)


        for j in range(-1,19):
            if j == -1:
                contenedor = soup.find_all('div', class_='product_row season first')[0]
                tmp = contenedor.find_all('div', class_='metascore_w small season positive')[0].get_text()
                puntuacion_series.append(tmp)
            else:
                contenedor = soup.find_all('div', class_='product_row season')[j]
                tmp = contenedor.find_all('div', class_='metascore_w small season positive')[0].get_text()
                puntuacion_series.append(tmp)


        for p in range(-1,19):
            if p == -1:
                contenedor = soup.find_all('div', class_='product_row season first')[0]
                tmp = contenedor.find_all('a', href=True)[0]
                tmp_serie = "http://www.metacritic.com" + tmp['href']
                info_series.append(tmp_serie)
            else:
                contenedor = soup.find_all('div', class_='product_row season')[p]
                tmp = contenedor.find_all('a', href=True)[0]
                tmp_serie = "http://www.metacritic.com" + tmp['href']
                info_series.append(tmp_serie)


        for h in range(-1,19):
            if h == -1:
                contenedor = soup.find_all('div', class_='product_row season first')[0]
                tmp = contenedor.find_all('div', class_='product_item product_date')[0].get_text()
                tmp = re.sub(r'\s+', ' ', tmp)
                tmp = tmp[1:-1]
                release_date_series.append(tmp)
            else:
                contenedor = soup.find_all('div', class_='product_row season')[h]
                tmp = contenedor.find_all('div', class_='product_item product_date')[0].get_text()
                tmp = re.sub(r'\s+', ' ', tmp)
                tmp = tmp[1:-1]
                release_date_series.append(tmp)

        return nombre_series, puntuacion_series, info_series, release_date_series
