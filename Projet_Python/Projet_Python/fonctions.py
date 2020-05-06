from django.shortcuts import render
from django.shortcuts import redirect
from . import form
id_utilisateur = ""


def Home(request):
    global id_utilisateur
    erreur=""
    id_utilisateur=""
    if(request.method == 'POST'):
        if(request.POST.get('login_client')):
            FormLoginClient = form.LoginClientForm(request.POST)
            if(FormLoginClient.is_valid()):
                data = FormLoginClient.cleaned_data
                if(data['id_client'] =='a' and data['pwd_client'] =="mdp"): #faire une vérif JSON ici
                    id_utilisateur = data['id_client']
                    return redirect('Page_Commande')
                else:
                    erreur="Identifiant/Mot de passe client invalide"
        if(request.POST.get('login_admin')):
            FormLoginAdmin = form.LoginAdminForm(request.POST)
            if(FormLoginAdmin.is_valid()):
                data = FormLoginAdmin.cleaned_data
                if(data['id_admin']=='admin' and data['pwd_admin']=='mdp'): #faire une vérif JSON ici
                    id_utilisateur = data['id_admin']
                    return redirect('Page_Admin')
                else:
                    erreur="Identifiant/Mot de passe admin invalide"
    FormLoginAdmin = form.LoginAdminForm()
    FormLoginClient = form.LoginClientForm()
    return render(request, 'HTML/home.html',{
        'erreur' : erreur,
        'Form_Login_Client' : FormLoginClient,
        'Form_Login_Admin' : FormLoginAdmin,
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