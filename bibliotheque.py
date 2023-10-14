import tkinter as tk
from view.mainMenu import MainMenu

class Bibliotheque:
    def __init__(self):
        root = tk.Tk()
        root.withdraw()  # Cacher la fenêtre racine
        app = MainMenu(root)
        app.center_window()
        root.mainloop()