import unittest
from model.bibliotheque import Bibliotheque

class TestBibliotheque(unittest.TestCase):
    def setUp(self):
        self.bibliotheque = Bibliotheque(nom="Biblio", adresse="123 Main St", numero_telephone="555-1234")

    def test_bibliotheque_properties(self):
        self.assertEqual(self.bibliotheque.nom, "Biblio")
        self.assertEqual(self.bibliotheque.adresse, "123 Main St")
        self.assertEqual(self.bibliotheque.numero_telephone, "555-1234")

    def test_bibliotheque_str(self):
        expected_str = "Le nom de la bibliothèque est Biblio, je suis situé au 123 Main St avec comme numéro 555-1234"
        self.assertEqual(str(self.bibliotheque), expected_str)

if __name__ == '__main__':
    unittest.main()