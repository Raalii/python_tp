"""
Module contenant la classe Livre.
Auteur : Mazabraud
Date : 13/10/2023
"""
from model.auteur import Auteur

class Livre:
    def __init__(self, id : int , titre: str, genre: str, annee_publication: int, statut: str, auteur: Auteur):
        """Classe Livre."""
        self.id = id
        self.titre = titre
        self.genre = genre
        self.annee_publication = annee_publication
        self.statut = statut
        self.auteur = auteur

    def __str__(self):
        return f"({self.titre!s},{self.genre!s},{self.annee_publication!s},{self.statut!s}), auteur : {self.auteur.prenom} {self.auteur.nom}"