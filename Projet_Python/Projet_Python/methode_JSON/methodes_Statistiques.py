#File contenant toutes les méthodes liées à la page de la commune pour visualiser différentes données statistiques
#! SAVE dans le dossier "Projet_Python/Graphs_Stats/"

#! """ Import """
import numpy as np
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
import matplotlib.dates as mdates
import squarify #Pour le TreeMap
import os
import pandas as pd
from pandas import DataFrame
import datetime
from datetime import timedelta, date
from matplotlib.ticker import  MaxNLocator

import json
import plotly.express as px
import plotly.graph_objects as go
from plotly.offline import plot
import folium


#Dictionnaire de la quantité de chaque produit commandés depuis le début du site
#Utilisé dans les méthodes : Histo_Product() ; PieChart_Product() ;TreeMap_Product()
commandeJson = dict()


### Méthode mettant à jour le dictionnaire commandeJson
def ConvertToStatisticsUse():
    with open('./JSON/commandes_faites.json') as json_file: #On importe le fichier des commanes
        fichier = json.load(json_file)
        #print(fichier)
    json_file.close()
    #On va le travailler pour l'avoir sous le format : commandeJson = {"tomates" : 12, "pain" : 5, "riz": 9, "pate" : 6, "farine":4}
    for uneCommande in fichier["commandes"]:#Commande n°1
        #print("uneCommande => ", uneCommande)
        for unProduit in uneCommande:
            #SI Le produit est déjà dans notre dictionnaire final et ce n'est pas l'id ou la date ou le CP
            if(unProduit in commandeJson.keys() and unProduit != "id" and unProduit != "Date" and unProduit != "CP" and uneCommande[str(unProduit)] != "0"): 
                addValue = commandeJson[unProduit] + int(uneCommande[unProduit])
                commandeJson[unProduit] = addValue
            #Sinon si ce n'est pas l'id ou la date
            #Alors on l'ajoute au dico final
            elif(unProduit != "id" and unProduit != "Date" and unProduit != "CP" and uneCommande[str(unProduit)] != "0"):
                commandeJson[unProduit] = int(uneCommande[unProduit])
    #On trie le dictionnaire par ses valeurs d'une facon decroissante
    sorted(commandeJson.items(), key=lambda x: x[1], reverse=True) #reverse=True : Trie dansl l'ordre decroissant 
    #print("CommandesJSON",commandeJson)


### Méthode faisant l'Histogramme de la quantité de commande de chaque produit commandé depuis le début du site ###
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


### Méthode faisant le Diagramme circulaire (Pie Chart)amme de la quantité de commande de chaque produit commandé depuis le début du site ###
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
    

### Méthode faisant le TreeMap de tous les produits commandés (suivant leur quantité) depuis le début du site ###
#Site Web : https://jingwen-z.github.io/data-viz-with-matplotlib-series5-treemap/
def TreeMap_Product():
    if(os.path.isfile('assets/Image/TreeMap_Quantite-totale-produit.png')): #Si le fichier existe
        os.remove('assets/Image/TreeMap_Quantite-totale-produit.png')#Supprimer l'image actuelle
    #Slicing d'un dictionnaire : ici on garde le top 10 des produits (car le dictionnaire est déjà trié par ordre décroissant suivant ses valeurs)
    topTen = dict(list(commandeJson.items())[0:10]) #10 premiers elements du dictionnaire
    #print("TOP 10 :\n", topTen)
    colors = ['orangered', 'darkorange', 'gold','yellow','greenyellow','palegreen', 'turquoise','paleturquoise','lavender','pink']
    plt.figure(figsize=(8, 6))
    plt.rc('font', size=10) 
    squarify.plot(sizes = topTen.values(), label=topTen.keys(), alpha=0.7, color=colors)
    plt.axis('off')
    
    plt.title("TreeMap des quantités par produit pour les "+ str(len(topTen.keys())) +" produits les plus commandés") #Titre adapté si moins de 10 produits
    plt.savefig('assets/Image/TreeMap_Quantite-totale-produit.png', bbox_inches='tight') #rajouter : pad_inches = 0 si on ne veut aucune zone blanche
    plt.close()
    #plt.show()


