from django.shortcuts import render
from django.shortcuts import redirect
from django.forms import formset_factory
import folium
from . import form
from .methode_JSON import methodes_JSON
from .methode_JSON import methodes_Statistiques
import json

#! Variables globales
id_utilisateur = ""
nb_personne_foyer = 0
FormCreation = form.CreationForm()
choix = "Frites" #choix par défaut
choix_commande = "Frites" #choix par défaut


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
                if(methodes_JSON.VerifClient(data['id_client'],data['pwd_client'])): #* faire une vérif JSON ici
                    id_utilisateur = data['id_client']
                    return redirect('Page_Commande')
                else:
                    erreur="Identifiant/Mot de passe client invalide"
        if(request.POST.get('login_admin')):
            FormLoginAdmin = form.LoginAdminForm(request.POST)
            if(FormLoginAdmin.is_valid()):
                data = FormLoginAdmin.cleaned_data
                if(methodes_JSON.VerifAdmin(data['id_admin'],data['pwd_admin'])): #* faire une vérif JSON ici
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


### Méthode déclanchant les actions liées à la création d'une commande par un utilisateur ###
def Commande(request):
    if(id_utilisateur!=""):
        message=''
        if(request.method == 'POST' and id_utilisateur!=""): #sécurité utilisateur connecté
            if(request.POST.get('Commande')):
                FormCommande = form.ProduitForm(request.POST)
                if(FormCommande.is_valid()):
                    data = FormCommande.cleaned_data
                    print('data', data)
                    #* Mettre les DATA dans le JSON
                    methodes_JSON.EnregistrerCommande(data, id_utilisateur) 
                    methodes_JSON.Remplissage_Livraison(data, id_utilisateur)
                    message='Commande réussie'
        FormProductList = form.ProduitForm()
        return render(request, 'HTML/commande.html',{
            'id_personne' : id_utilisateur,
            'Form_Product_List' : FormProductList,
            'message': message,
        })
    else: 
        erreur = "Accès refusé, vous devez être être connecté pour voir cette page"
        return render(request, 'HTML/acces_refuse.html',{
            'erreur' : erreur,
        })


def Allergie(request):
    if(id_utilisateur!=""):
        message = ''
        return render(request, 'HTML/allergie.html',{
            'message': message,
        })
    else: 
        erreur = "Accès refusé, vous devez être être connecté pour voir cette page"
        return render(request, 'HTML/acces_refuse.html',{
            'erreur' : erreur,
        })


def Creation(request):
    erreur=""
    global id_utilisateur 
    global nb_personne_foyer
    global FormCreation
    fig = folium.Figure(width=750, height=600)
    m = folium.Map(location=[48.8534, 2.3488], tiles='OpenStreetMap', zoom_start=10).add_to(fig) 

    if(request.method !='POST'):
        FormCreation = form.CreationForm()
    if(request.method=='POST'):
        if(request.POST.get('creation')):
            FormCreation = form.CreationForm(request.POST)
            if(FormCreation.is_valid()):
                data = FormCreation.cleaned_data
                print("data",data)
                #Vérifier unicité
                if(methodes_JSON.VerifUniciteClient(data['id_box'],data['latitude'],data['longitude'])):
                    #* Mettre les DATA dans le JSON
                    methodes_JSON.EnregistrerClient(data)
                    id_utilisateur = data['id_box']
                    nb_personne_foyer = data['nb_foyer']
                    return redirect('Page_Detail')
                erreur="Doublon d'un compte existant ou id déjà utilisé"
        if(request.POST.get('bouton')):
            FormCreation = form.CreationForm(request.POST)
            if(FormCreation.is_valid()):
                data = FormCreation.cleaned_data
                longitude = data['longitude']
                latitude = data['latitude']
                m= folium.Map(location=[latitude,longitude ],width=750, height=500,zoom_start=20)
                tooltip = 'Click me!'
                folium.Marker([latitude, longitude], popup='<i>Votre domicile</i>', tooltip=tooltip).add_to(m)
    m=m._repr_html_()
    
    return render(request, 'HTML/creation_compte.html',{
        'erreur' : erreur,
        'Form_Creation' : FormCreation,
        'map':m
    })
    

