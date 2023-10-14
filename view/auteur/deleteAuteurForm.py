import tkinter as tk
from tkinter import ttk, messagebox

from data.auteurData import AuteurData
from view.baseView import BaseView


class SupprimerAuteurForm(BaseView):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Supprimer un auteur")
        self.geometry("300x200")
        self.auteur_data = AuteurData()
        # Liste des auteurs
        self.auteurs = self.auteur_data.get_all()
        self.selected_auteur = tk.StringVar()

        self.init_widgets()

    def init_widgets(self):
        """Initialise les widgets."""
        ttk.Label(self, text="Sélectionnez un auteur à supprimer:").pack(pady=10)

        # Création du menu déroulant (ComboBox) pour la sélection des auteurs
        auteurs_noms = [f"{auteur.prenom} {auteur.nom}" for auteur in self.auteurs]
        self.combobox = ttk.Combobox(self, values=auteurs_noms, textvariable=self.selected_auteur)
        self.combobox.pack(pady=10)

        ttk.Button(self, text="Supprimer", command=self.confirm_delete).pack(pady=20)

    def confirm_delete(self):
        """Confirme la suppression de l'auteur sélectionné."""
        selected_index = self.combobox.current()
        if selected_index == -1:
            messagebox.showwarning("Attention", "Veuillez sélectionner un auteur à supprimer.")
            return

        response = messagebox.askyesno("Confirmation", "Êtes-vous sûr de vouloir supprimer cet auteur ?")
        if response:
            auteur_to_delete = self.auteurs[selected_index]
            self.auteur_data.delete(auteur_to_delete.id_auteur)
            messagebox.showinfo("Succès", "Auteur supprimé avec succès!")
            self.destroy()  # Ferme la fenêtre après la suppression
