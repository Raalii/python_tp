import tkinter as tk
from tkinter import ttk
from data.auteurData import AuteurData
from view.baseView import BaseView


class AfficherAuteurs(BaseView):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Liste des auteurs")
        self.geometry("600x400")

        self.create_widgets()

    def create_widgets(self):
        # Création du tableau
        self.tree = ttk.Treeview(self, columns=("ID", "Numéro", "Prénom", "Nom", "Adresse", "Date de naissance"),
                                 show="headings")

        # Configuration des colonnes
        self.tree.heading("ID", text="ID",anchor=tk.CENTER)
        self.tree.heading("Numéro", text="Numéro d'auteur",anchor=tk.CENTER)
        self.tree.heading("Prénom", text="Prénom",anchor=tk.CENTER)
        self.tree.heading("Nom", text="Nom",anchor=tk.CENTER)
        self.tree.heading("Adresse", text="Adresse",anchor=tk.CENTER)
        self.tree.heading("Date de naissance", text="Date de naissance",anchor=tk.CENTER)

        # Remplissage du tableau avec les données
        auteurs = AuteurData().get_all()
        for auteur in auteurs:
            self.tree.insert("", "end", values=(
            auteur.id_auteur, auteur.numero_auteur, auteur.prenom, auteur.nom, auteur.adresse, auteur.date_naissance))

        # Ajout d'une barre de défilement
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)

        # Positionnement des widgets
        self.tree.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
