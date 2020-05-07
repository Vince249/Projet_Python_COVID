from django import forms

#On intéragira avec cette variable globale en changeant la valeur de quantite_Max si on veut adapter le nb à la taille de la famille
product_List = [
        {'nom':"Pain", 'quantite_Max': 5},
        {'nom':"Riz", 'quantite_Max': 10},
        {'nom':"Farine", 'quantite_Max': 15},
        {'nom':"Pommes", 'quantite_Max': 8},
        {'nom':"Lait", 'quantite_Max': 12},
    ]

product_List_Condiment = [
    {'nom':"Sel/Poivre", 'quantite_Max': 2},
    {'nom':"Epice", 'quantite_Max': 1},
    {'nom':"Assaisonnements (Huile et vinaigre)", 'quantite_Max': 2},
]

product_List_Legume=[
    {'nom':"Pomme de terre", 'quantite_Max': 25},
    {'nom':"Tomate", 'quantite_Max': 20},
]

product_List_Fruit=[
    {'nom':"Pomme", 'quantite_Max': 15},
    {'nom':"Citron", 'quantite_Max': 7},
]
product_List_Conservation = [
    {'nom':"Frites-Surgelées", 'quantite_Max': 5},
    {'nom':"Choucroute en Conserve", 'quantite_Max': 6},
    {'nom':"Pâtes (500 g)", 'quantite_Max': 15},
    {'nom':"Riz (500 g)", 'quantite_Max': 8},
]
product_List_MatierePremiere = [
    {'nom':"Farine (kg)", 'quantite_Max': 3},
    {'nom':"Sucre (kg)", 'quantite_Max': 2},
    {'nom':"Oeuf (unité de 6)", 'quantite_Max': 3},
    {'nom':"Pain (Baguette)", 'quantite_Max': 12},
]
product_List_Laitier_Viande=[
    {'nom':"Beurre (250g)", 'quantite_Max': 8},
    {'nom':"Fromage", 'quantite_Max': 10},
    {'nom':"Crème fraiche (20 cl)", 'quantite_Max': 10},
    {'nom':"Poulet", 'quantite_Max': 5},
    {'nom':"Poisson", 'quantite_Max': 5},
]
product_List_HygieneSante=[
    {'nom':"Kit-Médicaments (Doliprane et Anti-inflammatoire", 'quantite_Max': 10},
    {'nom':"Pilile (plaquettes)", 'quantite_Max': 3},
    {'nom':"Kit-Soin du corps (Savon et dentifrice)", 'quantite_Max': 4},
]
product_List_Entretien=[
    {'nom':"kit-Entretien (Liquide vaisselle, lessive, javel)", 'quantite_Max': 3},
]


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
    Qt_Pain = forms.ChoiceField(choices= Functionchoice(product_List[0]['quantite_Max']))
    Qt_Riz = forms.ChoiceField(choices= Functionchoice(product_List[1]['quantite_Max']))
    Qt_Farine = forms.ChoiceField(choices= Functionchoice(product_List[2]['quantite_Max']))
    Qt_Pommes = forms.ChoiceField(choices= Functionchoice(product_List[3]['quantite_Max']))
    Qt_lait = forms.ChoiceField(choices= Functionchoice(product_List[4]['quantite_Max']))

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
    nom_box = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder': 'Nom'}))
    prenom_box = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder': 'Prénom'}))
    age_box = forms.IntegerField(label = '',min_value=0,widget=forms.NumberInput(attrs={'placeholder': 'Âge'}))

