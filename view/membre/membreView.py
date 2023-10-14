import tkinter as tk
from tkinter import ttk, messagebox

from view.membre.afficherMembreView import AfficherMembres
from view.membre.creerMembreForm import CreerMembreForm
from view.membre.deleteMembreForm import SupprimerMembreForm
from view.baseView import BaseView


class MembreView(BaseView):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Voir Membre")
        self.create_widgets()
        self.grab_set()  # Rend cette fenêtre modale
        self.center_window()

    def create_widgets(self):
        ttk.Label(self, text="Gestion des Membres", font=("Arial", 20)).pack(pady=20)

        ttk.Button(self, text="Voir tout les membres", command=self.voir_membre).pack(pady=10)
        ttk.Button(self, text="Créer un membre", command=self.creer_membre).pack(pady=10)
        ttk.Button(self, text="Supprimer un membre", command=self.supprimer_membre).pack(pady=10)
        ttk.Button(self, text="Modifier un membre", command=self.modifier_membre).pack(pady=10)

    def creer_membre(self):
        CreerMembreForm(self)

    def supprimer_membre(self):
        SupprimerMembreForm(self)

    def voir_membre(self):
        AfficherMembres(self)

    def modifier_membre(self):
        messagebox.showinfo("Information", "Modification d'un membre")
