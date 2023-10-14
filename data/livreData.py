import sqlite3

from model.auteur import Auteur
from model.livre import Livre


class LivreData:
    """Classe pour gérer les données des livres dans la base de données."""

    def __init__(self, db_name='TPFinal.db'):
        self.db_name = db_name

    def _connect(self):
        return sqlite3.connect(self.db_name)

    @staticmethod
    def _row_to_class(rows):
        """Transforme les lignes de la base de données en objets Livre."""
        return [Livre(*row[0:5], Auteur(*row[6:])) for row in rows]

    def create(self, livre : Livre):
        """Crée un nouveau livre dans la base de données."""
        with self._connect() as con:
            con.execute("INSERT INTO livre (titre, genre, anneePublication, statut, idAuteur) VALUES (?, ?, ?, ?, ?)",
                        (livre.titre, livre.genre, livre.annee_publication, livre.statut, livre.auteur.id_auteur))

    def get_by_name(self, titre: str):
        """Récupère un livre par son titre."""
        with self._connect() as con:
            rows = con.execute("SELECT * FROM livre INNER JOIN auteur ON livre.idAuteur = auteur.id WHERE titre = ?", (titre,)).fetchall()
        return self._row_to_class(rows)

    def get_all(self):
        """Récupère tous les livres disponibles."""
        with self._connect() as con:
            rows = con.execute("SELECT * FROM livre INNER JOIN auteur ON livre.idAuteur = auteur.id").fetchall()
        return self._row_to_class(rows)

    def update(self, id: int, titre: str, genre: str, annee_publication: int, statut: str, id_auteur: str):
        """Met à jour les informations d'un livre."""
        with self._connect() as con:
            con.execute("UPDATE livre SET titre = ?, genre = ?, anneePublication = ?, statut = ?, idAuteur = ? WHERE id = ?",
                        (titre, genre, annee_publication, statut, id_auteur, id))

    def delete(self, id: int):
        """Supprime un livre."""
        with self._connect() as con:
            con.execute("DELETE FROM livre WHERE id = ?", (id,))
