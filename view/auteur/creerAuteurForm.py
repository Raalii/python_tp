import tkinter as tk
from tkinter import ttk, messagebox
from data.auteurData import AuteurData
from model.auteur import Auteur
from view.baseView import BaseView


class CreerAuteurForm(BaseView):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Créer un auteur")
        self.geometry("300x240")

        # Variables pour stocker les entrées
        self.prenom_var = tk.StringVar()
        self.nom_var = tk.StringVar()
        self.adresse_var = tk.StringVar()
        self.date_naissance_var = tk.StringVar()
        self.numero_auteur_var = tk.IntVar()

        self.init_widgets()

    def init_widgets(self):
        """Initialise les widgets."""
        self.create_label_entry("Prénom:", 0, self.prenom_var)
        self.create_label_entry("Nom:", 1, self.nom_var)
        self.create_label_entry("Adresse:", 2, self.adresse_var)
        self.create_label_entry("Date de naissance:", 3, self.date_naissance_var)
        self.create_label_entry("Numéro d'auteur:", 4, self.numero_auteur_var)
        ttk.Button(self, text="Valider", command=self.validate_form).grid(row=5, column=0, columnspan=2, pady=20)

    def create_label_entry(self, label_text, row, variable):
        """Crée un label et une entrée et les place dans la grille."""
        ttk.Label(self, text=label_text).grid(row=row, column=0, sticky="w", padx=10, pady=5)
        ttk.Entry(self, textvariable=variable).grid(row=row, column=1, padx=10, pady=5)

    def validate_form(self):
        try:
            prenom = self.prenom_var.get()
            nom = self.nom_var.get()
            adresse = self.adresse_var.get()
            date_naissance = self.date_naissance_var.get()
            print(date_naissance)
            numero_auteur = self.numero_auteur_var.get()

            # Création de l'objet Auteur
            nouvel_auteur = Auteur(None, numero_auteur, prenom, nom, adresse, date_naissance)

            AuteurData().create(nouvel_auteur)
            messagebox.showinfo("Succès", "Auteur créé avec succès!")
            self.destroy()
        except:
            messagebox.showinfo("Erreur", "Une erreur est survenue")
