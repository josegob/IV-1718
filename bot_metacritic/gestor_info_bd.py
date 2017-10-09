import psycopg2
import funciones_top20
import os
from urllib import parse


def aniadirTop20():

    peliculas = funciones_top20.top20Peliculas()
    series = funciones_top20.top20Series()

    parse.uses_netloc.append("postgres")
    url = parse.urlparse(os.environ["DATABASE_URL"])

    # Connect to an existing database
    conn = psycopg2.connect(
        database=url.path[1:],
        user=url.username,
        password=url.password,
        host=url.hostname,
        port=url.port
    )

    # Open a cursor to perform database operations
    cur = conn.cursor()

    cur.execute("DELETE from top20peliculas")
    cur.execute("DELETE from top20series")

    for j in range(0,20):
        cur.execute("INSERT INTO top20peliculas (nombre_pelicula,puntuacion_pelicula,enlace_pelicula,fecha_pelicula) VALUES (%s,%s,%s,%s)", (peliculas[0][j],peliculas[1][j],peliculas[2][j],peliculas[3][j]))

    for p in range(0,20):
        cur.execute("INSERT INTO top20series (nombre_serie,puntuacion_serie,enlace_serie,fecha_serie) VALUES (%s,%s,%s,%s)", (series[0][p],series[1][p],series[2][p],series[3][p]))
    # Pass data to fill a query placeholders and let Psycopg perform
    # the correct conversion (no more SQL injections!)

    # Query the database and obtain data as Python objects

    # Make the changes to the database persistent
    conn.commit()

    # Close communication with the database
    cur.close()
    conn.close()
