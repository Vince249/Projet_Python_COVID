#File contenant toutes les méthodes liées à la page de la commune pour visualiser différentes données statistiques
#! SAVE dans le dossier "Projet_Python/Graphs_Stats/"

#! """ Import """
import numpy as np
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
import squarify #Pour le TreeMap
import os
from pandas import DataFrame
from datetime import datetime,timedelta
import json

#! """ Dataset"""
#Rappel :
#Data récupérées en sortie de commande : {'Qt_Pain': '2', 'Qt_Riz': '3', 'Qt_Farine': '0', 'Qt_Pommes': '6', 'Qt_lait': '10'}
#! Il faut un dataset de cette forme pour vouvir le convertir en DataFrame panda
#commandeJson = {"tomates" : 12, "pain" : 5, "riz": 9, "pate" : 6, "farine":4}
commandeJson = dict()

def ConvertToStatisticsUse():
    with open('./JSON/commandes_faites.json') as json_file: #On importe le fichier des commanes
        fichier = json.load(json_file)
        print(fichier)
    #On va le travailler pour l'avoir sous le format : commandeJson = {"tomates" : 12, "pain" : 5, "riz": 9, "pate" : 6, "farine":4}
    for uneCommande in fichier["commandes"]:#Commande n°1
        print("uneCommande => ", uneCommande)
        for unProduit in uneCommande:
            #SI Le produit est déjà dans notre dictionnaire final et ce n'est pas l'id ou la date
            if(unProduit in commandeJson.keys() and unProduit != "id" and unProduit != "Date"): 
                addValue = commandeJson[unProduit] + int(uneCommande[unProduit])
                commandeJson[unProduit] = addValue
            #Sinon si ce n'est pas l'id ou la date
            #Alors on l'ajoute au dico final
            elif(unProduit != "id" and unProduit != "Date"):
                commandeJson[unProduit] = int(uneCommande[unProduit])

### Histogramme de la quantité de commande de chaque produit ###

# Lien Web : 
# https://www.science-emergence.com/Articles/Simple-histogramme-avec-matplotlib/
# http://www.python-simple.com/python-matplotlib/histogram.php 
def Histo_Product():
    if(os.path.isfile("assets/Image/Histo_Quantite-totale-produit.png")):
        os.remove("assets/Image/Histo_Quantite-totale-produit.png") #Supprimer l'image actuelle
    plt.bar(x=commandeJson.keys(), height=commandeJson.values(), align='center', color='b')
    plt.grid(axis='y', alpha=0.75)
    plt.xlabel('Produits')
    plt.ylabel('Quantité totale')
    plt.title('Histogramme des quantités totales commandées pour chaque produit')  
    
    plt.savefig("assets/Image/Histo_Quantite-totale-produit.png")
    #plt.show() #! D'abord SAVE et ensuite SHOW
    plt.close()#On ferme le plot sinon les figures se superposent et l'enregistrement est corrompu
    #Emplacement : D:\Programmes\Git-Hub_Projet\Projet-Python_A3
    #!On peut préciser l'emplacement de stockage : plt.savefig('Sub Directory/graph.png')
    


### Diagramme circulaire (Pie Chart) ###
#Site Web : Pie Chart : 
# https://www.science-emergence.com/Articles/Simple-diagramme-circulaire-avec-matplotlib/

def PieChart_Product():
    if(os.path.isfile('assets/Image/Pie-Chart_Quantite-totale-produit.png')):
        os.remove('assets/Image/Pie-Chart_Quantite-totale-produit.png')#Supprimer l'image actuelle
    plt.pie(commandeJson.values(), labels=commandeJson.keys(), autopct='%1.1f%%', shadow=True, startangle=90)
    #Couleurs gérées automatiquement 
    # (possibilité de forcer avec : myColors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']
    #  et dans plt.pie() rajouter : colors = myColors MAIS que 4 couleurs
    plt.axis('equal')
    plt.title('Pie-Chart des quantités totales commandées pour chaque produit')

    plt.savefig('assets/Image/Pie-Chart_Quantite-totale-produit.png')
    #plt.show()
    plt.close()#On ferme le plot sinon les figures se superposent et l'enregistrement est corrompu
    

### TreeMap ###
#Site Web : https://jingwen-z.github.io/data-viz-with-matplotlib-series5-treemap/

def TreeMap_Product():
    os.remove('assets/Image/TreeMap_Quantite-totale-produit.png')
    plt.rc('font', size=14)
    squarify.plot(sizes = commandeJson.values(), label=commandeJson.keys(), alpha=0.7)
    plt.axis('off')
    plt.title('TreeMap des quantités par produit')

    plt.savefig('assets/Image/TreeMap_Quantite-totale-produit.png')
    plt.close()

def Quantite_Client():
    # Je veux montrer l'évolution du nb de personne avec un compte depuis le lancement du site, on va dire que le site est lancé le 01/05
    # On fait une liste des dates entre le 01/05 et aujourd'hui
    startdate = datetime.date(2020,5,1)
    enddate = datetime.date.today()
    listejours=[]
    for n in range(int ((enddate - startdate).days)+1):
        listejours.append( (startdate + timedelta(n)).strftime("%d-%m-%Y"))
    #on cherche le nb de client par date
    '''
    for i in listejours:

    Data = { 'Date': listejours,
    'Qt_Clients':
    }
    '''
    pass