### Méthode faisant un graphique du Nombre de commandes par jour depuis une date de début (fixée au : 2020-05-01) ###
def GraphTotalCommande():
    # On fait une liste des dates entre le 01/05 et aujourd'hui
    startdate = date(2020,5,1)#Date du début
    enddate = date.today()#Date d'aujourd'hui 
    listejours=[]#tableau de chaque date entre le début et aujourd'hui
    for n in range(int ((enddate - startdate).days)+1):
        listejours.append( (startdate + timedelta(n)).strftime("%Y-%m-%d"))
        #Save sous forme de string de la forme dd-mm-YYYY de toutes les dates de l'intervalle
    #on cherche le nb de commande par date
    #listejours = ['2020-05-01', '2020-05-02', '2020-05-03']

    #Beosin d'avoir un dico de la forme suivante pour utilisation de Panda : (DATES sous la forme YYYY-mm-dd et non dd-mm-YYYY)
    #dicoJourNmbCommande = {"Date":['01-05-2020', '02-05-2020', '03-05-2020', '04-05-2020', '05-05-2020', '06-05-2020', '07-05-2020', '08-05-2020', '09-05-2020'],
                            #"TotalCommandeJour" : [4,6,8,5,3,7,5,11,6],
                            #"TotalCommandeCumule":[4,10,18,23,26,33,38,49,55]}
    dicoJourNmbCommande = {"Date":listejours, "TotalCommandeJour":[], "TotalCommandeCumule":[]}

    with open('./JSON/commandes_faites.json') as json_file:
        fichier = json.load(json_file)
        listCommandes = fichier['commandes']
        cumulNbCommande = 0
        for day in listejours :
            total = 0
            for order in listCommandes :
                if(order["Date"] == day):
                    total += 1
            dicoJourNmbCommande["TotalCommandeJour"].extend([total])
            dicoJourNmbCommande["TotalCommandeCumule"].extend([cumulNbCommande + total])
            cumulNbCommande += total
    json_file.close()

    pandaJourCommande = DataFrame(dicoJourNmbCommande)
    #print(pandaJourCommande)
    pandaJourCommande['Date'] = pd.to_datetime(pandaJourCommande['Date'])
    myFig = pandaJourCommande.plot(x="Date", y="TotalCommandeCumule", x_compat=True,
                            kind='line',title="Graphique des commandes cumulées depuis le " + startdate.strftime(("%Y-%m-%d")),
                            grid=True, legend = False, figsize=(15,6), color='g')
    myFig.xaxis.set_major_locator(mdates.DayLocator(bymonthday=range(1,32,2)))
    myFig.get_figure().savefig('assets/Image/Cumule-Commandes.png', bbox_inches='tight')

### Méthode faisant un histogramme horizontal de la quantité commandée la semaine précédente selon les jours pour un produit ###
def Histo_ConsoProduit(NomProduit):
    if(os.path.isfile('assets/Image/HistoHorizontal_Quantite-Produit-Semaine.png')): #Si le fichier existe
        os.remove('assets/Image/HistoHorizontal_Quantite-Produit-Semaine.png')#Supprimer l'image actuelle
    
    with open('./JSON/commandes_faites.json') as json_file:
        fichier = json.load(json_file)
        commandes=fichier['commandes']

    df_Commande = pd.DataFrame(commandes,columns=["id","CP","Date","Choucroute","Farine","Frites","Oeuf","Pate","Poulet","SelPoivre","Epice","Assaisonnements","Pomme_de_terre","Tomate","Pomme","Citron","Riz","Sucre","Pain","Lait","Beurre","Fromage","Creme","Poisson","MedKit","Pilule","KitSoin","KitEntretien"])
    df_Commande['Date']= pd.to_datetime(df_Commande['Date']) #on convertit la colonne 'Date' en objet date
    print(df_Commande)
    valToday = datetime.datetime.today().weekday() #Valeur du jour actuel (commence à lundi avec lundi=0)
    startDate = date.today() - timedelta(days = valToday, weeks = 1)#On revient à lundi de la semaine dernière 
    endDate = startDate + timedelta(days = 6) #Renvoie au dimanche de la semaine dernière

    df_Semaine = df_Commande[df_Commande['Date'] >= pd.Timestamp(startDate)] #on ne selectionne que la semaine précédente
    df_Semaine = df_Semaine[df_Semaine['Date'] <= pd.Timestamp(endDate)]
    df_Semaine = df_Semaine.fillna(0) #NaN devient 0
    #print("\n\ndf_Semaine : \n", df_Semaine)
    #Convertion des quantité de string à int avec astype()
    #Groupe by date sur la semaine concernée
    #Sum des quantités des produits ayant le même nom pour 1 date précise
    df_GroupBy = df_Semaine.astype({NomProduit:int}).groupby('Date')[NomProduit].sum().reset_index()
    #On ajoute une colonne associant les dates au nom du jour de cette date
    df_GroupBy['Day'] = "days"
    for i in range(len(df_GroupBy.index)):
        df_GroupBy['Day'][i]= df_GroupBy['Date'][i].strftime('%A') # %A donne le nom du jour en entier (mais en anglais)
    
    #print("\n\ndf_Groupy : \n",df_GroupBy)
    df_GroupBy.plot(x='Day', y=NomProduit, kind='barh', figsize=(9,6), legend=False)
    plt.title("Diagramme de la consommation du produit : "+ NomProduit +"  sur la semaine précédente en fonction du jour ")
    plt.savefig('assets/Image/HistoHorizontal_Quantite-Produit-Semaine.png', bbox_inches='tight')
    plt.close()


