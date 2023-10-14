"""
Ce module contient la classe Auteur.
Auteur : Mazabraud
Date : 13/10/2023
"""

from datetime import date
from typing import Union

from model.personne import Personne


class Auteur(Personne):
    """
    Classe représentant un auteur.
    """

    def __init__(
            self,
            id_auteur: int,
            numero_auteur: int,
            prenom: str,
            nom: str,
            adresse: str,
            date_naissance: Union[date, str]):
        """
        Initialise un objet Auteur.

        :param id_auteur: L'identifiant de l'auteur.
        :param numero_auteur: Le numéro de l'auteur.
        :param prenom: Le prénom de l'auteur.
        :param nom: Le nom de l'auteur.
        :param adresse: L'adresse de l'auteur.
        :param date_naissance: La date de naissance de l'auteur (date ou chaîne de caractères).
        """
        super().__init__(prenom, nom, adresse, date_naissance)
        self.numero_auteur = numero_auteur
        self.id_auteur = id_auteur

    def __str__(self):
        """ Affichage d'un auteur """
        return f"{self.nom_prenom}, numéro {self.numero_auteur}"
