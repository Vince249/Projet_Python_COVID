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
                if(data['id_client'] =='a' and data['pwd_client'] =="mdp"): #* faire une vérif JSON ici
                    id_utilisateur = data['id_client']
                    return redirect('Page_Commande')
                else:
                    erreur="Identifiant/Mot de passe client invalide"
        if(request.POST.get('login_admin')):
            FormLoginAdmin = form.LoginAdminForm(request.POST)
            if(FormLoginAdmin.is_valid()):
                data = FormLoginAdmin.cleaned_data
                if(data['id_admin']=='admin' and data['pwd_admin']=='mdp'): #* faire une vérif JSON ici
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
    message=''
    if(request.method == 'POST'):
        if(request.POST.get('Commande')):
            FormCommande = form.ProduitForm(request.POST)
            if(FormCommande.is_valid()):
                data = FormCommande.cleaned_data
                #* Mettre les DATA dans le JSON
                message='Commande réussie'
    FormProductList = form.ProduitForm()
    return render(request, 'HTML/commande.html',{
        'id_personne' : id_utilisateur,
        'Form_Product_List' : FormProductList,
        'message': message,
    })

def Allergie(request):
    message = ''
    return render(request, 'HTML/allergie.html',{
        'message': message,
    })


def Creation(request):
    erreur=""
    global id_utilisateur 
    if(request.method=='POST'):
        #vérifier si le forms est correctement rempli
        #si non, erreur = "ERREUR"
        #si oui, mettre id dans la variable globale et autoriser la redirection et remplir le JSON avec les valeurs
        #* Mettre les DATA dans le JSON
        id_utilisateur = request.POST['id_box']
        return redirect('Page_Commande')
    return render(request, 'HTML/creation_compte.html',{
        'erreur' : erreur,
    })


def Admin(request):
    return render(request, 'HTML/admin.html',{
        'id_admin' : id_utilisateur,
    })