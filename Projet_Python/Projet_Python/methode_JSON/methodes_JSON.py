#Mettre ici les méthodes de lecture/écriture JSON
# Python program to update 
# JSON 


import json 

# function to add to JSON 
def write_json(data, filename):
	with open(filename,'w') as f:
		json.dump(data, f, indent=4)
	return

def EnregistrerClient(data):
	with open('./JSON/infos_client.json') as json_file:
		fichier = json.load(json_file)
		temp = fichier['foyers']
		temp.append(data)
		temp[len(temp)-1]['Personnes']=[]
	write_json(fichier,'./JSON/infos_client.json')
	return

def EnregistrerPersonnes(data):
	with open('./JSON/infos_client.json') as json_file:
		fichier = json.load(json_file)
		temp = fichier['foyers']
		temp[len(temp)-1]['Personnes'].append(data)
	write_json(fichier,'./JSON/infos_client.json')
	return

def EnregistrerCommande(data, id):
	with open('./JSON/commandes_faites.json') as json_file:
		fichier = json.load(json_file)
		temp = fichier['commandes']
		#print("1",data)
		datacleaned={}
		for k,v in data.items():
			if v != '0':
				datacleaned[k]=v
		print("Foramt de la commande : \n",datacleaned)
		datacleaned['id']=id
		temp.append(datacleaned)
	write_json(fichier,'./JSON/commandes_faites.json')
	return

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

def VerifAdmin(id,pwd):
	with open('./JSON/admin_login.json') as json_file:
		fichier = json.load(json_file)
		temp=fichier['admin']
		check = False
		for element in temp:
			if(element['id']==id and element['pwd']==pwd): check=True
	return check