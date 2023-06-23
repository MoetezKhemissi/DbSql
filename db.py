import mysql.connector



def create_database():
    # Connexion à la base de données MySQL (sans spécifier de base de données)
    cnx = mysql.connector.connect(
        host='localhost',
        user='root',
        password='root'
    )

    # Création d'un curseur pour exécuter les requêtes SQL
    cursor = cnx.cursor()

    # Création de la base de données "kenza"
    cursor.execute("CREATE DATABASE IF NOT EXISTS kenza")

    # Fermeture du curseur et de la connexion à la base de données
    cursor.close()
    cnx.close()

def create_tables():
    # Connexion à la base de données "kenza"
    cnx = mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='kenza'
    )

    # Création d'un curseur pour exécuter les requêtes SQL
    cursor = cnx.cursor()

    # Création de la table "donnees_candidat" si elle n'existe pas déjà
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS donnees_candidat (
            ID INT PRIMARY KEY,
            Candidate_Name VARCHAR(255),
            Question VARCHAR(255),
            Réponse VARCHAR(255)
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS candidat (
            ID INT PRIMARY KEY,
            Candidate_Name VARCHAR(255),
            score INT,
            decision VARCHAR(255)
        )
    """)

    # Création de la table "donnees_candidat_linkedin" si elle n'existe pas déjà
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS donnees_candidat_linkedin (
            ID INT PRIMARY KEY,
            Candidate_Name VARCHAR(500),
            Profile VARCHAR(500),
            `Additional Info` TEXT,
            Experience VARCHAR(500),
            Education VARCHAR(500),
            Certifications VARCHAR(500),
            Skills VARCHAR(500),
            Recommendations VARCHAR(500),
            Interests VARCHAR(500),
            Projects VARCHAR(500),
            Courses VARCHAR(500)
        )
    """)

    # Fermeture du curseur et de la connexion à la base de données
    cursor.close()
    cnx.close()

# Appeler les fonctions pour créer la base de données et les tables
create_database()
create_tables()
