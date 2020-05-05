from django.shortcuts import render

def Home(request):
    nom=""
    erreur=""
    if(request.method == 'POST'):
        id = request.POST['id']
        pwd = request.POST['pwd']
        # Accepté dans JSON ?
        # si accepté, erreur="", nom = Nom de la personne
        # si refusé, erreur = "Identifiant/Mot de passe invalide", nom="
        erreur = ""
        nom=id

    return render(request, 'HTML/home.html',{
        'erreur' : erreur,
        'nom' : nom,        
    })



def Commande(request,nom_personne):
    #METTRE ICI le dictionnaire
    #! Liste des produits proposés
    product_List = [
        {'nom':"Pain", 'quantite_Max': range(5)},
        {'nom':"Riz", 'quantite_Max': range(10)},
        {'nom':"Farine", 'quantite_Max': range(15)},
        {'nom':"Pommes", 'quantite_Max': range(8)},
        {'nom':"Lait", 'quantite_Max': range(12)},
    ]

    return render(request, 'HTML/commande.html',{
        'nom_personne' : nom_personne,
        'product_List' : product_List
        #mettre le nom du dico un peu même synthaxe que la ligne au dessus
    })


