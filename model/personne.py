"""
Module contenant la classe Personne.
Auteur : Mazabraud
Date : 13/10/2023
"""
from datetime import date, datetime
from typing import Union


class Personne:
    def __init__(self, prenom: str, nom: str, adresse: str, date_naissance : Union[date, str]):
        """Classe Personne."""
        self.prenom = prenom
        self.nom = nom
        self.adresse = adresse
        if isinstance(date_naissance, str):
            date_naissance = datetime.strptime(date_naissance, '%d/%m/%Y').date()
            date_naissance = date_naissance.strftime('%d/%m/%Y')
        self.date_naissance = date_naissance

    @property
    def age(self):
        """Calcule l'âge à partir de la date de naissance."""
        aujourdhui = date.today()

        # calcul age sur les annéess
        age = aujourdhui.year - self.date_naissance.year

        # Si la date d'anniv de cette année est pas passée, enlever 1 an
        if (aujourdhui.month, aujourdhui.day) < (self.date_naissance.month, self.date_naissance.day):
            age -= 1

        return age

    def __str__(self):
        return f"Je m'appelle {self.prenom} {self.nom}, j'ai {self.age} ans et j'habite au {self.adresse}"

    @property
    def nom_prenom(self):
        return f'{self.prenom} {self.nom}'
