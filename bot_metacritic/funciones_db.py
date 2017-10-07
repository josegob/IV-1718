import psycopg2
import top20
import os
from urllib import parse

lista_peliculas = []
lista_series = []
parse.uses_netloc.append("postgres")
url = parse.urlparse(os.environ["DATABASE_URL"])

def devuelveTop20():
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

    cur.execute("SELECT * FROM top20peliculas")
    lista_peliculas = cur.fetchall()

    cur.execute("SELECT * FROM top20series")
    lista_series = cur.fetchall()

    conn.commit()

    # Close communication with the database
    cur.close()
    conn.close()

    return lista_peliculas, lista_series
