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
- [Modèle Django - D_TYPE_VACCIN](#models_D_TYPE_VACCIN)
- [Modèle Django - D_DATE](#models_D_DATE)
- [Modèle Django - D_LOCATION](#models_D_LOCATION)
- [Modèle Django - F_FLUX](#models_F_FLUX)
- [Vue Django - ETL_DWH_D_TYPE_VACCIN](#views_ETL_DWH_D_TYPE_VACCIN)
- [Vue Django - ETL_DWH_D_DATE](#views_ETL_DWH_D_DATE)
- [Vue Django - ETL_DWH_D_LOCATION](#views_ETL_DWH_D_LOCATION)
- [Vue Django - ETL_DWH_F_FLUX](#views_ETL_DWH_F_FLUX)
- [Interface Web - index.html](#UI_index)
- [Interface Web - ETL_Table](#UI_ETL_Table)
- [Interface Web - CSS](#CSS)
- [API Django - views.py](#API_Views.py)
- [API Django - serializers.py](#API_serializers.py)
- [API Django Authentification - views_auth.py](#API_views_auth.py)
- [API Django Authentification - LoginSerializers](#API_LoginSerializers)
- [API Django Authentification - login.html](#API_login.html)
- [API Django Authentification - views_register.py](#API_views_register.py)
- [API Django Authentification - register.html](#API_register.html)
- [API Django Authentification - views_out.py](#API_views_out.py)
- [API Django Authentification - tests.py](#API_tests.py)


# API Django Authentification - `LoginSerializers` <a name="API_LoginSerializers"></a>

## Introduction <a name="introduction"></a>
Ce répertoire est conçu durant ma formation POEI Développeur Applicatif Python, afin d'intégrer l'entreprise Pharma Pilot à Cournond'Auvergne.<br>
Accompagné par Human Booster et de nombreux intervenants, j'aurai à la suite de cette formation mon premier CDI de reconversion professionnelle Concepteur Développeur d'Applications et Développeur Applicatif Python.

## Installation <a name="installation"></a>
Ce répertoire à été installé durant la formation sur mon compte github personnel et a une visibilité public à des fins de collaborations optimales avec les collaborateurs, intervenants et collègues.

## Utilisation <a name="utilisation"></a>
Ce répertoire se dote d'un fichier "README.md" dans le but de proposer une explication de chaque code réalisé durant ce projet CAP ENTREPRISE.<br>
On aura donc dans le sommaire l'ajout permanent des liens vers les différentes parties de ce projet et les mise à jour de ses programmes.<br>
Ce projet est la conclusion de 3 mois d'apprentissage, est sera présenté à l'ensemble des parties mercredi 13 mars.

## Contribuer <a name="contribuer"></a>
Toutes personnes à une visibilité sur l'entièreté du répertoire. En revanche, aucune modification n'est possible.<br>
Les véritables contributions se font lors de nos échanges en direct ou en visio, durant tout l'apprentissage de cet emploi.<br>
De nombreux cours théoriques et pratiques on été réalisés pour consolider notre culture et employabilité.

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

1. `docker-compose build`
2. `docker-compose up`
3. `python manage.py makemigrations`
4. `python manage.py migrate`

### Création `settings.py`

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

![Script_ETL_ODS_Flux](https://github.com/Jerome-Reviron/Pharma_post/blob/main/images_documentation/Script_ETL_ODS_Flux.png)<br>

### Étapes détaillées:

1. **Chargement du fichier CSV dans un DataFrame Pandas:**
Le script utilise la bibliothèque Pandas pour lire le fichier CSV (`flux-total-dep.csv`) dans un DataFrame appelé `df`. Il spécifie le délimiteur, l'encodage et demande de ne pas traiter les valeurs manquantes comme des NaN.<br>

2. **Troncature de la table `Flux`:**
Toutes les entrées existantes dans la table `Flux` sont supprimées (tronquées) à l'aide de la méthode `delete()`.<br>

3. **Création des objets `Flux` à partir du DataFrame:**
Le script utilise une compréhension de liste avec `iterrows()` pour créer une liste d'objets `Flux`. Chaque ligne du DataFrame est convertie en un objet `Flux`.<br>

4. **Insertion en bloc des objets `Flux` dans la base de données:**
La liste d'objets `Flux` est insérée en bloc dans la base de données à l'aide de la méthode `bulk_create()`.<br>

5. **Récupération des données après `bulk_create` dans un DataFrame:**
Les données insérées dans la base de données sont récupérées dans un nouveau DataFrame Pandas appelé `df_Flux_apres_bulk_create` à l'aide de la méthode `from_records()`.<br>

6. **Affichage des résultats:**
Le script affiche des messages indiquant le nombre de lignes chargées depuis le fichier CSV, le nombre d'objets `Flux` créés, et une confirmation de l'insertion des objets `Flux` dans la base de données.<br>

7. **Exécution du script:**
Le script est exécuté si le fichier est lancé en tant que script principal (`__name__ == "__main__"`).<br>

# Modèle Django - Flux <a name="models_Flux"></a> 

![Model_class_Flux](https://github.com/Jerome-Reviron/Pharma_post/blob/main/images_documentation/Model_class_Flux.png)<br>

Le fichier `models.py` contient la définition du modèle Django pour représenter les données d'un flux. Ce modèle, appelé `Flux`, est utilisé pour structurer les informations extraites du fichier `flux-total-dep.csv`. Les attributs du modèle correspondent aux différentes données du flux, telles que le code de la région, le libellé de la région, le code du département, le libellé du département, la date de fin de la semaine, le type de vaccin, le nombre d'unités de consommation directe du vaccin et le nombre total de doses du vaccin.

La méthode `__str__` du modèle est personnalisée pour renvoyer une représentation lisible du flux, comprenant le code de la région, le code du département et le type de vaccin.

### Introduction

Le fichier `models.py` définit le modèle Django appelé `Flux`, structurant les informations extraites du fichier "flux-total". Les attributs du modèle incluent des données essentielles telles que le code et le libellé de la région, le code et le libellé du département, la date de fin de la semaine, le type de vaccin, et les quantités de doses du vaccin.

### Fonctionnalités

La méthode `__str__` est implémentée pour fournir une représentation lisible du flux, incluant des informations clés telles que le code de la région, le code du département et le type de vaccin.

### Utilisations

Le modèle `Flux` est utilisé dans l'application Django pour structurer les données extraites du fichier `flux-total-dep.csv`. Il offre une représentation claire et organisée des flux, facilitant ainsi la manipulation et l'affichage de ces données.


# Vue Django - ETL_ODS_Flux <a name="views_ETL_ODS_Flux"></a> 

![Views_ETL_ODS_Flux](https://github.com/Jerome-Reviron/Pharma_post/blob/main/images_documentation/Views_ETL_ODS_Flux.png)<br>

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

![db_sqlite3_table_app_flux](https://github.com/Jerome-Reviron/Pharma_post/blob/main/images_documentation/db_sqlite3_table_app_flux.png)<br>

# ETL des Données DWH depuis DataFrame df_flux <a name="ETL_DWH_Flux.py"></a>

### Introduction

Ce script Python réalise un processus d'Extraction, Transformation et Chargement (ETL) des données à partir d'un DataFrame Pandas vers une base de données Django. Le modèle de données Django utilisé comprend les tables `Flux`, `D_TYPE_VACCIN`, `D_DATE`, `D_LOCATION`, et `F_FLUX`. Les données en question représentent des flux de vaccins, et le script effectue diverses opérations pour préparer et insérer ces données dans la base de données Django.

![Draw.io_MCD](https://github.com/Jerome-Reviron/Pharma_post/blob/main/images_documentation/Draw.io_MCD.png)<br>

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

![Models_class_tables_dimensions](https://github.com/Jerome-Reviron/Pharma_post/blob/main/images_documentation/Models_class_tables_dimensions.png)<br>

![Model_class_table_fait](https://github.com/Jerome-Reviron/Pharma_post/blob/main/images_documentation/Model_class_table_fait.png)<br>

# Modèle Django - D_TYPE_VACCIN <a name="models_D_TYPE_VACCIN"></a>

Le fichier `models.py` contient la définition du modèle Django pour représenter les données des types de vaccins dans le Data Warehouse (DWH). Ce modèle, appelé `D_TYPE_VACCIN`, est utilisé pour structurer les informations relatives aux différents types de vaccins.

### Introduction

Le modèle `D_TYPE_VACCIN` définit les types de vaccins dans le Data Warehouse. Chaque enregistrement représente un type de vaccin avec son libellé.

### Fonctionnalités

- Attributs :
  - `vaccinlabel` (str): Libellé du type de vaccin.
  
### Utilisations

Le modèle `D_TYPE_VACCIN` est utilisé dans le Data Warehouse pour organiser et représenter les informations sur les types de vaccins.

# Modèle Django - D_DATE <a name="models_D_DATE"></a>

Le fichier `models.py` contient la définition du modèle Django pour représenter les données des dates de fin de semaine dans le Data Warehouse (DWH). Ce modèle, appelé `D_DATE`, est utilisé pour structurer les informations relatives aux différentes dates de fin de semaine.

### Introduction

Le modèle `D_DATE` définit les dates de fin de semaine dans le Data Warehouse. Chaque enregistrement représente une date de fin de semaine.

### Fonctionnalités

- Attributs :
  - `date_fin_semaine` (Date): Date de fin de semaine, utilisée comme clé primaire.
  
### Utilisations

Le modèle `D_DATE` est utilisé dans le Data Warehouse pour organiser et représenter les informations sur les dates de fin de semaine.

# Modèle Django - D_LOCATION <a name="models_D_LOCATION"></a>

Le fichier `models.py` contient la définition du modèle Django pour représenter les données de localisation dans le Data Warehouse (DWH). Ce modèle, appelé `D_LOCATION`, est utilisé pour structurer les informations relatives aux emplacements.

### Introduction

Le modèle `D_LOCATION` définit les informations de localisation dans le Data Warehouse. Chaque enregistrement représente une combinaison de code de région et de code de département.

### Fonctionnalités

- Attributs :
  - `code_region_code_departement` (str): Clé primaire concaténée de `code_region` et `code_departement`.
  - `code_region` (int): Code de la région.
  - `code_departement` (str): Code du département.
  - `libelle_region` (str): Libellé de la région.
  - `libelle_departement` (str): Libellé du département.
  
- Méthode `save` : Surcharge de la méthode save pour concaténer les champs et créer la clé primaire.

### Utilisations

Le modèle `D_LOCATION` est utilisé dans le Data Warehouse pour organiser et représenter les informations de localisation.

# Modèle Django - F_FLUX <a name="models_F_FLUX"></a>

Le fichier `models.py` contient la définition du modèle Django pour représenter les données des flux de vaccins dans le Data Warehouse (DWH). Ce modèle, appelé `F_FLUX`, est utilisé pour structurer les informations relatives aux flux de vaccins.

### Introduction

Le modèle `F_FLUX` définit les flux de vaccins dans le Data Warehouse. Chaque enregistrement représente un flux avec des informations telles que le type de vaccin, la date de fin de semaine, la localisation, le nombre d'unités de consommation, et le nombre total de doses.

### Fonctionnalités

- Attributs :
  - `PK_F_FLUX` (str): Clé primaire concaténée de plusieurs champs.
  - `D_TYPE_VACCIN` (ForeignKey): Clé étrangère vers `D_TYPE_VACCIN`.
  - `D_DATE` (ForeignKey): Clé étrangère vers `D_DATE`.
  - `D_LOCATION` (ForeignKey): Clé étrangère vers `D_LOCATION`.
  - `nb_ucd` (float): Nombre d'unités de consommation.
  - `nb_doses` (float): Nombre de doses.
  
- Méthode `save` : Surcharge de la méthode save pour concaténer les champs et créer la clé primaire.

### Utilisations

Le modèle `F_FLUX` est utilisé dans le Data Warehouse pour organiser et représenter les informations sur les flux de vaccins.

# Vue Django - ETL_DWH_D_TYPE_VACCIN <a name="views_ETL_DWH_D_TYPE_VACCIN"></a>

Le fichier `views.py` contient des fonctions de vue Django, dont la fonction `ETL_DWH_D_TYPE_VACCIN` est responsable de l'Extraction, de la Transformation et du Chargement (ETL) des données des types de vaccins dans le système Django.

![Views_ETL_DWH_D_TYPE_VACCIN](https://github.com/Jerome-Reviron/Pharma_post/blob/main/images_documentation/Views_ETL_DWH_D_TYPE_VACCIN.png)<br>

### Introduction

La fonction `ETL_DWH_D_TYPE_VACCIN` récupère tous les libellés de types de vaccins de la base de données Django, applique une pagination pour afficher un nombre limité de types de vaccins par page, puis rend la page `ETL_DWH_D_TYPE_VACCIN.html` avec le contexte contenant les types de vaccins paginés.

### Fonctionnalités

- **Extraction des Types de Vaccins de la Base de Données :** Utilisation de la requête `D_TYPE_VACCIN.objects.all()` pour extraire tous les libellés de types de vaccins de la base de données.

- **Pagination des Types de Vaccins :** Application de la pagination pour afficher un nombre limité de types de vaccins par page, facilitant la navigation pour l'utilisateur.

- **Gestion des Pages :** Gestion des situations liées à la pagination, garantissant une expérience utilisateur sans accroc.

- **Rendu du Contexte :** Préparation d'un contexte contenant les types de vaccins paginés pour être rendu sur la page `ETL_DWH_D_TYPE_VACCIN.html`.

### Utilisations

La fonction `ETL_DWH_D_TYPE_VACCIN` est essentielle pour permettre à l'utilisateur de visualiser les types de vaccins paginés extraits de la base de données, facilitant ainsi le suivi et l'analyse des données sur les vaccins.

### Particularités

Aucune particularité spécifique n'est mentionnée pour la fonction `ETL_DWH_D_TYPE_VACCIN` dans ce contexte.

# Vue Django - ETL_DWH_D_DATE <a name="views_ETL_DWH_D_DATE"></a>

Le fichier `views.py` contient des fonctions de vue Django, dont la fonction `ETL_DWH_D_DATE` est responsable de l'Extraction, de la Transformation et du Chargement (ETL) des données des dates dans le système Django.

![Views_ETL_DWH_D_DATE](https://github.com/Jerome-Reviron/Pharma_post/blob/main/images_documentation/Views_ETL_DWH_D_DATE.png)<br>

### Introduction

La fonction `ETL_DWH_D_DATE` récupère toutes les dates de la base de données Django, applique une pagination pour afficher un nombre limité de dates par page, puis rend la page `ETL_DWH_D_DATE.html` avec le contexte contenant les dates paginées.

### Fonctionnalités

- **Extraction des Dates de la Base de Données :** Utilisation de la requête `D_DATE.objects.all()` pour extraire toutes les dates de la base de données.

- **Pagination des Dates :** Application de la pagination pour afficher un nombre limité de dates par page, facilitant la navigation pour l'utilisateur.

- **Gestion des Pages :** Gestion des situations liées à la pagination, garantissant une expérience utilisateur sans accroc.

- **Rendu du Contexte :** Préparation d'un contexte contenant les dates paginées pour être rendu sur la page `ETL_DWH_D_DATE.html`.

### Utilisations

La fonction `ETL_DWH_D_DATE` est essentielle pour permettre à l'utilisateur de visualiser les dates paginées extraites de la base de données, facilitant ainsi le suivi et l'analyse des données temporelles.

### Particularités

Aucune particularité spécifique n'est mentionnée pour la fonction `ETL_DWH_D_DATE` dans ce contexte.

# Vue Django - ETL_DWH_D_LOCATION <a name="views_ETL_DWH_D_LOCATION"></a>

Le fichier `views.py` contient des fonctions de vue Django, dont la fonction `ETL_DWH_D_LOCATION` est responsable de l'Extraction, de la Transformation et du Chargement (ETL) des données de localisation dans le système Django.

![Views_ETL_DWH_D_LOCATION](https://github.com/Jerome-Reviron/Pharma_post/blob/main/images_documentation/Views_ETL_DWH_D_LOCATION.png)<br>

### Introduction

La fonction `ETL_DWH_D_LOCATION` récupère toutes les localisations de la base de données Django, applique une pagination pour afficher un nombre limité de localisations par page, puis rend la page `ETL_DWH_D_LOCATION.html` avec le contexte contenant les localisations paginées.

### Fonctionnalités

- **Extraction des Localisations de la Base de Données :** Utilisation de la requête `D_LOCATION.objects.all()` pour extraire toutes les localisations de la base de données.

- **Pagination des Localisations :** Application de la pagination pour afficher un nombre limité de localisations par page, facilitant la navigation pour l'utilisateur.

- **Gestion des Pages :** Gestion des situations liées à la pagination, garantissant une expérience utilisateur sans accroc.

- **Rendu du Contexte :** Préparation d'un contexte contenant les localisations paginées pour être rendu sur la page `ETL_DWH_D_LOCATION.html`.

### Utilisations

La fonction `ETL_DWH_D_LOCATION` est essentielle pour permettre à l'utilisateur de visualiser les localisations paginées extraites de la base de données, facilitant ainsi le suivi et l'analyse des données de localisation.

### Particularités

Aucune particularité spécifique n'est mentionnée pour la fonction `ETL_DWH_D_LOCATION` dans ce contexte.

# Vue Django - ETL_DWH_F_FLUX <a name="views_ETL_DWH_F_FLUX"></a>

Le fichier `views.py` contient des fonctions de vue Django, dont la fonction `ETL_DWH_F_FLUX` est responsable de l'Extraction, de la Transformation et du Chargement (ETL) des données des flux de vaccins dans le système Django.

![Views_ETL_DWH_F_FLUX](https://github.com/Jerome-Reviron/Pharma_post/blob/main/images_documentation/Views_ETL_DWH_F_FLUX.png)<br>

### Introduction

La fonction `ETL_DWH_F_FLUX` récupère tous les flux de vaccins de la base de données Django, applique une pagination pour afficher un nombre limité de flux par page, puis rend la page `ETL_DWH_F_FLUX.html` avec le contexte contenant les flux paginés.

### Fonctionnalités

- **Extraction des Flux de la Base de Données :** Utilisation de la requête `F_FLUX.objects.all()` pour extraire tous les flux de vaccins de la base de données.

- **Pagination des Flux :** Application de la pagination pour afficher un nombre limité de flux par page, facilitant la navigation pour l'utilisateur.

- **Gestion des Pages :** Gestion des situations liées à la pagination, garantissant une expérience utilisateur sans accroc.

- **Rendu du Contexte :** Préparation d'un contexte contenant les flux paginés pour être rendu sur la page `ETL_DWH_F_FLUX.html`.

### Utilisations

La fonction `ETL_DWH_F_FLUX` est essentielle pour permettre à l'utilisateur de visualiser les flux paginés extraits de la base de données, facilitant ainsi le suivi et l'analyse des données sur les flux de vaccins.

### Particularités

Aucune particularité spécifique n'est mentionnée pour la fonction `ETL_DWH_F_FLUX` dans ce contexte.

# Interface Web - index.html <a name="UI_index"></a>

### Description du fichier `index.html`

Le fichier `index.html` est la page d'accueil de l'application Pharma Post. Il sert de point d'entrée pour les utilisateurs et présente des informations essentielles sur le projet, ainsi que des fonctionnalités de navigation.

### Caractéristiques Principales

- **Langue :** Le document est rédigé en français (`lang="fr"`).

- **En-tête :** L'en-tête contient des métadonnées importantes telles que la définition du jeu de caractères, la vue portée et le lien vers la feuille de style Bootstrap.

- **Titre :** La page est titrée "Pharma Post".

- **Barre de Navigation :** Une barre de navigation fixée en haut de la page permet aux utilisateurs de naviguer entre différentes sections du site. Elle inclut le logo de Pharma Post, le nom du projet, et un bouton pour afficher un panneau de navigation latéral.

- **Panneau de Navigation Latéral :** Un panneau latéral apparaît lorsqu'on clique sur le bouton de la barre de navigation. Il contient des liens vers des pages administratives, des tables, et des API en fonction du statut de connexion de l'utilisateur.

- **Sections :** La page est structurée en sections décrivant le projet, ses objectifs, et les étapes de développement. Ces sections incluent une description de Pharma Post, l'origine des données, les objectifs du projet, et les missions du développeur.

- **Liens :** Des liens vers des pages administratives, des tables, et des API sont inclus dans le panneau de navigation, permettant aux utilisateurs de naviguer rapidement vers des sections spécifiques du site.

- **Script Bootstrap :** Un script Bootstrap est inclus à la fin du fichier pour assurer un comportement réactif de l'interface utilisateur.

### Utilisations

Cette page d'accueil fournit aux utilisateurs des informations contextuelles sur le projet Pharma Post, son objectif, et les liens nécessaires pour accéder à des fonctionnalités spécifiques de l'application.

### Remarque

Le fichier `index.html` sert de point central pour l'expérience utilisateur sur Pharma Post, fournissant des informations essentielles et des liens de navigation pour accéder à d'autres parties de l'application.

# Interface Web - ETL_Tables <a name="UI_ETL_Table"></a>

## Description du fichier `ETL_DWH_F_FLUX.html`

Le fichier `ETL_DWH_F_FLUX.html` constitue l'interface utilisateur dédiée à la table de faits `F_FLUX` dans le système Pharma Post. Il offre une vue structurée et conviviale des données associées à cette table.

### Caractéristiques Principales

- **Langue :** Le document est rédigé en français (`lang="fr"`).

- **En-tête :** L'en-tête contient des métadonnées importantes telles que la définition du jeu de caractères, la vue portée et les liens vers les feuilles de style Bootstrap et personnalisée.

- **Titre :** La page est titrée "ETL_DWH_F_FLUX".

- **Barre de Navigation :** Une barre de navigation fixée en haut de la page permet aux utilisateurs de naviguer entre différentes sections du site. Elle inclut le logo de Pharma Post, le nom du projet, et un bouton pour afficher un panneau de navigation latéral.

- **Panneau de Navigation Latéral :** Un panneau latéral apparaît lorsqu'on clique sur le bouton de la barre de navigation. Il contient des liens vers des pages administratives, des tables, et des API en fonction du statut de connexion de l'utilisateur.

- **Contenu Principal :** La section principale présente des informations spécifiques à la table `F_FLUX`. Elle affiche le titre de la table, le nombre total de lignes dans la table, et une représentation tabulaire des données. Chaque colonne de la table est identifiée par un en-tête.

- **Pagination :** La pagination est intégrée pour gérer un grand nombre de lignes. Elle permet aux utilisateurs de naviguer entre les différentes pages de résultats.

### Utilisations

Cette interface facilite l'accès et la visualisation des données de la table de faits `F_FLUX` pour les utilisateurs de Pharma Post. Elle offre une expérience conviviale pour explorer les informations associées aux flux de données.

### Remarque

Le fichier `ETL_DWH_F_FLUX.html` suit la même structure que l'interface du fichier `ETL_ODS_Flux.html` du projet Pharma Post, assurant une cohérence dans la conception et la navigation. Pour maintenir cette uniformité, les fichiers `ETL_DWH_D_DATE.html`, `ETL_DWH_D_LOCATION.html`, et `ETL_DWH_D_TYPE_VACCIN.html` sont stylisés de manière similaire, en adaptant les noms de table et les colonnes en conséquence. Cela garantit une expérience utilisateur harmonieuse à travers les différentes tables de dimension.

# Interface Web - CSS <a name="CSS"></a>

## Installation de Bootstrap dans un Projet Django

### Étape 1: Installation de Bootstrap

Tout d'abord, ajoutez le lien vers la feuille de style Bootstrap dans votre fichier HTML. Vous pouvez le faire en ajoutant la ligne suivante dans la section `<head>` de votre fichier HTML.<br>

link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css".<br>

Cette ligne permet à votre projet Django d'accéder aux styles prédéfinis de Bootstrap.

### Étape 2: Configuration du Dossier Static

1. Créez un dossier `static` dans votre projet Django. Assurez-vous qu'il est situé à la racine du projet.

2. Créez un fichier `styles.css` dans le dossier `static`. Ce fichier contiendra vos règles CSS personnalisées comme les import de font_google.<br>

@import url('https://fonts.googleapis.com/css2?family=Crimson+Text:ital,wght@0,400;0,600;0,700;1,400;1,600;1,700&display=swap');<br>
@import url('https://fonts.googleapis.com/css2?family=Merriweather:ital,wght@0,300;0,400;0,700;0,900;1,300;1,400;1,700;1,900&display=swap');<br>
@import url('https://fonts.googleapis.com/css2?family=Kode+Mono:wght@400..700&display=swap');<br>

### Étape 3: Configuration des Paramètres Django

1. Ouvrez votre fichier `settings.py`** dans le dossier principal de votre projet Django.

2. Ajoutez la configuration pour `STATICFILES_DIRS`.** Cela permet à Django de savoir où trouver les fichiers statiques.
Cette étape est cruciale pour que Django puisse localiser les fichiers statiques, y compris les styles CSS personnalisés, dans le projet.

# API Django - `views.py` <a name="API_Views.py"></a>

Le fichier `views.py` de votre application Django met en œuvre une architecture générique pour les API en utilisant une classe de base, `BaseAPI`, et des classes dérivées spécifiques à chaque table de la base de données.

## BaseAPI

La classe `BaseAPI` agit comme une classe de base commune pour toutes les API de votre projet. Elle fournit des méthodes génériques pour les opérations CRUD, facilitant la gestion cohérente des différentes tables de la base de données.

### Fonctionnalités principales

- **Gestion des Modèles et Sérialiseurs :** Utilise des dictionnaires (`model_dict` et `serializer_dict`) pour associer dynamiquement les modèles et sérialiseurs correspondant à chaque table.

- **Configuration du Modèle par Défaut :** Définit `default_t` comme le modèle par défaut pour les requêtes, offrant une flexibilité dans le choix du modèle.

- **Sélection Dynamique du Modèle :** Permet aux classes dérivées de spécifier le modèle à utiliser en fonction de la requête.

- **Réponse Générique :** Renvoie des réponses JSON génériques avec des informations sur le modèle, le nombre total de lignes et les données sérialisées.

#### Méthode `get`

La méthode `get` récupère les données de la table associée au modèle spécifié. Elle permet d'effectuer des recherches, de sérialiser les données, et renvoie une réponse avec des informations détaillées.

## Classes Dérivées

Les classes dérivées, telles que `API_Operational_Data_Store_Flux`, spécialisent la classe de base pour chaque table spécifique de la base de données.

### Personnalisation des Opérations CRUD

Chaque classe dérivée peut personnaliser les méthodes CRUD selon les besoins spécifiques de la table associée. Par exemple, la classe `API_Operational_Data_Store_Flux` a des méthodes `get`, `post`, `put`, `patch`, et `delete` personnalisées pour la table Flux.

#### Méthode `get`

- Récupère les données de la table Flux, offrant une flexibilité pour renvoyer tous les enregistrements ou un enregistrement spécifique.

#### Méthode `post`

- Permet d'ajouter un nouvel enregistrement à la table Flux en utilisant les données fournies dans la requête POST.

#### Méthodes `put`, `patch`

- Facilitent la mise à jour des détails d'un enregistrement existant dans la table Flux, avec la distinction entre une mise à jour complète (`put`) et une mise à jour partielle (`patch`).

#### Méthode `delete`

- Permet de supprimer un enregistrement spécifié par son identifiant, ou tous les enregistrements si aucun identifiant n'est fourni.

# API Django -  `serializers.py` <a name="API_serializers.py"></a>

Le fichier `serializers.py` est essentiel pour l'API Django, car il définit comment les objets Python (issus des modèles) doivent être convertis en JSON, et vice versa. Il assure la sérialisation et la désérialisation des données, permettant ainsi aux vues de traiter facilement les requêtes HTTP.

## Serializer Django REST Framework

Dans votre cas, vous utilisez le module `serializers` de Django REST Framework pour créer des sérialiseurs spécifiques à chaque modèle de votre application.

### Fonctionnement Général

1. **Import des Modules Nécessaires :**
   - `serializers` : Module principal de Django REST Framework pour la création de sérialiseurs.
   - `authenticate` : Permet d'authentifier un utilisateur.
   - `Token` : Modèle de token d'authentification utilisé pour générer des tokens pour les utilisateurs.

2. **Import des Modèles :**
   - Vous importez les modèles Django associés à votre application, tels que `Flux`, `D_TYPE_VACCIN`, `D_DATE`, `D_LOCATION`, et `F_FLUX`.

3. **Création des Sérialiseurs :**
   - Vous définissez des classes de sérialiseur spécifiques à chaque modèle en utilisant `serializers.ModelSerializer`.
   - La classe `Meta` à l'intérieur de chaque sérialiseur indique le modèle associé et spécifie les champs à inclure dans la sérialisation (dans votre cas, tous les champs avec `fields = '__all__'`).

### Utilisation dans les Vues

1. **Import des Sérialiseurs dans `views.py` :**
   - Les sérialiseurs définis dans `serializers.py` sont importés dans le fichier `views.py`. Par exemple, `Flux_Serializer` est utilisé dans `API_Operational_Data_Store_Flux` pour sérialiser les données de la table `Flux`.

2. **Utilisation dans les Méthodes des Vues :**
   - Les sérialiseurs sont utilisés dans les méthodes des vues pour convertir les objets Python (récupérés de la base de données) en JSON lors des opérations de lecture (GET) et pour convertir les données JSON des requêtes HTTP en objets Python lors des opérations d'écriture (POST, PUT, PATCH).

3. **Réutilisation dans d'Autres Vues :**
   - Les sérialiseurs peuvent être réutilisés dans d'autres vues pour les modèles correspondants. Par exemple, `D_TYPE_VACCIN_Serializer` est utilisé pour sérialiser les données de la table `D_TYPE_VACCIN`.

### Avantages

- **Simplicité de Conversion :** Les sérialiseurs simplifient la conversion entre les objets Django (modèles) et le format JSON, facilitant ainsi la communication entre le backend et le frontend.
- **Réutilisation du Code :** En définissant des sérialiseurs pour chaque modèle, vous favorisez la réutilisation du code, améliorant la maintenabilité et la cohérence de l'application.

L'utilisation de sérialiseurs dans Django REST Framework est une pratique courante pour construire des APIs robustes et flexibles.

# API Django Authentification - `views_auth.py` <a name="API_views_auth.py"></a>

Le fichier `views_auth.py` de votre projet Django gère l'authentification des utilisateurs. Voici une brève description de son contenu :

## Class `LoginView`

La classe `LoginView` hérite de `TemplateView` de Django, permettant d'afficher un modèle HTML. Cette classe gère le processus d'authentification.

### Méthode `get`

La méthode `get` est utilisée pour gérer les requêtes GET, renvoyant le contenu HTML de la page de connexion.

### Méthode `post`

La méthode `post` gère les requêtes POST, principalement utilisées pour la soumission du formulaire de connexion. Elle effectue les actions suivantes :

1. Utilise le sérialiseur `LoginSerializer` pour valider les données du formulaire.
2. Si les données sont valides, elle authentifie l'utilisateur avec les informations fournies.
3. Si l'authentification réussit, elle crée un token d'authentification pour l'utilisateur.
4. Renvoie une réponse JSON contenant le token en cas de succès, ou les erreurs en cas d'échec.

### Utilisation des Classes et Modules

- `TemplateView`: Classe de Django pour afficher des modèles HTML.
- `render`: Fonction de Django pour générer une réponse HTTP avec le contenu HTML.
- `authenticate`: Fonction de Django pour authentifier un utilisateur.
- `LoginSerializer`: Sérialiseur utilisé pour valider et traiter les informations de connexion.
- `JsonResponse`: Réponse JSON pour les requêtes.

Cette classe facilite le processus d'authentification dans votre application Django, en utilisant Django REST Framework pour la gestion des tokens et des sérialiseurs.

# API Django Authentification - `LoginSerializers` <a name="API_LoginSerializers"></a>

Le fichier `serializers.py` de votre projet Django contient un sérialiseur spécifique, `LoginSerializer`, utilisé pour valider les informations de connexion d'un utilisateur.

## Class `LoginSerializer` 

La classe `LoginSerializer` hérite du sérialiseur de Django REST Framework et est conçue pour traiter les informations de connexion, telles que le nom d'utilisateur (`username`) et le mot de passe (`password`).

### Champs du Sérialiseur

- `username`: Champ pour le nom d'utilisateur.
- `password`: Champ pour le mot de passe (en écriture seulement, indiqué par `write_only=True`).

### Méthode `validate`

La méthode `validate` est définie pour effectuer la validation personnalisée des données du sérialiseur. Elle réalise les opérations suivantes :

1. Récupère le nom d'utilisateur et le mot de passe à partir des données.
2. Vérifie si le nom d'utilisateur et le mot de passe sont fournis.
3. Utilise la fonction `authenticate` de Django pour vérifier l'authenticité des informations de connexion.
4. En cas de succès, renvoie les données de l'utilisateur authentifié.

Si des erreurs sont détectées pendant la validation, des exceptions de type `serializers.ValidationError` sont levées.

Ce sérialiseur est utilisé dans le processus d'authentification de la classe `LoginView` de votre fichier `views_auth.py`, contribuant ainsi à la sécurisation de l'accès à votre application.

# API Django Authentification - `login.html` <a name="API_login.html"></a>

Le fichier `login.html` de votre projet Django représente la page de connexion à l'interface d'administration. Voici une description détaillée de son contenu :

### Structure HTML
- La balise `<head>` contient des méta-informations, des liens vers des feuilles de style externes (Font Awesome et votre fichier `styles.css`), et le titre de la page.
- La balise `<body>` contient la structure du formulaire de connexion.

### Contenu du Formulaire
- Un ensemble d'icônes stylisées avec des couleurs spécifiées (`--clr`) pour un design visuel.
- Un formulaire avec la classe `Log` et l'ID `login-form` qui sera soumis à la validation lorsqu'un utilisateur tente de se connecter.
- Les champs du formulaire comprennent un champ pour le nom d'utilisateur (`username`) et un champ pour le mot de passe (`password`).
- Un bouton "Valider" (`Btn_login`) qui soumet le formulaire.

### Utilisation de JavaScript
- Un script JavaScript à la fin du fichier permet de gérer la soumission du formulaire.
- Lorsqu'un utilisateur soumet le formulaire, le script récupère les valeurs des champs, le jeton CSRF, et effectue une requête POST à l'URL `http://localhost:8000/api/login/`.
- En cas de succès, l'utilisateur est redirigé vers `http://localhost:8000/`.
- En cas d'échec, des messages d'erreur sont affichés dans la console du navigateur.

### Bouton de Retour
- Un lien avec la classe `Btn_back1` permet de revenir à la page d'accueil en cliquant sur le bouton.

Ce fichier facilite l'interaction de l'utilisateur avec le processus d'authentification et ajoute des éléments visuels attrayants à la page de connexion. Vous avez également implémenté une gestion des erreurs côté client pour une meilleure expérience utilisateur.

# API Django Authentification - `views_register.py` <a name="API_views_register.py"></a>

Le fichier "views_register.py" contient la classe "RegisterView", une vue Django chargée de gérer l'inscription d'un nouvel utilisateur en tant qu'administrateur.

## Class `RegisterView`

### Propriétés
- `template_name` : Nom du modèle HTML utilisé pour l'affichage du formulaire d'inscription.
- `form_class` : Classe du formulaire utilisé pour la création d'un nouvel utilisateur. Dans ce cas, il s'agit de "CustomUserCreationForm".

### Méthode GET
La méthode GET est invoquée lorsqu'un utilisateur accède à la page d'inscription. Elle effectue les actions suivantes :
- Vérifie si l'utilisateur est déjà authentifié et s'il est un administrateur.
- Si c'est le cas, affiche le formulaire d'inscription pour un nouvel administrateur.
- Si l'utilisateur n'est pas authentifié ou n'est pas un administrateur, redirige vers la page de connexion.

### Méthode POST
La méthode POST est invoquée lorsque le formulaire d'inscription est soumis. Elle effectue les actions suivantes :
- Vérifie à nouveau l'authentification et les privilèges administratifs de l'utilisateur.
- Valide le formulaire d'inscription avec les données fournies.
- Si le formulaire est valide, crée un nouvel utilisateur avec les droits d'administrateur et génère un token d'authentification.
- Retourne une réponse JSON avec un message de succès et le token en cas de réussite.
- En cas d'erreur, renvoie une réponse JSON avec les erreurs de formulaire.

Cette classe assure la création d'un nouvel administrateur à partir du formulaire d'inscription, avec des vérifications de sécurité pour s'assurer que l'accès est limité aux administrateurs déjà authentifiés.


# API Django Authentification - `register.html` <a name="API_register.html"></a>

Ce fichier représente le formulaire d'inscription (register) d'une application Django. Il permet aux utilisateurs de créer un compte en fournissant un nom d'utilisateur, une adresse e-mail, et un mot de passe.

### HTML Form

Le fichier contient une balise `<form>` HTML avec les champs suivants :
- `Nom d'utilisateur` : Pour saisir le nom d'utilisateur.
- `Email` : Pour saisir l'adresse e-mail.
- `Mot de passe` : Pour saisir le mot de passe.
- `Confirmez le mot de passe` : Pour confirmer le mot de passe.

### Styles et Icônes

Le formulaire est stylisé à l'aide de classes CSS et d'icônes Font Awesome pour une présentation visuelle attrayante.

### Soumission du Formulaire

Lorsque l'utilisateur remplit le formulaire et le soumet, une requête POST est effectuée vers l'URL 'http://localhost:8000/api/register/'. Les données du formulaire, telles que le nom d'utilisateur, l'e-mail et les mots de passe, sont envoyées au serveur.

### JavaScript

Le fichier inclut également du code JavaScript pour gérer la soumission du formulaire via une requête Fetch. Il récupère les valeurs des champs du formulaire, crée un objet FormData, et envoie les données au serveur. En cas de succès, l'utilisateur est redirigé vers 'http://localhost:8000/'. En cas d'erreur, des messages d'erreur sont affichés dans la console.

### Bouton de Retour

Un bouton de retour est inclus, permettant à l'utilisateur de revenir à la page d'accueil du site.

# API Django Authentification - `LoginSerializers` <a name="API_LoginSerializers"></a>

# Class `LogoutView`

La classe "LogoutView" représente une vue Django chargée de gérer la déconnexion d'un utilisateur. Elle hérite de la classe générique "TemplateView" de Django.

## Méthode GET

La classe définit une méthode GET qui est invoquée lorsqu'un utilisateur accède à la page de déconnexion. À ce stade, la méthode effectue les actions suivantes :
- Appelle la fonction `logout(request)` pour déconnecter l'utilisateur actuellement authentifié.
- Redirige l'utilisateur vers la page d'accueil du site en utilisant `return redirect('/')`.

## Fonctionnalité de Déconnexion

L'objectif principal de cette classe est de fournir une fonctionnalité simple et propre de déconnexion pour les utilisateurs connectés. La déconnexion est réalisée en appelant la fonction `logout(request)`, qui met fin à la session de l'utilisateur.

## Redirection vers la Page d'Accueil

Après la déconnexion réussie, l'utilisateur est redirigé vers la page d'accueil du site pour une meilleure expérience utilisateur.

Note : Assurez-vous que l'URL '/' dans `return redirect('/')` correspond à l'URL de la page d'accueil de votre application Django.

Cette classe peut être utilisée en conjonction avec un lien ou un bouton de déconnexion dans votre interface utilisateur pour permettre aux utilisateurs de se déconnecter de manière sécurisée.

# API Django Authentification - `views_out.py` <a name="API_views_out.py"></a>

# Class `LogoutView`

La classe "LogoutView" représente une vue Django chargée de gérer la déconnexion d'un utilisateur. Elle hérite de la classe générique "TemplateView" de Django.

## Méthode GET

La classe définit une méthode GET qui est invoquée lorsqu'un utilisateur accède à la page de déconnexion. À ce stade, la méthode effectue les actions suivantes :
- Appelle la fonction `logout(request)` pour déconnecter l'utilisateur actuellement authentifié.
- Redirige l'utilisateur vers la page d'accueil du site en utilisant `return redirect('/')`.

## Fonctionnalité de Déconnexion

L'objectif principal de cette classe est de fournir une fonctionnalité simple et propre de déconnexion pour les utilisateurs connectés. La déconnexion est réalisée en appelant la fonction `logout(request)`, qui met fin à la session de l'utilisateur.

## Redirection vers la Page d'Accueil

Après la déconnexion réussie, l'utilisateur est redirigé vers la page d'accueil du site pour une meilleure expérience utilisateur.

Note : Assurez-vous que l'URL '/' dans `return redirect('/')` correspond à l'URL de la page d'accueil de votre application Django.

Cette classe peut être utilisée en conjonction avec un lien ou un bouton de déconnexion dans votre interface utilisateur pour permettre aux utilisateurs de se déconnecter de manière sécurisée.

# API Django Authentification - `tests.py` <a name="API_tests.py"></a>

Le fichier "tests.py" contient une suite de tests unitaires pour les vues associées aux modèles de l'application Django. Ces tests sont écrits à l'aide du module Django TestCase et visent à assurer le bon fonctionnement des fonctionnalités CRUD (Create, Read, Update, Delete) pour le modèle "Flux" ainsi que d'autres modèles associés.

## Structure des Tests

L'ensemble des tests de ce fichier s'adapte à chacune des classes correspondantes aux diférentes classes du fichiers `views.py` avec chacune 6 méthodes. Pour l'explication voici les tests sur la class `TestFlux` pour la class `Flux` du fichiers `views.py`.

### Méthode `setUp`
- Initialise les données nécessaires pour les tests, y compris une instance de l'APIRequestFactory, des vues associées aux modèles, et des instances de modèles pour effectuer les tests.

### Tests CRUD
1. **Test de récupération de la liste des flux**
   - Vérifie si la requête GET renvoie une réponse HTTP 200.
   - Vérifie si le nombre d'éléments retournés correspond au nombre d'objets Flux dans la base de données.

2. **Test de récupération détaillée d'un flux**
   - Vérifie si la requête GET renvoie une réponse HTTP 200.
   - Vérifie si les détails du flux récupéré correspondent à ceux de l'objet Flux créé lors de la configuration.

3. **Test de création d'un nouveau flux**
   - Vérifie si la requête POST renvoie une réponse HTTP 201 après la création d'un nouveau flux.
   - Vérifie si le nombre total d'objets Flux dans la base de données a augmenté.

4. **Test de mise à jour d'un flux**
   - Vérifie si la requête PUT renvoie une réponse HTTP 200 après la mise à jour d'un flux existant.
   - Vérifie si les modifications apportées à l'objet Flux sont correctement enregistrées dans la base de données.

5. **Test de mise à jour partielle d'un flux**
   - Vérifie si la requête PATCH renvoie une réponse HTTP 200 après la mise à jour partielle d'un flux existant.
   - Vérifie si les modifications partielles sont correctement enregistrées dans la base de données.

6. **Test de suppression d'un flux**
   - Vérifie si la requête DELETE renvoie une réponse HTTP 204 après la suppression d'un flux existant.
   - Vérifie si l'objet Flux est effectivement supprimé de la base de données.

### Remarque
- Les tests utilisent l'authentification forcée avec un utilisateur et un token, assurant ainsi que seuls les utilisateurs authentifiés peuvent accéder aux fonctionnalités CRUD.

