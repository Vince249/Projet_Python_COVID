Le projet vous est donné avec un environnement virtuel. Cependant, utilisant 2 OS différents au sein de l'équipe (MAC et Windows) nous avons dû nous adapter.\
\
En effet, afin d'accéder à cet environnement virtuel sur Windows il suffit de le sélectionner comme l'interpréteur Python puis d'ouvrir un nouveau terminal. Si celui-ci ne s'active pas, saisissez la commande suivante : virtual_environment/Scripts/activate.\
\
Sur MAC, nous avons dû créer un autre environnement virtuel car le fichier settings.json (dans le folder .vscode) exécute un fichier (python.exe) se trouvant dans le dossier "Scripts" qui est inexistant pour les utilisateurs de cet OS. Si ces derniers l'utilisaient, il se retrouvaient sans interpréteur python.\
Ainsi, afin d'utiliser cet autre environnement virtuel, il faut le faire manuellement via le terminal bash ou zsh, suivant ce que vous avez.\
Vérifiez d'être placé au bon endroit (regarder le chemin dans le terminal), vous devez être à la racine du dossier contenant le projet. Puis, écrivez la commande suivante : source virtual_environment_MAC/bin/activate.\
\
Si vous n'avez pas accès à l'environnement virtuel ou si vous ne souhaitez pas l'utiliser, vous devez installer les packages sur votre machine. Pour ce faire, saisissez la commande associée à cela pour installer les packages suivants : Django, Folium, Matplotlib, Numpy, Plotly, Pandas, Squarify.\
\
Enfin, pour lancer le serveur et accéder à l'interface web, il faut vous déplacer jusqu'au dossier contenenant le fichier "manage.py" grâce à la commande "cd chemin/vers/ce/dossier". Si vous êtes placé à la racine du dossier contenant le projet, cela devrait donc être : cd Projet_Python/. Après cela, vous pouvez le lancer le serveur.\
Pour lancer le serveur si vous êtes sur Windows écrivez : py manage.py runserver.\
Pour lancer le serveur si vous êtes sur MAC écrivez : python manage.py runserver.\
\
Vous pouvez désormais accéder à l'interface web en suivant les instructions données à la suite de cette commande.\
\
Afin d'accéder à l'interface client rapidement vous pouvez saisir l'identifiant "a" et le mot de passe "a" qui est un client que nous avons déjà crée.\
De même, afin d'accéder un l'interface administrateur, vous pouvez saisir l'identifiant "admin" et le mot de passe "admin".
