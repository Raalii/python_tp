import tkinter as tk
from tkinter import ttk, messagebox

from data.livreData import LivreData
from data.auteurData import AuteurData
from model.livre import Livre
from view.baseView import BaseView


class CreerLivreForm(BaseView):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Créer un livre")
        self.geometry("600x600")

        self.auteur_data = AuteurData()
        self.auteurs = self.auteur_data.get_all()  # Liste des objets Auteur

        self.create_widgets()

    def create_widgets(self):
        # Variables pour stocker les entrées
        self.titre_var = tk.StringVar()
        self.genre_var = tk.StringVar()
        self.annee_publication_var = tk.IntVar()
        self.selected_auteur = tk.StringVar()

        # Création des widgets
        ttk.Label(self, text="Titre:").grid(row=0, column=0, sticky="w", padx=10, pady=5)
        ttk.Entry(self, textvariable=self.titre_var).grid(row=0, column=1, padx=10, pady=5)

        ttk.Label(self, text="Genre:").grid(row=1, column=0, sticky="w", padx=10, pady=5)
        ttk.Entry(self, textvariable=self.genre_var).grid(row=1, column=1, padx=10, pady=5)

        ttk.Label(self, text="Année de publication:").grid(row=2, column=0, sticky="w", padx=10, pady=5)
        ttk.Entry(self, textvariable=self.annee_publication_var).grid(row=2, column=1, padx=10, pady=5)

        ttk.Label(self, text="Auteur:").grid(row=4, column=0, sticky="w", padx=10, pady=5)
        auteurs_noms = [f"{auteur.prenom} {auteur.nom}" for auteur in self.auteurs]
        self.auteur_combobox = ttk.Combobox(self, values=auteurs_noms, textvariable=self.selected_auteur)
        self.auteur_combobox.grid(row=4, column=1, padx=10, pady=5)

        ttk.Button(self, text="Valider", command=self.validate_form).grid(row=5, column=0, columnspan=2, pady=20)

    def validate_form(self):
        try:
            titre = self.titre_var.get()
            genre = self.genre_var.get()
            annee_publication = self.annee_publication_var.get()

            selected_index = self.auteur_combobox.current()
            if selected_index == -1:
                messagebox.showwarning("Attention", "Veuillez sélectionner un auteur.")
                return

            auteur_obj = self.auteurs[selected_index]

            print(type(auteur_obj))

            # Création de l'objet Livre
            nouveau_livre = Livre(None, titre, genre, annee_publication, "Dispo", auteur_obj)

            LivreData().create(nouveau_livre)
            messagebox.showinfo("Succès", "Livre créé avec succès!")
        except:
            messagebox.showinfo("Erreur", "Une erreur est survenue lors de la création du livre.")
