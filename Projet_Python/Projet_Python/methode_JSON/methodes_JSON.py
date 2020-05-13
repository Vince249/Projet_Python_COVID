#Mettre ici les méthodes de lecture/écriture JSON
# Python program to update 
# JSON 

from datetime import datetime
import json 
from datetime import date,timedelta


# function to add to JSON 
def write_json(data, filename):
	with open(filename,'w') as f:
		json.dump(data, f, indent=4)
	return


def EnregistrerClient(data):
	with open('./JSON/infos_client.json') as json_file:
		fichier = json.load(json_file)
		temp = fichier['foyers']
		data['Personnes']=[]
		today = date.today()
		data['Date']=today.strftime("%Y-%m-%d")
		temp.append(data)
	write_json(fichier,'./JSON/infos_client.json')
	return


def EnregistrerPersonnes(data):
	with open('./JSON/infos_client.json') as json_file:
		fichier = json.load(json_file)
		temp = fichier['foyers']
		temp[len(temp)-1]['Personnes'].append(data)
	write_json(fichier,'./JSON/infos_client.json')
	return


### Méthode ajoutant la commande passée par un client à la BDD des commandes effectuées ###
def EnregistrerCommande(data, id):
	#récupération CP de la personne ayant commandé (utile pour la partie admin)
	CP=""
	with open('./JSON/infos_client.json') as json_file:
		fichier = json.load(json_file)
		temp = fichier['foyers']
		for element in temp:
			if (element["id_box"]==id): CP = element["codeP"]
  
	with open('./JSON/commandes_faites.json') as json_file:
		fichier = json.load(json_file)
		temp = fichier['commandes']
		datacleaned={}
		for k,v in data.items():
			if (v != '0'):
				datacleaned[k]=v
		datacleaned['id']=id
		datacleaned['CP']=CP
		datacleaned['Date'] = (datetime.now()).strftime("%Y-%m-%d") #Ajout de la date au format YYYY-mm-dd 
		
		temp.append(datacleaned)
	write_json(fichier,'./JSON/commandes_faites.json')
	return


### Méthode créant la livraison associé à la commande venant d'être passée. Nous avons fixer le jour de livraison à j+1 par rapport à la date de la commande ###
def Remplissage_Livraison(data,id):
	#initialisation des données que l'on veut récupérer
	tel=""
	ville=""
	codeP=""
	adresse=""
	produits_commande={}

	#commande à livrer
	for k,v in data.items():
			if (v != '0'):
				produits_commande[k]=v

	#on donne la valeur qu'il faut aux données initialisées précédemment
	with open('./JSON/infos_client.json') as json_file:
		fichier = json.load(json_file)
		temp = fichier['foyers']
		for element in temp:
			if (element["id_box"]==id): 
				tel = element["tel"]
				ville=element["ville"]
				codeP=element["codeP"]
				adresse=element["adresse"]
	
  
	with open('./JSON/livraisons.json') as json_file:
		fichier = json.load(json_file)
		temp = fichier['liste_livraisons']
		datacleaned={}
		datacleaned['id']=id
		datacleaned['tel']=tel
		datacleaned['ville']=ville
		datacleaned['codeP']=codeP
		datacleaned['adresse']=adresse
		datacleaned['Date_livraison'] = (date.today() + timedelta(days=1)).strftime("%Y-%m-%d") #Ajout de la date au format YYYY-mm-dd -> par défaut on dit que la livraison se fait au jour j+1 par rapport à la date de la commande
		datacleaned['produits_commande']=produits_commande

		temp.append(datacleaned)
	write_json(fichier,'./JSON/livraisons.json')
	return


### Méthode vérifiant si l'Id et le password entrés par le client sont dans la base de données clients ###
def VerifClient(id,pwd):
	with open('./JSON/infos_client.json') as json_file:
		fichier = json.load(json_file)
		temp=fichier['foyers']
		check = False
		for element in temp:
			if(element['id_box']==id and element['pwd']==pwd): 
				check=True
				break
	return check


### Méthode vérifiant si l'Id et le password entrés par l'admin sont dans la base de données admin ###
def VerifAdmin(id,pwd):
	with open('./JSON/admin_login.json') as json_file:
		fichier = json.load(json_file)
		temp=fichier['admin']
		check = False
		for element in temp:
			if(element['id']==id and element['pwd']==pwd): check=True
	return check

def VerifUniciteClient(id,latitude,longitude):
	with open('./JSON/infos_client.json') as json_file:
		fichier = json.load(json_file)
		temp=fichier['foyers']
		check = True
		for element in temp:
			if(element['id_box']==id or (element['latitude']==latitude and element['longitude']==longitude)): check=False
	return check