def Details(request):
    if(id_utilisateur!=""):
        FormSetDetails = formset_factory(form.CreationPersonne, extra=nb_personne_foyer)
        erreur=""
        if(request.method == 'POST'):
            if(request.POST.get('details')):
                FormSetDetails = formset_factory(form.CreationPersonne, extra=nb_personne_foyer)
                formset = FormSetDetails(request.POST)
                if(formset.is_valid()):
                    check=True
                    #! Vérification formset, on aurait aussi pu simplement modifier dans la library forms le fichier formset ligne 173 en mettant : defaults['empty_permitted'] = False              
                    for forms in formset:
                        
                        if (not forms.is_valid() or not forms.has_changed()) : 
                            check=False
                            erreur="Tous les champs doivent être remplis"
                    if(check):
                        for forms in formset:  
                            data=forms.cleaned_data
                            print("Personne :", data)
                            #* Mettre les DATA de chaque personne dans le JSON
                            methodes_JSON.EnregistrerPersonnes(data)
                        return redirect('Page_Commande')
                else:
                    erreur="Tous les champs doivent être remplis"   
        return render(request, 'HTML/details.html',{
            'Form_Set' : FormSetDetails,
            'erreur' : erreur
        })
    else:
        erreur = "Accès refusé, vous devez être avoir créé votre compte pour voir cette page"
        return render(request, 'HTML/acces_refuse.html',{
            'erreur' : erreur,
        })


### Méthode déclanchant les actions de consultation des données par l'administrateur (la commune) ###
def Admin(request):
    if(id_utilisateur=='admin'):
        m= folium.Map(location=[43.634, 1.433333],zoom_start=20)
        m=m._repr_html_()
        methodes_Statistiques.ConvertToStatisticsUse()#Convertion du tableau pour qu'il puisse être utilisé
        methodes_Statistiques.TreeMap_Product() #Création du TreeMap
        methodes_Statistiques.Quantite_Client() 
        methodes_Statistiques.GraphTotalCommande()
        html_entrepot = methodes_Statistiques.EntrepotArrondissementTab() #Création du contenu HTML pour affichage de la liste des entrepots de la ville dans la page HTML admin
        map_entrepot = methodes_Statistiques.EntrepotArrondissementMap()
        orderOfTheDay = methodes_Statistiques.DetailCommandeToday() #Création du contenu HTML pour affichage de la synthèse des commandes détailléees du jour dans la page HTML admin
        
        #selection du produit pour affichage personalisé de la map qui suit
        global choix
        if(request.method == 'POST'):
            if(request.POST.get('Bouton_Choix_Produit')):
                choix=request.POST['choix_produit']
        FormChoixProduit = form.Choix_Produit()

        map_produits = methodes_Statistiques.Arrondissement_Map(choix)
        map_livraison_du_jour = methodes_Statistiques.Livraisons_Map()
        

        global choix_commande
        if(request.method == 'POST'):
            if(request.POST.get('Bouton_Choix_Produit_Commande')):
                choix_commande=request.POST['choix_produit_commande']
                print(choix_commande)
        FormChoixProduitCommande = form.Choix_Produit_Commande()

        #html_graph = methodes_Statistiques.NomFonction(choix_commande) #fonction armand

        return render(request, 'HTML/admin.html',{
            'id_admin' : id_utilisateur,
            'map':m,
            'map_produits' : map_produits,
            'html_entrepot':html_entrepot,
            'orderOfTheDay':orderOfTheDay,
            'FormChoixProduit' : FormChoixProduit,
            'map_entrepot' : map_entrepot,
            'map_livraison_du_jour' : map_livraison_du_jour,
            'FormChoixProduitCommande' : FormChoixProduitCommande,
            #'html_graph' : html_graph -> fonction armand
        })
    else:
        erreur='Accès refusé, vous devez être admin pour voir cette page'
        return render(request, 'HTML/acces_refuse.html',{
            'erreur' : erreur,
        })
