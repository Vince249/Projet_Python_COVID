from django.shortcuts import render
from django.shortcuts import redirect

id_utilisateur=""
def Home(request):
    global id_utilisateur
    erreur=""
    id_utilisateur=""
    if(request.method == 'POST'):
        id = request.POST['id']
        pwd = request.POST['pwd']
        if(id=='a' and pwd =="mdp"): #ici mettre vérification JSON
            #return redirect('/commande')
            #naviguer vers page commande sans paramètre par l'URL (on peut utiliser des variables globales)
            id_utilisateur = id
            return redirect('Page_Commande')
            #naviguer vers page commande sans paramètre sans l'URL (on peut utiliser des variables globales)
        else:
            erreur="Identifiant/Mot de passe invalide"


    return render(request, 'HTML/home.html',{
        'erreur' : erreur,
    })


def Commande(request):
    return render(request, 'HTML/commande.html',{
        'id':id_utilisateur
    })

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


