import tkinter as tk
from tkinter import ttk, messagebox

from data.livreData import LivreData
from view.baseView import BaseView


class SupprimerLivreForm(BaseView):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Supprimer un livre")
        self.geometry("400x200")
        self.livre_data = LivreData()

        # Liste des livres
        self.livres = self.livre_data.get_all()
        self.selected_livre = tk.StringVar()

        self.init_widgets()

    def init_widgets(self):
        """Initialise les widgets."""
        ttk.Label(self, text="Sélectionnez un livre à supprimer:").pack(pady=10)

        # Création du menu déroulant (ComboBox) pour la sélection des livres
        livres_titres = [livre.titre for livre in self.livres]
        self.combobox = ttk.Combobox(self, values=livres_titres, textvariable=self.selected_livre)
        self.combobox.pack(pady=10)

        ttk.Button(self, text="Supprimer", command=self.confirm_delete).pack(pady=20)

    def confirm_delete(self):
        """Confirme la suppression du livre sélectionné."""
        selected_index = self.combobox.current()
        if selected_index == -1:
            messagebox.showwarning("Attention", "Veuillez sélectionner un livre à supprimer.")
            return

        response = messagebox.askyesno("Confirmation", "Êtes-vous sûr de vouloir supprimer ce livre ?")
        if response:
            livre_to_delete = self.livres[selected_index]
            self.livre_data.delete(livre_to_delete.id)
            messagebox.showinfo("Succès", f"Livre '{livre_to_delete.titre}' supprimé avec succès!")
            self.destroy()  # Ferme la fenêtre après la suppression
