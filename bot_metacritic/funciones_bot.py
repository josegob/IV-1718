import requests
from bs4 import BeautifulSoup
import re


headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
lista_final = []
lista_series = []
lista_peliculas = []

def buscadorJuegos(busqueda):

    juego = busqueda.lower()
    juego = re.sub(r'\s+', ' ', juego)
    juego = juego.replace(" ", "-")


    url_base = "http://www.metacritic.com/game/pc/"
    url_juego = url_base + juego
    url_final = requests.get(url_juego, headers=headers)

    if (url_final.status_code == 404):
        #print("El juego buscado no se encuentra en la base de datos de Metacritic")
        #lista_final.append("El juego introducido no se encuentra en la base de datos de Metacritic")
        return -1

    else:
        soup = BeautifulSoup(url_final.content, 'html.parser')
        nombre_juego = soup.find_all('span', itemprop='name')[0].get_text()
        nombre_juego = re.sub(r'\s+', ' ', nombre_juego)
        nombre_juego = nombre_juego[1:-1]
        #print("\nNombre del juego:", nombre_juego)
        lista_final.append(nombre_juego)

        if (len(soup.find_all('span', itemprop='ratingValue')) > 0):
            nota_metacritic = soup.find_all('span', itemprop='ratingValue')[0].get_text()
            nota_metacritic = re.sub(r'\s+', ' ', nota_metacritic)
            #print("Nota Metacritic:",nota_metacritic)
            lista_final.append(nota_metacritic)
        else:
            #print("Aun no hay nota de metacritic para este juego")
            lista_final.append("Aun no hay nota de metacritic para este juego")

        if (len(soup.find_all('div', class_='metascore_w user large game mixed'))) > 0:
            #print("Nota media usuarios:", soup.find_all('div', class_='metascore_w user large game mixed')[0].get_text())
            nota_usuarios = soup.find_all('div', class_='metascore_w user large game mixed')[0].get_text()
            lista_final.append(nota_usuarios)
        elif (len(soup.find_all('div', class_='metascore_w user large game positive'))) > 0:
            #print("Nota media usuarios:", soup.find_all('div', class_='metascore_w user large game positive')[0].get_text())
            nota_usuarios = soup.find_all('div', class_='metascore_w user large game positive')[0].get_text()
            lista_final.append(nota_usuarios)
        elif (len(soup.find_all('div', class_='metascore_w user large game negative'))) > 0:
            #print("Nota media usuarios:", soup.find_all('div', class_='metascore_w user large game negative')[0].get_text())
            nota_usuarios = soup.find_all('div', class_='metascore_w user large game negative')[0].get_text()
            lista_final.append(nota_usuarios)
        else:
            #print("Aun no hay nota media de los usuarios para este juego")
            lista_final.append("Aun no hay nota media de los usuarios para este juego")


        #print("Fecha de lanzamiento:", soup.find_all('span', itemprop='datePublished')[0].get_text())
        release_date = soup.find_all('span', itemprop='datePublished')[0].get_text()
        lista_final.append(release_date)

        dev = soup.find_all('li', class_="summary_detail developer")[0].get_text()
        dev = re.sub(r'\s+', ' ', dev)
        dev = dev[12:-1]
        #print("Desarrolladora:", dev)
        lista_final.append(dev)

        lista_final.append(url_juego)
 
        return lista_final



def buscadorSeries(busqueda):

    serie = busqueda.lower()
    serie = re.sub(r'\s+', ' ', serie)
    serie = serie.replace(" ", "-")


    url_base = "http://www.metacritic.com/tv/"
    url_serie = url_base + serie
    url_final = requests.get(url_serie, headers=headers)

    if (url_final.status_code == 404):
        #lista_series.append("La serie introducida no se encuentra en la base de datos de Metacritic")
        return -1


    else:
        soup = BeautifulSoup(url_final.content, 'html.parser')
        nombre_serie = soup.find_all('span', itemprop='name')[0].get_text()
        nombre_serie = re.sub(r'\s+', ' ', nombre_serie)
        nombre_serie = nombre_serie[1:-1]
        lista_series.append(nombre_serie)

        if (len(soup.find_all('span', itemprop='ratingValue')) > 0):
            nota_metacritic = soup.find_all('span', itemprop='ratingValue')[0].get_text()
            nota_metacritic = re.sub(r'\s+', ' ', nota_metacritic)
            lista_series.append(nota_metacritic)

        else:
            lista_series.append("Aun no hay nota de metacritic para esta serie")

        if (len(soup.find_all('div', class_='metascore_w user large game mixed'))) > 0:
            nota_usuarios = soup.find_all('div', class_='metascore_w user large game mixed')[0].get_text()
            lista_series.append(nota_usuarios)
        elif (len(soup.find_all('div', class_='metascore_w user large game positive'))) > 0:
            nota_usuarios = soup.find_all('div', class_='metascore_w user large game positive')[0].get_text()
            lista_series.append(nota_usuarios)
        elif (len(soup.find_all('div', class_='metascore_w user large game negative'))) > 0:
            nota_usuarios = soup.find_all('div', class_='metascore_w user large game negative')[0].get_text()
            lista_series.append(nota_usuarios)
        else:
            lista_series.append("Aun no hay nota media de los usuarios para esta serie")


        detalles = soup.find_all('div', class_='product_data')[0]
        tmp = detalles.find_all('li', class_='summary_detail release_data')[0]
        tmp_2 = tmp.find_all('span', class_='data')[0].get_text()
        lista_series.append(tmp_2)

        detalles = soup.find_all('div', class_='product_data')[0]
        tmp = detalles.find_all('li', class_='summary_detail network publisher')[0]
        tmp_2 = tmp.find_all('span', itemprop='name')[0].get_text()
        tmp_2 = re.sub(r'\s+', ' ', tmp_2)
        tmp_2 = tmp_2[1:-1]
        lista_series.append(tmp_2)

        lista_series.append(url_serie)

        return lista_series


