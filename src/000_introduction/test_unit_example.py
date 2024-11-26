import unittest


class Carrello:
    def __init__(self):
        self.prodotti = []

    def aggiungi_prodotto(self, prodotto):
        pass

    def totale_prodotti(self):
        pass


class CarrelloShould(unittest.TestCase):
    def test_given_empty_cart_when_product_added_then_cart_contains_product(self):
        # Given
        carrello = Carrello()

        # When
        carrello.aggiungi_prodotto("Laptop")

        # Then
        self.assertEqual(carrello.totale_prodotti(), 1)
        self.assertIn("Laptop", carrello.prodotti)
