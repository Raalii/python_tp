import unittest
from datetime import date
from model.auteur import Auteur

class TestAuteur(unittest.TestCase):
    def setUp(self):
        self.auteur = Auteur(id=1, numero_auteur=123, prenom="John", nom="Doe", adresse="123 Main St", date_naissance=date(1990, 1, 1))

    def test_auteur_properties(self):
        self.assertEqual(self.auteur.prenom, "John")
        self.assertEqual(self.auteur.nom, "Doe")
        self.assertEqual(self.auteur.adresse, "123 Main St")
        self.assertEqual(self.auteur.date_naissance, date(1990, 1, 1))
        self.assertEqual(self.auteur.numero_auteur, 123)
        self.assertEqual(self.auteur.id, 1)

    def test_auteur_str(self):
        expected_str = "John Doe, né le 1990-01-01 et mon numéro d'auteur est le 123"
        self.assertEqual(str(self.auteur), expected_str)

if __name__ == '__main__':
    unittest.main()