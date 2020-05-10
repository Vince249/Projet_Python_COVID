from django import forms


class LoginClientForm(forms.Form):
    id_client = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder': 'Identifiant'}))
    pwd_client = forms.CharField(label = '',widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))


class LoginAdminForm(forms.Form):
    id_admin = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder': 'Identifiant'}))
    pwd_admin = forms.CharField(label = '',widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))


def Functionchoice(a):
    liste=[]
    for i in range(a+1): liste.append((str(i),str(i)))
    return liste
class ProduitForm(forms.Form):

    SelPoivre = forms.ChoiceField(label="Sel/Poivre ",choices= Functionchoice(2))
    Epice = forms.ChoiceField(label="Epices ",choices= Functionchoice(1))
    Assaisonnements = forms.ChoiceField(label="Assaisonnements (Huile et vinaigre) ",choices= Functionchoice(2))

    Pomme_de_terre = forms.ChoiceField(label="Pomme de terre ",choices= Functionchoice(25))
    Tomate = forms.ChoiceField(label="Tomate ",choices= Functionchoice(20))

    Pomme = forms.ChoiceField(label="Pomme ",choices= Functionchoice(15))
    Citron = forms.ChoiceField(label="Tomate ",choices= Functionchoice(7))

    Frite = forms.ChoiceField(label="Frites-Surgelées ",choices= Functionchoice(5))
    Choucroute = forms.ChoiceField(label="Choucroute en Conserve ",choices= Functionchoice(6))
    Pate = forms.ChoiceField(label="Pâtes (500 g) ",choices= Functionchoice(15))
    Riz = forms.ChoiceField(label="Riz (500 g) ",choices= Functionchoice(8))

    Farine = forms.ChoiceField(label="Farine (kg) ",choices= Functionchoice(3))
    Sucre = forms.ChoiceField(label="Sucre (kg) ",choices= Functionchoice(2))
    Oeuf = forms.ChoiceField(label="Oeuf (unité de 6) ",choices= Functionchoice(3))
    Pain = forms.ChoiceField(label="Pain (Baguette) ",choices= Functionchoice(12))

    Lait = forms.ChoiceField(label="Lait (1L)",choices= Functionchoice(4))
    Beurre = forms.ChoiceField(label="Beurre (250g) ",choices= Functionchoice(8))
    Fromage = forms.ChoiceField(label="Fromage ",choices= Functionchoice(10))
    Creme = forms.ChoiceField(label="Crème fraiche (20 cl) ",choices= Functionchoice(10))
    Poulet = forms.ChoiceField(label="Poulet ",choices= Functionchoice(5))
    Poisson = forms.ChoiceField(label="Poisson ",choices= Functionchoice(5))

    MedKit= forms.ChoiceField(label="Kit-Médicaments (Doliprane et Anti-inflammatoire) ",choices= Functionchoice(10))
    Pilule = forms.ChoiceField(label="Pilule (plaquettes) ",choices= Functionchoice(3))
    KitSoin = forms.ChoiceField(label="Kit-Soin du corps (Savon et dentifrice) ",choices= Functionchoice(4))

    KitEntretien = forms.ChoiceField(label="kit-Entretien (Liquide vaisselle, lessive, javel) ",choices= Functionchoice(3))
    

class CreationForm(forms.Form):
    id_box = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder': 'Identifiant Foyer'}))
    Email = forms.CharField(label="",max_length = 254,widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    pwd = forms.CharField(label = '',widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    tel = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder': 'Téléphone'}))
    ville = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder': 'Ville'}))
    codeP = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder': 'Code Postal'}))
    adresse = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder': 'Adresse'}))
    latitude = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder': 'Latitude'}))
    longitude = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder': 'Longitude'}))
    nb_animal = forms.IntegerField(label = '',min_value=0,widget=forms.NumberInput(attrs={'placeholder': "Nombre d'animaux"}))
    nb_foyer = forms.IntegerField(label = '',min_value=0,widget=forms.NumberInput(attrs={'placeholder': "Nb personnes foyer"}))


class CreationPersonne(forms.Form):
    nom_box = forms.CharField(label="",required=True,widget=forms.TextInput(attrs={'placeholder': 'Nom'}))
    prenom_box = forms.CharField(label="",required=True,widget=forms.TextInput(attrs={'placeholder': 'Prénom'}))
    age_box = forms.IntegerField(label = '',required=True,min_value=0,widget=forms.NumberInput(attrs={'placeholder': 'Âge'}))

class Choix_Produit(forms.Form):
    #Liste de tout nos produits 
    Product_Choice = [
       ("",""),
       ('Frites','Frites'),
       ('Pate', 'Pate'),
       ('Epice', 'Epice'),
       ('SelPoivre','SelPoivre'),
       ('Assaisonnements','Assaisonnements'),
       ('Pomme_de_terre','Pomme_de_terre'),
       ('Tomate','Tomate'),
       ('Pomme','Pomme'),
       ('Citron','Citron'),
       ('Choucroute','Choucroute'),
       ('Riz','Riz'),
       ('Farine','Farine'),
       ('Sucre','Sucre'),
       ('Oeuf','Oeuf'),
       ('Pain','Pain'),
       ('Lait','Lait'),
       ('Beurre','Beurre'),
       ('Fromage','Fromage'),
       ('Creme','Creme'),
       ('Poulet','Poulet'),
       ('Poisson','Poisson'),
       ('MedKit','MedKit'),
       ('Pilule','Pilule'),
       ('KitSoin','KitSoin'),
       ('KitEntretien','KitEntretien'),
    ]
    Product_Choice.sort(key=lambda tup: tup[0]) #on les trie pour plus de lisibilité
    choix_produit = forms.ChoiceField(label="Choix du produit à afficher ", choices=Product_Choice)

