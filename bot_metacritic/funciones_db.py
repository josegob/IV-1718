import psycopg2
import top20

lista_peliculas = []
lista_series = []

def devuelveTop20():
    # Connect to an existing database
    conn = psycopg2.connect("dbname=top20db user=top20bot password=root")

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
