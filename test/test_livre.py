import unittest
from model.auteur import Auteur
from model.livre import Livre

class TestLivre(unittest.TestCase):
    def setUp(self):
        self.auteur = Auteur(id=1, numero_auteur=123, prenom="John", nom="Doe", adresse="123 Main St", date_naissance="10/10/1999")
        self.livre = Livre(id=1, titre="Mon Livre", genre="Fiction", annee_publication=2020, statut="Disponible", auteur=self.auteur)

    def test_livre_properties(self):
        self.assertEqual(self.livre.titre, "Mon Livre")
        self.assertEqual(self.livre.genre, "Fiction")
        self.assertEqual(self.livre.annee_publication, 2020)
        self.assertEqual(self.livre.statut, "Disponible")
        self.assertEqual(self.livre.auteur, self.auteur)

    def test_livre_str(self):
        expected_str = "(Mon Livre,Fiction,2020,Disponible), auteur : John Doe"
        self.assertEqual(str(self.livre), expected_str)

if __name__ == '__main__':
    unittest.main()