import tkinter as tk
from tkinter import ttk
from data.empruntData import EmpruntData
from view.baseView import BaseView

class AfficherEmprunts(BaseView):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Liste des emprunts")
        self.geometry("800x400")

        self.create_widgets()


    def create_widgets(self):
        # Création du tableau
        self.tree = ttk.Treeview(self, columns=(
        "ID", "Membre", "Livre", "Date d'emprunt", "Date de retour prévue", "Date de retour reelle"), show="headings")

        # Configuration des colonnes
        self.tree.heading("ID", text="ID", anchor=tk.CENTER)
        self.tree.heading("Membre", text="Membre", anchor=tk.CENTER)
        self.tree.heading("Livre", text="Livre", anchor=tk.CENTER)
        self.tree.heading("Date d'emprunt", text="Date d'emprunt", anchor=tk.CENTER)
        self.tree.heading("Date de retour prévue", text="Date de retour", anchor=tk.CENTER)
        self.tree.heading("Date de retour reelle", text="Date de retour reelle", anchor=tk.CENTER)

        # Remplissage du tableau avec les données
        emprunts = EmpruntData().get_all()
        for emprunt in emprunts:
            if emprunt.date_retour_reelle == None :
                emprunt.date_retour_reelle = "Encore en prêt"
            self.tree.insert("", "end", values=(
                emprunt.id,
                f"{emprunt.membre.prenom} {emprunt.membre.nom}",
                emprunt.livre.titre,
                emprunt.date_emprunt,
                emprunt.date_retour_prevue,
                emprunt.date_retour_reelle,

            ))


        # Ajout d'une barre de défilement
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)

        # Positionnement des widgets
        self.tree.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
