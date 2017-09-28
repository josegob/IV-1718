import requests
from bs4 import BeautifulSoup
import re
import sys
sys.path.insert(0, '/bot_metacritic')
import funciones_bot
import unittest


class TestsBotTelegram(unittest.TestCase):

    def test_url(self):
        self.assertEqual(funciones_bot.buscadorJuegos('juego prueba test'), -1)
        self.assertEqual(funciones_bot.buscadorSeries('serie prueba test'), -1)
        self.assertEqual(funciones_bot.buscadorJuegos('pelicula prueba test'), -1)

    def test_listas(self):
        self.assertEqual(len(funciones_bot.buscadorJuegos('life is strange')), 6)
        self.assertEqual(len(funciones_bot.buscadorSeries('young sheldon')), 6)
        self.assertEqual(len(funciones_bot.buscadorPeliculas('american made')), 6)


if __name__ == '__main__':
    unittest.main()