def buscadorPeliculas(busqueda):

    pelicula = busqueda.lower()
    pelicula = re.sub(r'\s+', ' ', pelicula)
    pelicula = pelicula.replace(" ", "-")


    url_base = "http://www.metacritic.com/movie/"
    url_pelicula = url_base + pelicula
    url_final = requests.get(url_pelicula, headers=headers)


    if (url_final.status_code == 404):
        #lista_peliculas.append("La serie introducida no se encuentra en la base de datos de Metacritic")
        return -1


    else:
        soup = BeautifulSoup(url_final.content, 'html.parser')
        nombre_pelicula = soup.find_all('div', class_='product_page_title oswald')[0].get_text()
        nombre_pelicula = re.sub(r'\s+', ' ', nombre_pelicula)
        nombre_pelicula = nombre_pelicula[1:-6]
        lista_peliculas.append(nombre_pelicula)

        if (len(soup.find_all('td', class_='summary_right pad_btm1')) > 0):
            if (len(soup.find_all('span', class_='metascore_w larger movie positive')) > 0):
                nota_metacritic = soup.find_all('span', class_='metascore_w larger movie positive')[0].get_text()
                nota_metacritic = re.sub(r'\s+', ' ', nota_metacritic)
                lista_peliculas.append(nota_metacritic)

            elif (len(soup.find_all('span', class_='metascore_w larger movie mixed')) > 0):
                nota_metacritic = soup.find_all('span', class_='metascore_w larger movie mixed')[0].get_text()
                nota_metacritic = re.sub(r'\s+', ' ', nota_metacritic)
                lista_peliculas.append(nota_metacritic)

            else:
                nota_metacritic = soup.find_all('span', class_='metascore_w larger movie negative')[0].get_text()
                nota_metacritic = re.sub(r'\s+', ' ', nota_metacritic)
                lista_peliculas.append(nota_metacritic)

        if (len(soup.find_all('div', class_='distribution'))) > 1:
            tmp = soup.find_all('div', class_='distribution')[1]
            nota_usuarios = tmp.find_all('div', class_='metascore_w user larger movie positive')[0].get_text()
            print(nota_usuarios)
            lista_peliculas.append(nota_usuarios)

        elif (len(soup.find_all('div', class_='distribution'))) > 1:
            tmp = soup.find_all('div', class_='distribution')[1]
            nota_usuarios = tmp.find_all('div', class_='metascore_w user larger movie mixed')[0].get_text()
            print(nota_usuarios)
            lista_peliculas.append(nota_usuarios)

        elif (len(soup.find_all('div', class_='distribution'))) > 1:
            tmp = soup.find_all('div', class_='distribution')[1]
            nota_usuarios = tmp.find_all('div', class_='metascore_w user larger movie negative')[0].get_text()
            print(nota_usuarios)
            lista_peliculas.append(nota_usuarios)

        else:
            lista_peliculas.append("Aun no hay nota media de los usuarios para esta serie")


        detalles = soup.find_all('div', class_='details_section')[0]
        tmp = detalles.find_all('span', class_='distributor')[0].get_text()
        tmp = re.sub(r'\s+', ' ', tmp)
        tmp = tmp[:-3]
        lista_peliculas.append(tmp)

        detalles = soup.find_all('div', class_='details_section')[0]
        tmp = detalles.find_all('span', class_='release_date')[0].get_text()
        tmp = re.sub(r'\s+', ' ', tmp)
        tmp = tmp[15:-1]
        lista_peliculas.append(tmp)

        lista_peliculas.append(url_pelicula)

        return lista_peliculas
