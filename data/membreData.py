import sqlite3
from datetime import date
from model.membre import Membre


class MembreData:
    """Classe pour gérer les données des membres dans la base de données."""

    def __init__(self, db_name='TPFinal.db'):
        self.db_name = db_name

    def _connect(self):
        return sqlite3.connect(self.db_name)

    @staticmethod
    def _row_to_membre(rows):
        return [Membre(*row) for row in rows]

    def _execute_query(self, query, params=()):
        with self._connect() as con:
            return con.execute(query, params).fetchall()

    def create(self, membre : Membre):
        with self._connect() as con:
            con.execute(
                "INSERT INTO membre (prenom, nom, adresse, date_naissance, numeroMembre) VALUES (?, ?, ?, ?, ?)",
                (membre.prenom, membre.nom, membre.adresse, membre.date_naissance, membre.numero_membre))

    def get_by_name(self, nom: str):
        rows = self._execute_query("SELECT * FROM membre WHERE nom = ?", (nom,))
        return self._row_to_membre(rows)

    def get_all(self):
        rows = self._execute_query("SELECT * FROM membre")
        return self._row_to_membre(rows)

    def update(self, id: int, prenom: str, nom: str, adresse: str, date_naissance: date, numero_membre: int):
        with self._connect() as con:
            con.execute(
                "UPDATE membre SET prenom = ?, nom = ?, adresse = ?, date_naissance = ?, numeroMembre = ? WHERE id = ?",
                (prenom, nom, adresse, date_naissance, numero_membre, id))

    def delete(self, id: int):
        with self._connect() as con:
            con.execute("DELETE FROM membre WHERE id = ?", (id,))
