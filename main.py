from bibliotheque import Bibliotheque
from data.auteurData import AuteurData
from data.empruntData import EmpruntData
from data.livreData import LivreData
from data.membreData import MembreData
from data.initBDD import initBDD
from model.auteur import Auteur


# Initialisation de la BDD
initBDD()

if __name__ == "__main__":
    bibliotheque = Bibliotheque()
