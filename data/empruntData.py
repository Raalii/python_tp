import sqlite3
from datetime import date
from model.auteur import Auteur
from model.emprunt import Emprunt
from model.livre import Livre
from model.membre import Membre


class EmpruntData:
    """Classe pour gérer les données des emprunts dans la base de données."""

    def __init__(self, db_name='TPFinal.db'):
        self.db_name = db_name

    def _connect(self):
        return sqlite3.connect(self.db_name)

    @staticmethod
    def _row_to_emprunt(rows):
        """Transforme les lignes de la base de données en objets Emprunt."""
        return [Emprunt(Membre(*row[18:]), Livre(*row[6:11], Auteur(*row[12:18])), row[0], row[3], row[4]) for row in
                rows]

    def _execute_query(self, query, params=()):
        with self._connect() as con:
            return con.execute(query, params).fetchall()

    def create(self, emprunt : Emprunt):
        with self._connect() as con:
            con.execute('''
            INSERT INTO emprunt (numeroMembre, idLivre, dateEmprunt, dateRetourPrevue)
            VALUES (?, ?, ?, ?)
            ''', (emprunt.membre.id, emprunt.livre.id, emprunt.date_emprunt, emprunt.date_retour_prevue))

    def get_by_member(self, numero_membre: int):
        rows = self._execute_query(
            '''SELECT * FROM emprunt 
            INNER JOIN livre ON emprunt.idLivre = livre.id 
            INNER JOIN auteur ON livre.idAuteur = auteur.id 
            INNER JOIN membre ON emprunt.numeroMembre = membre.id
            WHERE emprunt.numeroMembre = ?
            ''', (numero_membre,))
        return self._row_to_emprunt(rows)

    def get_all(self):
        rows = self._execute_query(
            '''SELECT * FROM emprunt 
            INNER JOIN livre ON emprunt.idLivre = livre.id 
            INNER JOIN auteur ON livre.idAuteur = auteur.id 
            INNER JOIN membre ON emprunt.numeroMembre = membre.id
            ''')
        return self._row_to_emprunt(rows)


    def delete(self, id_emprunt: int):
        with self._connect() as con:
            con.execute("DELETE FROM emprunt WHERE idEmprunt = ?", (id_emprunt,))

    def update_date_retour(self, id_emprunt: int, date_retour_reelle: date):
        with self._connect() as con:
            con.execute("UPDATE emprunt SET dateRetourReelle = ? WHERE idEmprunt = ?", (date_retour_reelle, id_emprunt))
