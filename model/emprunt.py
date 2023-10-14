from datetime import date
from model.livre import Livre
from model.membre import Membre


class Emprunt:
    def __init__(self, membre: Membre, livre: Livre, id : int, date_emprunt: date, date_retour_prevue: date, date_retour_reelle: date = None):
        self.id = id
        self.membre = membre
        self.livre = livre
        self.date_emprunt = date_emprunt
        self.date_retour_prevue = date_retour_prevue
        self.date_retour_reelle = date_retour_reelle

    def __str__(self):
        return f"{self.membre.prenom} {self.membre.nom} a emprunté {self.livre.titre} écrit par {self.livre.auteur.prenom} {self.livre.auteur.nom} le {self.date_emprunt}. Retour prévu le {self.date_retour_prevue}."
