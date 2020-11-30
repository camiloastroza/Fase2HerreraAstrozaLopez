from django.test import SimpleTestCase
from catalogo.forms import GameForm

class TestForms(SimpleTestCase):

    def test_game_form_valid_data(self):
        form = GameForm(data={
            'cod': '3',
            'nombre': 'Mario Kart',
            'creador': 'Shigeru Miyamoto',
            'descripcion': 'Videojuego de carreras de la saga Mario Bros'
        })

        self.assertTrue(form.is_valid())



    def test_game_form_no_data(self):
        form = GameForm(data={})


        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors),4)

