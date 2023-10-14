import tkinter as tk
from tkinter import ttk
from data.livreData import LivreData
from view.baseView import BaseView


class AfficherLivres(BaseView):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Liste des livres")
        self.geometry("800x400")

        self.create_widgets()

    def create_widgets(self):
        # Création du tableau
        self.tree = ttk.Treeview(self, columns=("ID", "Titre", "Genre", "Année de publication", "Statut", "Auteur"),
                                 show="headings")

        # Configuration des colonnes
        self.tree.heading("ID", text="ID", anchor=tk.CENTER)
        self.tree.heading("Titre", text="Titre", anchor=tk.CENTER)
        self.tree.heading("Genre", text="Genre", anchor=tk.CENTER)
        self.tree.heading("Année de publication", text="Année de publication", anchor=tk.CENTER)
        self.tree.heading("Statut", text="Statut", anchor=tk.CENTER)
        self.tree.heading("Auteur", text="Auteur", anchor=tk.CENTER)

        # Remplissage du tableau avec les données
        livres = LivreData().get_all()
        for livre in livres:
            self.tree.insert("", "end", values=(
                livre.id, livre.titre, livre.genre, livre.annee_publication, livre.statut, f"{livre.auteur.prenom} {livre.auteur.nom}"))

        # Ajout d'une barre de défilement
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)

        # Positionnement des widgets
        self.tree.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
