import tkinter as tk
from tkinter import ttk
from view.baseView import BaseView
from view.emprunt.creerEmpruntForm import CreerEmpruntForm
from view.emprunt.deleteEmpruntForm import SupprimerEmpruntForm
from view.emprunt.afficherEmprunts import AfficherEmprunts

class EmpruntView(BaseView):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Gestion des Emprunts")
        self.create_widgets()
        self.grab_set()  # Rend cette fenêtre modale
        self.center_window()

    def create_widgets(self):
        ttk.Label(self, text="Gestion des Emprunts", font=("Arial", 20)).pack(pady=20)

        ttk.Button(self, text="Voir tous les emprunts", command=self.voir_emprunts).pack(pady=10)
        ttk.Button(self, text="Créer un emprunt", command=self.creer_emprunt).pack(pady=10)
        ttk.Button(self, text="Supprimer un emprunt", command=self.supprimer_emprunt).pack(pady=10)

    def creer_emprunt(self):
        CreerEmpruntForm(self)

    def supprimer_emprunt(self):
        SupprimerEmpruntForm(self)

    def voir_emprunts(self):
        AfficherEmprunts(self)
