#File contenant toutes les méthodes liées à la page de la commune pour visualiser différentes données statistiques
#! SAVE dans le dossier "Projet_Python/Graphs_Stats/"

import numpy as np
import matplotlib.pyplot as plt

"""# Dataset"""
#Rappel :
#Data récupérées en sortie de commande : {'Qt_Pain': '2', 'Qt_Riz': '3', 'Qt_Farine': '0', 'Qt_Pommes': '6', 'Qt_lait': '10'}
#! Il faut un dataset de cette forme pour vouvir le convertir en DataFrame panda
commandeJson = {"tomates" : 12, "pain" : 5, "riz": 9, "pate" : 6, "farine":4}

### Histogramme de la quantité de commande de chaque produit ###

# Lien Web : 
# https://www.science-emergence.com/Articles/Simple-histogramme-avec-matplotlib/
# http://www.python-simple.com/python-matplotlib/histogram.php 

plt.bar(x=commandeJson.keys(), height=commandeJson.values(), align='center', color='b')
plt.grid(axis='y', alpha=0.75)
plt.xlabel('Produits')
plt.ylabel('Quantité totale')
plt.title('Histogramme des quantités totales commandées pour chaque produit')

plt.savefig("Projet_Python/Graphs_Stats/Histo_Quantite-totale-produit.png")
#Emplacement : D:\Programmes\Git-Hub_Projet\Projet-Python_A3
#!On peut préciser l'emplacement de stockage : plt.savefig('Sub Directory/graph.png')
plt.show() #! D'abord SAVE et ensuite SHOW


### Diagramme circulaire (Pie Chart) ###
#Site Web : Pie Chart : 
# https://www.science-emergence.com/Articles/Simple-diagramme-circulaire-avec-matplotlib/

plt.pie(commandeJson.values(), labels=commandeJson.keys(), autopct='%1.1f%%', shadow=True, startangle=90)
#Couleurs gérées automatiquement 
# (possibilité de forcer avec : myColors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']
#  et dans plt.pie() rajouter : colors = myColors MAIS que 4 couleurs
plt.axis('equal')
plt.title('Pie-Chart des quantités totales commandées pour chaque produit')

plt.savefig('Projet_Python/Graphs_Stats/Pie-Chart_Quantite-totale-produit.png')
plt.show()