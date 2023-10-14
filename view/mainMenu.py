from tkinter import ttk

from view.auteur.auteurViewMenu import AuteurView
from view.baseView import BaseView
from view.emprunt.empruntView import EmpruntView
from view.livre.livreViewMenu import LivreView
from view.membre.membreView import MembreView


class MainMenu(BaseView):
    def __init__(self, parent):
        super().__init__(parent)
        self.create_widgets()
        self.center_on_screen()

    def create_widgets(self):
        """Créer les widgets pour le menu principal."""
        ttk.Label(self, text="Menu principal", font=("Arial", 20)).pack(pady=20)

        ttk.Button(self, text="Voir Auteur", command=self.open_auteur_menu).pack(pady=10)
        ttk.Button(self, text="Voir Livre", command=self.open_livre_menu).pack(pady=10)
        ttk.Button(self, text="Voir Emprunt", command=self.open_emprunt_menu).pack(pady=10)
        ttk.Button(self, text="Voir Membre", command=self.ouvrir_membre_menu).pack(pady=10)

    def open_auteur_menu(self):
        # Ouvrir la vue Auteur
        AuteurView(self)

    def open_livre_menu(self):
        # Ouvrir la vue Livre
        LivreView(self)

    def open_emprunt_menu(self):
        # Ouvrir la vue Emprunt
        EmpruntView(self)

    def ouvrir_membre_menu(self):
        # Ouvrir la vue Membre
        MembreView(self)

    def center_on_screen(self):
        self.master.after_idle(self._center_on_screen)

    def _center_on_screen(self):
        # Récupère la largeur et la hauteur de l'écran
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # Récupère la largeur et la hauteur de la fenêtre
        window_width = self.winfo_reqwidth()
        window_height = self.winfo_reqheight()

        # Calcule la position pour centrer la fenêtre sur l'écran
        position_x = (screen_width // 2) - (window_width // 2)
        position_y = (screen_height // 2) - (window_height)

        # Positionne la fenêtre
        self.geometry(f"+{position_x}+{position_y}")
