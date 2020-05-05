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
    test = [
        {'nom':"truc", 'age': "18"},
        {'nom':"pipo", 'age': "58"},
    ]
    return render(request, 'HTML/home.html',{
        'erreur' : erreur,
        'nom' : nom,
        'test' : test
    })


def Commande(request,nom_personne):
    return render(request, 'HTML/commande.html',{
        'nom_personne' : nom_personne
    })


