import sqlite3

def initBDD():
    """Fonction qui permet d'initialiser la base de données ainsi que les tables associés"""
    # Création base de données
    con = sqlite3.connect('TPFinal.db')

    # Créer un objet curseur
    curseur = con.cursor()

    # Création de la table "livre"
    curseur.execute('''
        CREATE TABLE IF NOT EXISTS livre (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titre TEXT NOT NULL,
            genre TEXT NOT NULL,
            anneePublication INTEGER NOT NULL,
            statut TEXT NOT NULL,
            idAuteur INT NOT NULL,
            FOREIGN KEY (idAuteur) REFERENCES auteur(numeroAuteur) ON DELETE CASCADE
        )
        ''')

    # Création de la table "auteur"
    curseur.execute('''
    CREATE TABLE IF NOT EXISTS auteur (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        numeroAuteur INTEGER,
        prenom TEXT NOT NULL,
        nom TEXT NOT NULL,
        adresse TEXT,
        date_naissance DATE
    )
    ''')

    # Création de la table "Membre"
    curseur.execute('''
    CREATE TABLE IF NOT EXISTS membre (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        numeroMembre INTEGER,
        prenom TEXT NOT NULL,
        nom TEXT NOT NULL,
        adresse TEXT,
        date_naissance DATE
    )
    ''')

    curseur.execute('''
        CREATE TABLE IF NOT EXISTS emprunt (
            idEmprunt INTEGER PRIMARY KEY AUTOINCREMENT,
            numeroMembre INTEGER NOT NULL,
            idLivre INTEGER NOT NULL,
            dateEmprunt DATE NOT NULL,
            dateRetourPrevue DATE NOT NULL,
            dateRetourReelle DATE,
            FOREIGN KEY (numeroMembre) REFERENCES membre(numeroMembre) ON DELETE CASCADE,
            FOREIGN KEY (idLivre) REFERENCES livre(id) ON DELETE CASCADE
        )
        ''')

    con.commit()
    con.close()