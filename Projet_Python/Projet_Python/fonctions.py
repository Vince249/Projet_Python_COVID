from django.shortcuts import render
from django.shortcuts import redirect
from django.forms import formset_factory
from . import form
id_utilisateur = ""
nb_personne_foyer = 0

def Home(request):
    global id_utilisateur
    global nb_personne_foyer
    erreur=""
    id_utilisateur=""
    nb_personne_foyer=0
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


def Creation(request):
    erreur=""
    global id_utilisateur 
    global nb_personne_foyer
    if(request.method=='POST'):
        if(request.POST.get('creation')):
            FormCreation = form.CreationForm(request.POST)
            if(FormCreation.is_valid()):
                data = FormCreation.cleaned_data
                #vérifier si le forms est correctement rempli
                #si non, erreur = "ERREUR"
                #si oui, mettre id dans la variable globale, autoriser la redirection et remplir le JSON avec les valeurs
                #* Mettre les DATA dans le JSON
                id_utilisateur = data['id_box']
                nb_personne_foyer = data['nb_foyer']
                return redirect('Page_Detail')
    FormCreation = form.CreationForm()
    return render(request, 'HTML/creation_compte.html',{
        'erreur' : erreur,
        'Form_Creation' : FormCreation,
    })

def Details(request):

    if(request.method == 'POST'):
        if(request.POST.get('details')):
            FormSetDetails = formset_factory(form.CreationPersonne, extra=nb_personne_foyer)
            formset = FormSetDetails(request.POST)
            if(formset.is_valid()):
                for forms in formset:  
                    data=forms.cleaned_data
                    print("Personne :", data)
                    #* Mettre les DATA de chaque personne dans le JSON
                return redirect('Page_Commande')
    FormSetDetails = formset_factory(form.CreationPersonne, extra=nb_personne_foyer)
    return render(request, 'HTML/details.html',{
        'Form_Set' : FormSetDetails,
    })


def Admin(request):
    return render(request, 'HTML/admin.html',{
        'id_admin' : id_utilisateur,
    })