import tkinter as tk
from tkinter import ttk, messagebox
from data.empruntData import EmpruntData
from data.membreData import MembreData
from data.livreData import LivreData
from model.emprunt import Emprunt
from view.baseView import BaseView

class CreerEmpruntForm(BaseView):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Créer un emprunt")
        self.geometry("400x300")

        self.membre_data = MembreData()
        self.livre_data = LivreData()

        self.membres = self.membre_data.get_all()
        self.livres = self.livre_data.get_all()

        self.create_widgets()

    def create_widgets(self):
        # Variables pour stocker les entrées
        self.selected_membre = tk.StringVar()
        self.selected_livre = tk.StringVar()
        self.date_emprunt_var = tk.StringVar()
        self.date_retour_var = tk.StringVar()

        # Création des widgets
        ttk.Label(self, text="Membre:").grid(row=0, column=0, sticky="w", padx=10, pady=5)
        membres_noms = [f"{membre.prenom} {membre.nom}" for membre in self.membres]
        self.membre_combobox = ttk.Combobox(self, values=membres_noms, textvariable=self.selected_membre)
        self.membre_combobox.grid(row=0, column=1, padx=10, pady=5)

        ttk.Label(self, text="Livre:").grid(row=1, column=0, sticky="w", padx=10, pady=5)
        livres_titres = [livre.titre for livre in self.livres]
        self.livre_combobox = ttk.Combobox(self, values=livres_titres, textvariable=self.selected_livre)
        self.livre_combobox.grid(row=1, column=1, padx=10, pady=5)

        ttk.Label(self, text="Date d'emprunt:").grid(row=2, column=0, sticky="w", padx=10, pady=5)
        ttk.Entry(self, textvariable=self.date_emprunt_var).grid(row=2, column=1, padx=10, pady=5)

        ttk.Label(self, text="Date de retour:").grid(row=3, column=0, sticky="w", padx=10, pady=5)
        ttk.Entry(self, textvariable=self.date_retour_var).grid(row=3, column=1, padx=10, pady=5)

        ttk.Button(self, text="Valider", command=self.validate_form).grid(row=4, column=0, columnspan=2, pady=20)

    def validate_form(self):
        try:
            selected_membre_index = self.membre_combobox.current()
            selected_livre_index = self.livre_combobox.current()

            if selected_membre_index == -1 or selected_livre_index == -1:
                messagebox.showwarning("Attention", "Veuillez sélectionner un membre et un livre.")
                return

            membre_obj = self.membres[selected_membre_index]
            livre_obj = self.livres[selected_livre_index]
            date_emprunt = self.date_emprunt_var.get()
            date_retour = self.date_retour_var.get()

            # Création de l'objet Emprunt
            nouvel_emprunt = Emprunt(membre_obj, livre_obj, None, date_emprunt, date_retour)

            EmpruntData().create(nouvel_emprunt)
            messagebox.showinfo("Succès", "Emprunt créé avec succès!")
        except:
            messagebox.showinfo("Erreur", "Une erreur est survenue lors de la création de l'emprunt.")
