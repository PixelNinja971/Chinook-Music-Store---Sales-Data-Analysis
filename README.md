🎵 Chinook Music Store - Data Analysis Pipeline


Ce projet est une solution d'analyse de données automatisée pour le store Chinook. Il combine la puissance du SQL pour l'extraction de données complexes et la flexibilité de Python pour le traitement et la visualisation.

L'architecture du projet est modulaire : les requêtes métier sont isolées de la logique d'exécution pour permettre une maintenance facile et une évolution rapide des indicateurs.

📂 Structure du Projet

main.py : Point d'entrée du projet. Gère la connexion à la base et génère les graphiques.

fonctions.py (ou utils.py) : Contient les requêtes SQL et la logique de traitement des données.

Chinook.sqlite : La base de données relationnelle du store.

README.md : Documentation du projet.

🛠️ Stack Technique

Base de données : SQLite3

Analyse de données : Pandas

Visualisation : Matplotlib

Versionnage : Git / GitHub

📊 Analyses Disponibles

Le pipeline permet de visualiser instantanément :

Top 10 des ventes par titre de musique.

Chiffre d'affaires par pays pour identifier les marchés clés.

Performance des employés basée sur le volume de ventes total.

🚀 Installation et Utilisation

Cloner le dépôt :

Bash
git clone https://github.com/TonPseudo/Chinook-Project.git
cd "Chinook Project"
Installer les bibliothèques nécessaires :

Bash
pip install pandas matplotlib
Lancer l'analyse :

Bash
python main.py
💡 Ce que j'ai appris

Architecture logicielle modulaire (séparation des responsabilités).

Jointures SQL complexes (INNER JOIN) et agrégations (SUM, GROUP BY).

Manipulation de DataFrames avec Pandas.

Création de visuels impactants avec Matplotlib.