def Arrondissement_Map(Product_name):
    with open('./JSON/arrondissements.geojson') as json_file:
        data_arrondissements = json.load(json_file)

    with open('./JSON/commandes_faites.json') as json_file:
        fichier = json.load(json_file)
        commandes=fichier['commandes']

    #on initialise les colonnes pour éviter que si le produit choisi n'a jamais été commandé le site plante car si on selectionne un produit qui n'a jamais été commandé et que la colonne n'existe pas, le dataframe bug
    df_temp = pd.DataFrame(commandes,columns=["id","CP","Date","Choucroute","Farine","Frites","Oeuf","Pate","Poulet","SelPoivre","Epice","Assaisonnements","Pomme_de_terre","Tomate","Pomme","Citron","Riz","Sucre","Pain","Lait","Beurre","Fromage","Creme","Poisson","MedKit","Pilule","KitSoin","KitEntretien"])
    df_temp['Date']= pd.to_datetime(df_temp['Date']) #on convertit la colonne 'Date' en objet date

    trente_jours_avant = date.today() - timedelta(days=30)
    df = df_temp[df_temp['Date'] >= pd.Timestamp(trente_jours_avant)] #on ne selectionne que les 30 derniers jours

    df = df.fillna(0) #si une commande contient certains produits mais pas d'autres, leur valeur dans le dataframe sera "NaN" et ne pourra être lu lors de la conversion en int
    
    #on fait un astype(dict) avec dict contenant le nom d'une colonne et un type pour convertir une colonne en un type particulier
    #chaque colonne de produit ayant une quantité de type str, on convertit la colonne voulu (=le produit selectionné) en int afin de pouvoir faire sum
    #on met le reset index pour conserver un dataframe, sinon on a un SeriesFrame
    #on groupy by CP et on compte dans chaque CP le nombre de produit commandés
    fig = go.Figure(px.choropleth_mapbox(df.astype({Product_name:int}).groupby('CP')[Product_name].sum().reset_index(), 
                    geojson=data_arrondissements, 
                    locations='CP', 
                    color=Product_name,
                    #color_continuous_scale="Viridis", #couleur peut etre changer surement
                    mapbox_style="carto-positron",
                    zoom=11, center = {"lat": 48.8534, "lon": 2.3488},
                    opacity=0.5,
                    labels={'quantite':'quantite de produit'},
                    ))
    

    fig.update_layout(autosize=False,
                    height=600,
                    width=830,
                    margin={"r":0,"t":0,"l":0,"b":0}
                    #title_text='Quantité du produit commandé par arrondissement',
                    )

    return plot(fig, output_type='div')


