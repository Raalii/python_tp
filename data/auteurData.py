import sqlite3
from datetime import date

from model.auteur import Auteur


class AuteurData:
    """Classe pour gérer les données des auteurs dans la base de données."""

    def __init__(self, db_name='TPFinal.db'):
        self.db_name = db_name

    def _connect(self):
        return sqlite3.connect(self.db_name)


    def create(self, auteur : Auteur):
        """Crée un nouvel auteur dans la base de données."""
        print(auteur.date_naissance)
        with self._connect() as con:
            con.execute("INSERT INTO auteur (prenom, nom, adresse, date_naissance, numeroAuteur) VALUES (?, ?, ?, ?, ?)",
                        (auteur.prenom, auteur.nom, auteur.adresse, auteur.date_naissance, auteur.numero_auteur))

    def get_by_name(self, nom: str):
        """Récupère un auteur par son nom."""
        with self._connect() as con:
            rows = con.execute("SELECT * FROM auteur WHERE nom = ?", (nom,)).fetchall()

        return [Auteur(*auteur) for auteur in rows]

    def get_by_id(self, id: int):
        """Récupère un auteur par son nom."""
        with self._connect() as con:
            rows = con.execute("SELECT * FROM auteur WHERE id = ?", (int,)).fetchone()

        return Auteur(*rows)

    def get_all(self):
        """Récupère tous les auteurs."""
        with self._connect() as con:
            rows = con.execute("SELECT * FROM auteur").fetchall()
            print()
        return [Auteur(*auteur) for auteur in rows]

    def update(self, id: int, prenom: str, nom: str, adresse: str, date_naissance: date, numero_auteur: int):
        """Met à jour les informations d'un auteur."""
        with self._connect() as con:
            con.execute("UPDATE auteur SET prenom = ?, nom = ?, adresse = ?, date_naissance = ?, numeroAuteur= ? WHERE id = ?",
                        (prenom, nom, adresse, date_naissance, numero_auteur, id))

    def delete(self, id: int):
        """Supprime un auteur."""
        with self._connect() as con:
            con.execute("DELETE FROM auteur WHERE id = ?", (id,))
