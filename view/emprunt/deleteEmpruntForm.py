import tkinter as tk
from tkinter import ttk, messagebox
from data.empruntData import EmpruntData
from view.baseView import BaseView

class SupprimerEmpruntForm(BaseView):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Supprimer un emprunt")
        self.geometry("400x200")

        self.emprunt_data = EmpruntData()
        self.emprunts = self.emprunt_data.get_all()

        self.create_widgets()

    def create_widgets(self):
        # Variables pour stocker les entrées
        self.selected_emprunt = tk.StringVar()

        # Création des widgets
        ttk.Label(self, text="Sélectionnez un emprunt à supprimer:").pack(pady=10)

        emprunts_liste = [f"Emprunt {emprunt.id}: {emprunt.membre.prenom} {emprunt.membre.nom} - {emprunt.livre.titre}" for emprunt in self.emprunts]
        self.emprunt_combobox = ttk.Combobox(self, values=emprunts_liste, textvariable=self.selected_emprunt)
        self.emprunt_combobox.pack(pady=10)

        ttk.Button(self, text="Supprimer", command=self.confirm_delete).pack(pady=20)

    def confirm_delete(self):
        """Confirme la suppression de l'emprunt sélectionné."""
        selected_index = self.emprunt_combobox.current()
        if selected_index == -1:
            messagebox.showwarning("Attention", "Veuillez sélectionner un emprunt à supprimer.")
            return

        response = messagebox.askyesno("Confirmation", "Êtes-vous sûr de vouloir supprimer cet emprunt ?")
        if response:
            emprunt_to_delete = self.emprunts[selected_index]
            self.emprunt_data.delete(emprunt_to_delete.id)
            messagebox.showinfo("Succès", "Emprunt supprimé avec succès!")
            self.destroy()  # Ferme la fenêtre après la suppression