def Quantite_Client():
    if(os.path.isfile('assets/Image/Totaux_Personnes_Courbe.png')):
        os.remove('assets/Image/Totaux_Personnes_Courbe.png')#Supprimer l'image actuelle

    # Je veux montrer l'évolution du nb de personne avec un compte depuis le lancement du site, on va dire que le site est lancé le 01/05
    # On fait une liste des dates entre le 01/05 et aujourd'hui
    startdate = datetime.date(2020,5,1)
    enddate = datetime.date.today()
    listejours=[]
    for n in range(int ((enddate - startdate).days)+1):
        listejours.append( (startdate + timedelta(n)).strftime("%Y-%m-%d"))
    #on cherche le nb de client par date
    Liste_Totaux_Personnes = [0]
    #* On initialise le premier terme
    f=open('./JSON/infos_client.json')
    fichier = json.load(f)
    temp = fichier['foyers']
    for element in temp:
        if(element['Date']==startdate.strftime("%Y-%m-%d")):
            Liste_Totaux_Personnes[0]+=len(element['Personnes'])
    #* Maintenant on fait les autres dates
    for index_jour in range(1,len(listejours)):
        date_actu = listejours[index_jour]
        Liste_Totaux_Personnes.append(0)
        for element in temp:
            if(element['Date']==date_actu):
                Liste_Totaux_Personnes[index_jour]+=len(element['Personnes'])
        Liste_Totaux_Personnes[index_jour]+= Liste_Totaux_Personnes[index_jour-1]
    print('Liste', Liste_Totaux_Personnes)
    Data={
        'Jours' : listejours,
        'Totaux_Personnes':Liste_Totaux_Personnes
    }
    df=DataFrame(Data,columns=['Jours','Totaux_Personnes'])
    df['Jours']= pd.to_datetime(df['Jours'])
    fig = df.plot(x='Jours', y='Totaux_Personnes',figsize=(10,10),x_compat=True, 
                    title="Evolution du nombre d'utilisateur depuis le " + startdate.strftime(("%Y-%m-%d")))
    fig.xaxis.set_major_locator(mdates.DayLocator(bymonthday=range(1,32,2)))
    fig.get_figure().savefig('assets/Image/Totaux_Personnes_Courbe.png', bbox_inches='tight')


def EntrepotArrondissementTab():
    df=pd.DataFrame({ 'Arrondissement':[75001,75002,75003,75004,75005,75006,75007,75008,75009,75010,75011,75012,75013,75014,75015,75016,75017,75018,75019,75020],
    'N_tel_Entrepôt':['013075001','013075002','013075003','013075004','013075005','013075006','013075007','013075008',
    '013075009','013075010','013075011','013075012','013075013','013075014','013075015','013075016','013075017','0130750018','0130750019','013075020'],
    'Adresse':['151 Rue de Rivoli, 75001 Paris, France',
    '1 Galerie Vivienne, 75002 Paris, France',
    '53 Rue de Bretagne, 75003 Paris, France',
    '87 Rue Saint-Antoine, 75004 Paris, France',
    'La Libre Pensée, Rue des Fossés Saint-Jacques, 75005 Paris, France',
    '78 Rue Bonaparte, 75006 Paris, France',
    '144 Rue de Grenelle, 75007 Paris, France',
    '87 Boulevard Malesherbes, 75008 Paris, France',
    '10 Rue Chauchat, 75009 Paris, France',
    '1 Rue Pierre Bullet, 75010 Paris, France',
    '103 Boulevard Voltaire, 75011 Paris, France',
    '155 Avenue Daumesnil, 75012 Paris, France',
    '24 Rue Abel Hovelacque, 75013 Paris, France',
    '165 Avenue du Maine, 75014 Paris, France',
    '17 Rue du Docteur Jacquemaire Clemenceau, 75015 Paris, France',
    '57 Avenue Georges Mandel, 75116 Paris, France',
    '36 - 38 Rue de Saussure, 75017 Paris, France',
    '68 Rue Ordener, 75018 Paris, France',
    '9 Rue Adolphe Mille, 75019 Paris, France',
    '28 Rue de la Dhuis, 75020 Paris, France']
    })
    df.index = df.index + 1
    html = df.to_html(table_id='Entrepot', justify='center')
    return html


