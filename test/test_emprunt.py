import unittest
from datetime import date
from model.auteur import Auteur
from model.livre import Livre
from model.membre import Membre
from model.emprunt import Emprunt

class TestEmprunt(unittest.TestCase):
    def setUp(self):
        self.auteur = Auteur(id=1, numero_auteur=123, prenom="John", nom="Doe", adresse="123 Main St", date_naissance="01/10/1990")
        self.livre = Livre(id=1, titre="Mon Livre", genre="Fiction", annee_publication=2020, statut="Disponible", auteur=self.auteur)
        self.membre = Membre(id=1, numero_membre=456, prenom="Alice", nom="Johnson", adresse="456 Elm St", date_naissance="01/10/1990")
        self.emprunt = Emprunt(membre=self.membre, livre=self.livre, id=1, date_emprunt="13/10/2023", date_retour_prevue="20/10/2023")

    def test_emprunt_properties(self):
        self.assertEqual(self.emprunt.membre, self.membre)
        self.assertEqual(self.emprunt.livre, self.livre)
        self.assertEqual(self.emprunt.date_emprunt, "13/10/2023")
        self.assertEqual(self.emprunt.date_retour_prevue, "20/10/2023")
        self.assertIsNone(self.emprunt.date_retour_reelle)

    def test_emprunt_str(self):

        expected_str = "Alice Johnson a emprunté Mon Livre écrit par John Doe le 13/10/2023. Retour prévu le 20/10/2023."
        self.assertEqual(str(self.emprunt), expected_str)

if __name__ == '__main__':
    unittest.main()