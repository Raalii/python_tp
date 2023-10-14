import tkinter as tk
from tkinter import ttk

class BaseView(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.title("Bibliothèque")
        self.geometry("600x450")
        self.grab_set()  # Rend cette fenêtre modale
        self.center_window()

    def center_window(self):
        # Récupère la position de la fenêtre parent
        parent_x = self.parent.winfo_x()
        parent_y = self.parent.winfo_y()

        # Récupère la largeur et la hauteur de la fenêtre actuelle
        window_width = self.winfo_width()
        window_height = self.winfo_height()

        # Calcule la position pour centrer la fenêtre actuelle par rapport à la fenêtre parent
        position_x = parent_x
        position_y = parent_y + 100

        # Positionne la fenêtre
        self.geometry(f"+{position_x}+{position_y}")