def EntrepotArrondissementMap():
    df=pd.DataFrame({'Arrondissement':[75001,75002,75003,75004,75005,75006,75007,75008,75009,75010,75011,75012,75013,75014,75015,75016,75017,75018,75019,75020],
                      'Latitude':[48.86251,48.86649,48.863673,48.85464,48.845443,48.850697,48.858125,48.877962,48.872873,48.871734,48.858916,48.841413,48.832375,48.832741,48.842268,48.863506,48.884682,48.892182,48.888404,48.868454],
                      'Longitude':[2.337419,2.340099,2.360845,2.362531,2.343935,2.332586,2.314873,2.315784,2.339604,2.358037,2.378265,2.388038,2.352903,2.32513,2.298531,2.279297,2.315886,2.34656,2.388472,2.404612],
                      'N_tel_Entrepôt':['013075001','013075002','013075003','013075004','013075005','013075006','013075007','013075008','013075009','013075010',
                                        '013075011','013075012','013075013','013075014','013075015','013075016','013075017','0130750018','0130750019','013075020'],
                      'Adresse':['151 Rue de Rivoli, 75001 Paris, France',
                                 '1 Galerie Vivienne, 75002 Paris, France',
                                 '53 Rue de Bretagne, 75003 Paris, France',
                                 '87 Rue Saint-Antoine, 75004 Paris, France',
                                 'La Libre Pensée, Rue des Fossés Saint-Jacques, 75005 Paris, France',
                                 '78 Rue Bonaparte, 75006 Paris, France',
                                 '144 Rue de Grenelle, 75007 Paris, France',
                                 '87 Boulevard Malesherbes, 75008 Paris, France',
                                 '10 Rue Chauchat, 75009 Paris, France',
                                 '1 Rue Pierre Bullet, 75010 Paris, France',
                                 '103 Boulevard Voltaire, 75011 Paris, France',
                                 '155 Avenue Daumesnil, 75012 Paris, France',
                                 '24 Rue Abel Hovelacque, 75013 Paris, France',
                                 '165 Avenue du Maine, 75014 Paris, France',
                                 '17 Rue du Docteur Jacquemaire Clemenceau, 75015 Paris, France',
                                 '57 Avenue Georges Mandel, 75116 Paris, France',
                                 '36 - 38 Rue de Saussure, 75017 Paris, France',
                                 '68 Rue Ordener, 75018 Paris, France',
                                 '9 Rue Adolphe Mille, 75019 Paris, France',
                                 '28 Rue de la Dhuis, 75020 Paris, France']
    })

    with open('./JSON/arrondissements.geojson') as json_file:
        data_arrondissements = json.load(json_file)

    locations = df[['Latitude', 'Longitude']]
    locationlist = locations.values.tolist()
    
    fig = folium.Figure(width=750, height=600)
    map = folium.Map(location=[48.8534, 2.3488], tiles='CartoDB positron', zoom_start=12).add_to(fig)   
    
    for point in range(0, len(locationlist)):
        folium.Marker(locationlist[point], popup=df['Adresse'][point],icon=folium.Icon(icon="cloud",color="red")).add_to(map) #on peut changer l'icone, j'ai mis celui-ci pour montrer que c'était possible
    folium.GeoJson(data_arrondissements,name='geojson',style_function=lambda x:{'fillColor': 'blue', 'color': 'blue'}).add_to(map)

    return fig._repr_html_()


