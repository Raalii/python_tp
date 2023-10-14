import tkinter as tk
from tkinter import ttk

from view.baseView import BaseView


class BaseForm(BaseView):
    def __init__(self, parent, title=""):
        super().__init__(parent)
        self.title(title)
        self.init_widgets()

    def init_widgets(self):
        """Méthode pour initialiser les widgets. À surcharger dans les sous-classes."""
        pass

    def create_label_entry(self, label_text, row, variable):
        """Crée un label et une entrée et les place dans la grille."""
        ttk.Label(self, text=label_text).grid(row=row, column=0, sticky="w", padx=10, pady=5)
        ttk.Entry(self, textvariable=variable).grid(row=row, column=1, padx=10, pady=5)

    def validate_form(self):
        """Méthode pour valider le formulaire. À surcharger dans les sous-classes."""
        pass