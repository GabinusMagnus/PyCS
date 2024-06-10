import sqlite3
import csv

# connexion à la base de données

connexion = sqlite3.connect('db_test.db')

# ouvrir le fichier .csv en écriture seule
testcsv = open('test.csv', 'w', newline='')

# objet pour écrire dans le fichier .csv 
ecrireCSV = csv.writer(testcsv)

# liste qui contiendra les valeurs corrspondant aux descripteurs login et mdp
liste_login_mdp = []
for i in connexion.execute('SELECT login, mdp FROM test').fetchall():
    liste_login_mdp.append(list(i))

# Ecrire les valeurs dans le fichier .csv
ecrireCSV.writerows(liste_login_mdp)

# Libération du fichier .csv et de la base de données
testcsv.close()
connexion.close()