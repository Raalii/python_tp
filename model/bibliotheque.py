class Bibliotheque:
    def __init__(self, nom : str, adresse: str, numero_telephone : str):
        self.nom = nom
        self.adresse = adresse
        self.numero_telephone=numero_telephone

    def __str__(self):
        return f"Le nom de la bibliothèque est {self.nom}, je suis situé au {self.adresse} avec comme numéro {self.numero_telephone}"