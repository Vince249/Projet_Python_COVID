from django.shortcuts import render
from django.shortcuts import redirect

id_utilisateur = ""

def Home(request):
    global id_utilisateur
    erreur=""
    id_utilisateur=""

    if(request.method == 'POST'):
        if (request.POST.get("login_client")):
            id_client = request.POST['id_client']
            pwd_client = request.POST['pwd_client']
            if(id_client =='a' and pwd_client =="mdp"): #ici mettre vérification JSON
                #return redirect('/commande')
                #naviguer vers page commande sans paramètre par l'URL (on peut utiliser des variables globales)
                id_utilisateur = id_client
                return redirect('Page_Commande')
                #naviguer vers page commande sans paramètre sans l'URL (on peut utiliser des variables globales)
            else:
                erreur="Identifiant/Mot de passe client invalide"

        if (request.POST.get("login_admin")):
            id_admin = request.POST['id_admin']
            pwd_admin = request.POST['pwd_admin']
            if(id_admin =='adminid' and pwd_admin =="adminmdp"): #ici mettre vérification JSON
                id_utilisateur = id_admin
                return redirect('Page_Admin')
                #naviguer vers page commande sans paramètre sans l'URL (on peut utiliser des variables globales)
            else:
                erreur="Identifiant/Mot de passe admin invalide"


    return render(request, 'HTML/home.html',{
        'erreur' : erreur,
    })


def Commande(request):
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
        'nom_personne' : id_utilisateur,
        'product_List' : product_List
    })
        #mettre le nom du dico un peu même synthaxe que la ligne au dessus


def Creation(request):
    erreur=""
    global id_utilisateur 
    if(request.method=='POST'):
        #vérifier si le forms est correctement rempli
        #si non, erreur = "ERREUR"
        #si oui, mettre id dans la variable globale et autoriser la redirection et remplir le JSON avec les valeurs
        id_utilisateur = request.POST['id_box']
        return redirect('Page_Commande')
    return render(request, 'HTML/creation_compte.html',{
        'erreur' : erreur,
    })


def Admin(request):
    return render(request, 'HTML/admin.html',{
        'id_admin' : id_utilisateur,
    })