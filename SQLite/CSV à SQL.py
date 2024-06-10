import sqlite3
import csv

# connexion à la base de données
connexion = sqlite3.connect('db_test.db')

# ouvrir le fichier csv en lecture
testcsv = open('test.csv', 'r', newline='')


# tableau contenant login et mdp
tableau_login_mdp = []
rangee_tableau = 0
for rangee in list(csv.reader(testcsv)):
    tableau_login_mdp.append([rangee[0], rangee[1]]) # ajout de login et mdp dans une nouvelle rangée
    rangee_tableau += 1


# insertion dans la base de données de tous les login et mdp du fichier .CSV
for rangee in tableau_login_mdp:
    connexion.execute("INSERT INTO test (login, mdp) VALUES (?, ?);", (rangee[0], rangee[1]))
connexion.execute("SELECT * FROM test").fetchall()

# mise à jour du mot de passe des utilisateurs de la base données selon le fichier .CSV
for loginSQL in connexion.execute("SELECT login, mdp FROM test").fetchall():
    for loginCSV in tableau_login_mdp:
        # login est un tuple, contenant seulement le login, au format ('login', ).
        if loginSQL[0] == loginCSV[0] and loginSQL[1] != loginCSV[1]: # Si le mdp SQL est différent du mdp CSV
            connexion.execute("UPDATE test SET mdp = ? WHERE mdp = ?", (loginCSV[1], loginSQL[1])) # Remplacer le mdp SQL par le mdp CSV


connexion.commit()
connexion.close()