import tkinter as tk
from tkinter import ttk, messagebox

from view.livre.afficherLivreView import AfficherLivres
from view.livre.creerLivreForm import CreerLivreForm
from view.livre.deleteLivreForm import SupprimerLivreForm
from view.baseView import BaseView


class LivreView(BaseView):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Voir Livre")
        self.create_widgets()
        self.grab_set()  # Rend cette fenêtre modale
        self.center_window()

    def create_widgets(self):
        ttk.Label(self, text="Gestion des Livres", font=("Arial", 20)).pack(pady=20)

        ttk.Button(self, text="Voir tous les livres", command=self.voir_livre).pack(pady=10)
        ttk.Button(self, text="Créer un livre", command=self.creer_livre).pack(pady=10)
        ttk.Button(self, text="Supprimer un livre", command=self.supprimer_livre).pack(pady=10)
        ttk.Button(self, text="Modifier un livre", command=self.modifier_livre).pack(pady=10)

    def creer_livre(self):
        CreerLivreForm(self)

    def supprimer_livre(self):
        SupprimerLivreForm(self)

    def voir_livre(self):
        AfficherLivres(self)

    def modifier_livre(self):
        messagebox.showinfo("Information", "Modification d'un livre")
