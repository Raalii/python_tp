import tkinter as tk
from tkinter import ttk, messagebox

from view.auteur.afficherAuteurView import AfficherAuteurs
from view.auteur.creerAuteurForm import CreerAuteurForm
from view.auteur.deleteAuteurForm import SupprimerAuteurForm
from view.baseView import BaseView


class AuteurView(BaseView):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Voir Auteur")
        self.create_widgets()
        self.grab_set()  # Rend cette fenêtre modale
        self.center_window()

    def create_widgets(self):
        ttk.Label(self, text="Gestion des Auteurs", font=("Arial", 20)).pack(pady=20)

        ttk.Button(self, text="Voir tout les auteurs ", command=self.voir_auteur).pack(pady=10)
        ttk.Button(self, text="Créer un auteur", command=self.creer_auteur).pack(pady=10)
        ttk.Button(self, text="Supprimer un auteur", command=self.supprimer_auteur).pack(pady=10)
        ttk.Button(self, text="Modifier un auteur", command=self.modifier_auteur).pack(pady=10)

    def creer_auteur(self):
        # Code pour créer un auteur
        # Vous pouvez ouvrir une nouvelle fenêtre pour obtenir les détails de l'auteur
        CreerAuteurForm(self)

    def supprimer_auteur(self):
        # Code pour supprimer un auteur
        SupprimerAuteurForm(self)

    def voir_auteur(self):
        # Code pour ajouter un auteur
        AfficherAuteurs(self)

    def modifier_auteur(self):
        # Code pour modifier un auteur
        messagebox.showinfo("Information", "Modification d'un auteur")
