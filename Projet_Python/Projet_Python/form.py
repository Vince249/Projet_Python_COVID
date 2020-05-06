from django import forms

#On intéragira avec cette variable globale en changeant la valeur de quantite_Max si on veut adapter le nb à la taille de la famille
product_List = [
        {'nom':"Pain", 'quantite_Max': 5},
        {'nom':"Riz", 'quantite_Max': 10},
        {'nom':"Farine", 'quantite_Max': 15},
        {'nom':"Pommes", 'quantite_Max': 8},
        {'nom':"Lait", 'quantite_Max': 12},
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
