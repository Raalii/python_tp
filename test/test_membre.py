import unittest
from datetime import date
from model.membre import Membre

class TestMembre(unittest.TestCase):
    def setUp(self):
        self.membre = Membre(id=1, numero_membre=123, prenom="Alice", nom="Johnson", adresse="123 Main St", date_naissance=date(1985, 5, 5))

    def test_membre_properties(self):
        self.assertEqual(self.membre.prenom, "Alice")
        self.assertEqual(self.membre.nom, "Johnson")
        self.assertEqual(self.membre.adresse, "123 Main St")
        self.assertEqual(self.membre.date_naissance, date(1985, 5, 5))
        self.assertEqual(self.membre.numero_membre, 123)
        self.assertEqual(self.membre.id, 1)

    def test_membre_str(self):
        expected_str = "None et mon numéro de membre est le 123"
        self.assertEqual(str(self.membre), expected_str)

if __name__ == '__main__':
    unittest.main()