### Méthode détaillant la quantité de produits commandés pour toutes les commandes faites le jour de consultation et détaillé par arrondissement ###
def DetailCommandeToday():
    listArrondissements = ["75001","75002","75003","75004","75005","75006","75007","75008","75009","75010",
                            "75011","75012","75013","75014","75015","75016","75017","75018","75019","75020"]

    dicoPorduitOneDay = {"Produit":[], "Quantite":[], "Arrondissement":[]}
    todayDate = date.today().strftime("%Y-%m-%d")
    #Lecture du fichier des commandes pour prendre celles du jour
    with open('./JSON/commandes_faites.json') as json_file: #./JSON/commandes_faites.json
        fichier = json.load(json_file)
        listCommandes = fichier['commandes']
        for arrondissement in listArrondissements :
            listProduit_UnArrondissement = dict()
            for order in listCommandes :
                if(order["Date"] == todayDate and order["CP"]== arrondissement):
                    for unProduit in order:
                        #SI Le produit est déjà dans notre dictionnaire de l'arrondissement et ce n'est pas l'id ou la date ou le CP
                        if(unProduit in listProduit_UnArrondissement.keys() and unProduit != "id" and unProduit != "Date" and unProduit != "CP"): 
                            addValue = listProduit_UnArrondissement[unProduit] + int(order[unProduit])
                            listProduit_UnArrondissement[unProduit] = addValue
                        #Sinon si ce n'est pas l'id ou la date ou le CP
                        #Alors on l'ajoute au dico final
                        elif(unProduit != "id" and unProduit != "Date" and unProduit != "CP"):
                            listProduit_UnArrondissement[unProduit] = int(order[unProduit])
            #On ajoute les clés (donc les produits) à la liste des produits           
            dicoPorduitOneDay['Produit'].extend(listProduit_UnArrondissement.keys())
            #On ajoute la quantité totale de chaque porduit pr cet arrondissement à la liste des quantités  
            dicoPorduitOneDay['Quantite'].extend(listProduit_UnArrondissement.values())
            dicoPorduitOneDay['Arrondissement'].extend([arrondissement]*len(listProduit_UnArrondissement.keys()))
        
    #Convertion en DataFrame pandas
    dataPandasFormat = pd.DataFrame(dicoPorduitOneDay)
    #Trie par ordre décroissant
    dataPandasFormat_Sorted_Desc = dataPandasFormat.sort_values(by="Quantite", ascending=False).reset_index(drop=True)
    #print("Sorted_Desc : \n", dataPandasFormat_Sorted_Desc)
    #Modification des colonnes en mettant les CP en index de colonne (utilisation de pivot)
    dataPandasFormat_Pivot = dataPandasFormat_Sorted_Desc.pivot("Produit","Arrondissement","Quantite")
    dataPandasFormat_Pivot = dataPandasFormat_Pivot.fillna(0) #Remplace tous les NaN par des 0
    #Sauvegarde du dataFrame sous forme de tableau html
    dataPandas_HtmlFormat = dataPandasFormat_Pivot.to_html(table_id='OrderOfTheDay', justify='center')
    return dataPandas_HtmlFormat


def Livraisons_Map():
    with open('./JSON/arrondissements.geojson') as json_file:
        data_arrondissements = json.load(json_file)

    with open('./JSON/livraisons.json') as json_file:
        fichier = json.load(json_file)
        liste_livraisons=fichier['liste_livraisons']

    #on initialise les colonnes pour éviter que si le produit choisi n'a jamais été commandé le site plante car si on selectionne un produit qui n'a jamais été commandé et que la colonne n'existe pas, le dataframe bug
    df_temp = pd.DataFrame(liste_livraisons)
    df_temp['Date_livraison']= pd.to_datetime(df_temp['Date_livraison']) #on convertit la colonne 'Date' en objet date

    df = df_temp[df_temp['Date_livraison'] >= pd.Timestamp(date.today())] #on ne veut qu'aujourd'hui puisqu'on veut les livraisons de la journée

    df = df.fillna(0) #si une commande contient certains produits mais pas d'autres, leur valeur dans le dataframe sera "NaN" et ne pourra être lu lors de la conversion en int
    
    #print("livraisons",df)
    
    #on met le reset index pour conserver un dataframe, sinon on a un SeriesFrame
    #on groupy by codeP et on compte dans chaque codeP le nombre de personne ayant passé une commande
    fig = go.Figure(px.choropleth_mapbox(df.groupby('codeP').count().reset_index(),
                    geojson=data_arrondissements, 
                    locations='codeP', 
                    color='id', #la couleur dépend du nombre de personne à livrer 
                    #color_continuous_scale="Viridis", #couleur peut etre changer surement
                    mapbox_style="carto-positron",
                    zoom=11, center = {"lat": 48.8534, "lon": 2.3488},
                    opacity=0.5,
                    labels={'id':'Nombre de livraison'},
                    ))
    

    fig.update_layout(autosize=False,
                    height=600,
                    width=830,
                    margin={"r":0,"t":0,"l":0,"b":0},
                    #title_text='Quantité du produit commandé par arrondissement',
                    )

    return plot(fig, output_type='div')