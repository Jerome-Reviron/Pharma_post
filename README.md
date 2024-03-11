# Pharma_post

## Table des Matières
- [Introduction](#introduction)
- [Installation](#installation)
- [Utilisation](#utilisation)
- [Contribuer](#contribuer)
- [Licence](#licence)
- [Mise en place du projet Django](#projet_django)
- [ETL des Données de Flux depuis un CSV](#ETL_ODS_Flux.py)
- [Modèle Django - Flux](#models_Flux)
- [Vue Django - ETL_ODS_Flux](#views_ETL_ODS_Flux)
- [ETL des Données DWH depuis DataFrame df_flux](#ETL_DWH_Flux.py)

## Introduction <a name="introduction"></a>
Ce répertoire est conçu durant ma formation POEI Développeur Applicatif Python, afin d'intégrer l'entreprise Pharma Pilot à Cournond'Auvergne.<br>
Accompagné par Human Booster et de nombreux intervenants, j'aurai à la suite de cette formation mon premier CDI de reconversion professionnelle Concepteur Développeur d'Applications.

## Installation <a name="installation"></a>
Ce répertoire à été installé durant la formation sur mon compte github personnel et a une visibilité public à des fins de collaborations optimales avec les collaborateurs, intervenants et collègues.

## Utilisation <a name="utilisation"></a>
Ce répertoire se dote d'un fichier "README.md" dans le but de proposer une explication de chaque code réalisé durant ce projet CAP ENTREPRISE.<br>
On aura donc dans le sommaire l'ajout permanent des liens vers les différentes partie de ce projet et les mise à jour de ses programmes.<br>
Ce projet est la conclusion de 3 mois d'apprentissage, est sera présenté à l'ensemble des parties mercredi 13 mars.

## Contribuer <a name="contribuer"></a>
Toutes personnes à une visibilité sur l'entièreté du répertoire. En revanche, aucune modification n'est possible.<br>
Les véritables contributions se font lors de nos échanges en direct ou en visio, durant tout l'apprentissage de cet emploi.<br>
De nombreux cours théoriques et pratiques sont réalisés pour consolider notre culture et employabilité.

## Licence <a name="licence"></a>
Tout droit réservé à moi même, Monsieur Reviron Jérôme.

# Mise en place du projet Django <a name="projet_django"></a>

### Création d’un nouveau repository GitHub
- Démarrez en créant un nouveau repository GitHub. Dans cet exemple, le repository est nommé Pharma_post.
- Créez un nouveau dossier dans le répertoire racine de votre choix.
- Ouvrez le dossier nouvellement créé avec Visual Studio Code.
- Dans le terminal de VS Code, exécutez la commande suivante pour cloner le repository GitHub dans votre dossier local :git clone https://github.com/Jerome-Reviron/Pharma_post.git.
- Fermez Visual Studio Code pour déplacer le fichier .git et le README.md du dossier Pharma_post à la racine du projet.
- Enfin, supprimez le dossier Pharma_post du répertoire.

### Création du fichier Dockerfile à la racine
- Créez un fichier Dockerfile à la racine du projet avec le contenu suivant :<br>
![Dockerfile](https://github.com/Jerome-Reviron/Pharma_post/blob/main/images_documentation/Dockerfile.png)

### Création du fichier docker-compose.yml à la racine
- Créez un fichier docker-compose.yml à la racine du projet avec un contenu de base.<br>
![docker-compose](https://github.com/Jerome-Reviron/Pharma_post/blob/main/images_documentation/docker-compose.png)

### Création du fichier requirements.txt à la racine
- Créez un fichier requirements.txt à la racine du projet avec le contenu suivant :<br>
![requirements](https://github.com/Jerome-Reviron/Pharma_post/blob/main/images_documentation/requirments.png)

### Commandes pour créer le projet Django
1. Exécutez la commande suivante pour créer un projet Django nommé Pharma_post : django-admin startproject Pharma_post
2. Vérifiez que vous êtes dans le bon répertoire avec la commande : cd Pharma_post
3. Si vous vous trouvez dans le répertoire : C:\Users\HB\Desktop\root\Pharma_post\Pharma_post >
4. Sinon remontez d'un cran avec la commande : cd ..
5. Ensuite, créez le dossier "app" avec la commande : python manage.py startapp app

### Commandes GitHub
1. Ajoutez tous les fichiers au suivi de Git : git add .
2. Effectuez un premier commit : git commit -m "Initial commit"
3. Poussez les changements vers la branche principale (main) : git push origin main
4. Créez une nouvelle branche "dev" : git checkout -b dev
5. Ajoutez et committez les modifications sur la branche "dev" : git add . et git commit -m "first commit on dev branch"
6. Poussez les changements vers la branche "dev" : git push origin dev

### Commande Docker

1. docker-compose build
2. docker-compose up
3. python manage.py makemigrations
4. python manage.py migrate

### Création settings.py

![settings_path](https://github.com/Jerome-Reviron/Pharma_post/blob/main/images_documentation/settings_DIR.png)<br>
![settings_installed_app](https://github.com/Jerome-Reviron/Pharma_post/blob/main/images_documentation/settings_INSTALLED_APPS.png)<br>
![settings_root_templates](https://github.com/Jerome-Reviron/Pharma_post/blob/main/images_documentation/settings_MIDDLEWARE.png)<br>
![settings_databases](https://github.com/Jerome-Reviron/Pharma_post/blob/main/images_documentation/settings_TEMPLATES.png)<br>
![settings_static](https://github.com/Jerome-Reviron/Pharma_post/blob/main/images_documentation/settings_DATABASES.png)<br>
![settings_static](https://github.com/Jerome-Reviron/Pharma_post/blob/main/images_documentation/settings_STATIC.png)<br>
![settings_static](https://github.com/Jerome-Reviron/Pharma_post/blob/main/images_documentation/settings_CONNEXION_API.png)<br>


# ETL des Données ODS depuis un CSV <a name="ETL_ODS_Flux.py"></a>

### Introduction:
Ce script Python réalise le processus d'Extraction, Transformation et Chargement (ETL) des données contenues dans un fichier CSV (`flux-total-dep.csv`) vers une base de données Django. Les données représentent des flux de vaccins, et le modèle Django utilisé est appelé `Flux`. Les étapes comprennent le chargement du fichier CSV, la troncature de la table `Flux`, la création d'objets `Flux` à partir des données du CSV, l'insertion en bloc dans la base de données à l'aide de `bulk_create`, et enfin, la récupération des données après l'insertion.

### Étapes détaillées:

1. Chargement du fichier CSV dans un DataFrame Pandas:
Le script utilise la bibliothèque Pandas pour lire le fichier CSV (`flux-total-dep.csv`) dans un DataFrame appelé `df`. Il spécifie le délimiteur, l'encodage et demande de ne pas traiter les valeurs manquantes comme des NaN.<br>

2. Troncature de la table `Flux`:
Toutes les entrées existantes dans la table `Flux` sont supprimées (tronquées) à l'aide de la méthode `delete()`.<br>

3. Création des objets `Flux` à partir du DataFrame:
Le script utilise une compréhension de liste avec `iterrows()` pour créer une liste d'objets `Flux`. Chaque ligne du DataFrame est convertie en un objet `Flux`.<br>

4. Insertion en bloc des objets `Flux` dans la base de données:
La liste d'objets `Flux` est insérée en bloc dans la base de données à l'aide de la méthode `bulk_create()`.<br>

5. Récupération des données après `bulk_create` dans un DataFrame:
Les données insérées dans la base de données sont récupérées dans un nouveau DataFrame Pandas appelé `df_Flux_apres_bulk_create` à l'aide de la méthode `from_records()`.<br>

6. Affichage des résultats:
Le script affiche des messages indiquant le nombre de lignes chargées depuis le fichier CSV, le nombre d'objets `Flux` créés, et une confirmation de l'insertion des objets `Flux` dans la base de données.<br>

7. Exécution du script:
Le script est exécuté si le fichier est lancé en tant que script principal (`__name__ == "__main__"`).<br>

# ETL des Données de Flux depuis un CSV <a name="ETL_ODS_Flux.py"></a>

Ce script Python, `ETL_ODS_Flux.py`, effectue le processus d'Extraction, Transformation et Chargement (ETL) des données contenues dans un fichier CSV vers la base de données Django en utilisant le modèle `Flux`.

### Introduction

Le script utilise Pandas pour lire un fichier CSV contenant des données sur les flux, puis les charge dans la base de données Django via le modèle `Flux`.

### Fonctionnalités

- **Chargement du CSV**:<br>
  Le script charge le fichier CSV `flux-total-dep.csv` dans un DataFrame Pandas.

- **Troncature de la Table Flux**:<br>
  La table `Flux` de la base de données Django est tronquée pour supprimer toutes les entrées existantes.

- **Création des Objets Flux**:<br>
  Des objets `Flux` sont créés à partir des données du DataFrame Pandas en utilisant une compréhension de liste avec `to_dict`.

- **Insertion en Bloc dans la Base de Données**:<br>
  Les objets `Flux` sont insérés en bloc dans la base de données en utilisant la méthode `bulk_create` pour optimiser les performances d'insertion.

- **Récupération des Données Après l'Insertion**:<br>
  Les données insérées dans la base de données sont récupérées dans un nouveau DataFrame Pandas après l'opération `bulk_create`.

### Utilisation

1. Assurez-vous d'avoir un fichier CSV nommé `flux-total-dep.csv` dans le répertoire `data`.
2. Exécutez le script `ETL_ODS_Flux.py`.

### Particularités

- **Optimisation des Performances**:<br>
  Le script utilise `bulk_create` pour optimiser l'insertion en bloc des objets `Flux` dans la base de données.

- **Utilisation de Django ORM**:<br>
  Les opérations de troncature, création d'objets et insertion sont effectuées en utilisant les fonctionnalités de Django ORM.

# Modèle Django - Flux <a name="models_Flux"></a> 

Le fichier `models.py` contient la définition du modèle Django pour représenter les données d'un flux. Ce modèle, appelé `Flux`, est utilisé pour structurer les informations extraites du fichier "flux-total". Les attributs du modèle correspondent aux différentes données du flux, telles que le code de la région, le libellé de la région, le code du département, le libellé du département, la date de fin de la semaine, le type de vaccin, le nombre d'unités de consommation directe du vaccin et le nombre total de doses du vaccin.

La méthode `__str__` du modèle est personnalisée pour renvoyer une représentation lisible du flux, comprenant le code de la région, le code du département et le type de vaccin.

### Introduction

Le fichier `models.py` définit le modèle Django appelé `Flux`, structurant les informations extraites du fichier "flux-total". Les attributs du modèle incluent des données essentielles telles que le code et le libellé de la région, le code et le libellé du département, la date de fin de la semaine, le type de vaccin, et les quantités de doses du vaccin.

### Fonctionnalités

La méthode `__str__` est implémentée pour fournir une représentation lisible du flux, incluant des informations clés telles que le code de la région, le code du département et le type de vaccin.

### Utilisations

Le modèle `Flux` est utilisé dans l'application Django pour structurer les données extraites du fichier "flux-total". Il offre une représentation claire et organisée des flux, facilitant ainsi la manipulation et l'affichage de ces données.

## Particularités

Aucune particularité spécifique n'est mentionnée pour le modèle `Flux` dans ce contexte.

# Vue Django - ETL_ODS_Flux <a name="views_ETL_ODS_Flux"></a> 

Le fichier `views.py` contient des fonctions de vue Django, dont la fonction principale est `ETL_ODS_Flux`. Cette fonction est responsable de l'extraction, de la transformation et du chargement (ETL) des données de flux dans le système Django. Voici une explication détaillée de chaque partie de la fonction :

- **Extraction des Flux de la Base de Données :** La fonction commence par extraire tous les flux de la base de données Django à l'aide de la requête `Flux.objects.all()`.

- **Pagination des Flux :** La pagination est ensuite appliquée pour afficher un nombre limité de flux par page. Cela est réalisé en utilisant la classe `Paginator` de Django, qui divise la liste complète des flux en pages.

- **Gestion des Pages :** La fonction gère différentes situations liées à la pagination, telles que la page demandée n'étant pas un entier ou si la page est hors de portée. Elle ajuste la page en conséquence pour garantir une expérience utilisateur fluide.

- **Rendu du Contexte :** Enfin, la fonction prépare un contexte contenant les flux paginés (`context = {'fluxs': fluxs}`) et rend la page `ETL_ODS_Flux.html` avec ce contexte.

### Introduction

Le fichier `views.py` contient des fonctions de vue Django, dont la fonction `ETL_ODS_Flux` est chargée d'effectuer le processus d'Extraction, de Transformation et de Chargement (ETL) des données de flux dans l'écosystème Django.

### Fonctionnalités

- **Extraction des Flux de la Base de Données :** Utilisation de la requête `Flux.objects.all()` pour extraire tous les flux de la base de données.

- **Pagination des Flux :** Application de la pagination pour afficher un nombre limité de flux par page, facilitant la navigation pour l'utilisateur.

- **Gestion des Pages :** Gestion des situations liées à la pagination, garantissant une expérience utilisateur sans accroc.

- **Rendu du Contexte :** Préparation d'un contexte contenant les flux paginés pour être rendu sur la page `ETL_ODS_Flux.html`.

### Utilisations

La fonction `ETL_ODS_Flux` est essentielle pour permettre à l'utilisateur de visualiser les flux paginés extraits de la base de données, facilitant ainsi le suivi et l'analyse des données.

### Particularités

Aucune particularité spécifique n'est mentionnée pour la fonction `ETL_ODS_Flux` dans ce contexte.

# ETL des Données DWH depuis DataFrame df_flux <a name="ETL_DWH_Flux.py"></a>

### Introduction

Ce script Python réalise un processus d'Extraction, Transformation et Chargement (ETL) des données à partir d'un DataFrame Pandas vers une base de données Django. Le modèle de données Django utilisé comprend les tables `Flux`, `D_TYPE_VACCIN`, `D_DATE`, `D_LOCATION`, et `F_FLUX`. Les données en question représentent des flux de vaccins, et le script effectue diverses opérations pour préparer et insérer ces données dans la base de données Django.

### Étapes détaillées

1. Chargement des DataFrames pour flux
Les données de la table `Flux` de la base de données sont extraites sous forme de dictionnaires à l'aide de la méthode `values()`.
Un DataFrame Pandas (`df_flux`) est créé à partir de ces données.<br>

2. Filtrage des lignes
Les lignes du DataFrame sont filtrées en utilisant la méthode `query()` pour exclure les valeurs "NA" dans les colonnes `nb_ucd` et `nb_doses`.
La longueur du DataFrame après l'application des filtres est affichée.<br>

3. Nettoyage des valeurs de la colonne 'type_de_vaccin'
Les valeurs de la colonne 'type_de_vaccin' sont nettoyées en supprimant les espaces et en les remplaçant par des underscores.<br>

4. Bulk create des enregistrements D_TYPE_VACCIN, gestion des doublons
Une liste unique des types de vaccin est créée à partir des valeurs uniques de la colonne 'type_de_vaccin'.
Toutes les données de la table `D_TYPE_VACCIN` sont supprimées (`truncate`) avant l'insertion.
Les objets `D_TYPE_VACCIN` sont créés à partir de la liste unique et insérés en bloc dans la base de données.<br>

5. Bulk create des enregistrements D_DATE, gestion des doublons
Une liste unique des dates est créée à partir des valeurs uniques de la colonne 'date_fin_semaine'.
Toutes les données de la table `D_DATE` sont supprimées (`truncate`) avant l'insertion.
Les objets `D_DATE` sont créés à partir de la liste unique et insérés en bloc dans la base de données.<br>

6. Bulk create des enregistrements D_LOCATION, gestion des doublons
Le DataFrame est prétraité en ajoutant un "0" devant chaque `code_departement` d'un seul chiffre.
Le DataFrame est trié selon les colonnes spécifiées.
Une colonne 'code_region_code_departement' est ajoutée au DataFrame.
Toutes les données de la table `D_LOCATION` sont supprimées (`truncate`) avant l'insertion.
Les objets `D_LOCATION` sont créés à partir des lignes triées du DataFrame et insérés en bloc dans la base de données.<br>

7. Tri du DataFrame principal et création d'objets F_FLUX
Le DataFrame principal (`df_flux_sorted`) est trié selon la clé primaire concaténée.
Une liste d'objets `F_FLUX` est créée à partir des lignes triées du DataFrame.<br>

8. Suppression des entrées existantes et insertion en bloc des objets F_FLUX
Toutes les entrées existantes dans la table `F_FLUX` sont supprimées.
Les objets `F_FLUX` sont insérés en bloc dans la base de données avec une transaction atomique pour garantir l'intégrité.
Des messages de progression sont affichés pendant l'insertion.<br>
