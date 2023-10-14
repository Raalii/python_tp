"""
Module contenant la classe Membre.
Auteur : Mazabraud
Date : 13/10/2023
"""

from datetime import date
from model.personne import Personne


class Membre(Personne):
    def __init__(self, id : int, numero_membre: int, prenom: str, nom: str, adresse: str, date_naissance: date):
        """Classe Membre."""
        super().__init__(prenom, nom, adresse, date_naissance)
        self.numero_membre = numero_membre
        self.id = id

    def __str__(self):
        return f"{super().__str__()} et mon numéro de membre est le {self.numero_membre}"
