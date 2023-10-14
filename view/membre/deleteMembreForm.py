import tkinter as tk
from tkinter import ttk, messagebox

from data.membreData import MembreData
from view.baseView import BaseView


class SupprimerMembreForm(BaseView):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Supprimer un membre")
        self.geometry("300x240")
        self.membres_data = MembreData()
        self.membres = self.membres_data.get_all()
        self.selected_membre = tk.StringVar()

        self.init_widgets()


    def init_widgets(self):
        """Initialise les widgets."""
        ttk.Label(self, text="Sélectionnez un membre à supprimer:").pack(pady=10)

        # Création du menu déroulant (ComboBox) pour la sélection des auteurs
        membres_noms = [f"{membre.prenom} {membre.nom}" for membre in self.membres]
        self.combobox = ttk.Combobox(self, values=membres_noms, textvariable=self.selected_membre)
        self.combobox.pack(pady=10)

        ttk.Button(self, text="Supprimer", command=self.confirm_delete).pack(pady=20)

    def confirm_delete(self):
        """Confirme la suppression du membre sélectionné."""
        selected_index = self.combobox.current()
        if selected_index == -1:
            messagebox.showwarning("Attention", "Veuillez sélectionner un membre à supprimer.")
            return

        response = messagebox.askyesno("Confirmation", "Êtes-vous sûr de vouloir supprimer ce membre ?")
        if response:
            membre_to_delete = self.membres[selected_index]
            self.membres_data.delete(membre_to_delete.id)
            messagebox.showinfo("Succès", "Auteur supprimé avec succès!")
            self.destroy()  # Ferme la fenêtre après la suppression
