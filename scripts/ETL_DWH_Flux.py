import pandas as pd
import os
from app.models import Flux, D_TYPE_VACCIN, D_DATE, D_LOCATION, F_FLUX
from datetime import date
from django.db import IntegrityError
from django.db import transaction

def run():

    # Charger les DataFrames pour flux
    flux_data = Flux.objects.values()
    df_flux = pd.DataFrame.from_records(flux_data)

    # Filtrer les lignes en utilisant query
    df_flux = df_flux.query('nb_ucd != "NA" and nb_doses != "NA"')
    print(f"Longueur du DataFrame après application des filtres : {len(df_flux)}")

    # Nettoyer les valeurs de la colonne 'vaccinlabel'
    print(df_flux.columns)
    df_flux['type_de_vaccin'] = df_flux['type_de_vaccin'].str.strip().str.replace(' ', '_')

    # Bulk create D_TYPE_VACCIN records, handling possible duplicates
    with transaction.atomic():
        try:
            # Créer une liste unique de types de vaccin
            unique_types_vaccin = sorted(set(df_flux['type_de_vaccin'].unique()))
            
            # Supprimer toutes les données de la table D_TYPE_VACCIN avant l'insertion
            D_TYPE_VACCIN.objects.all().delete()
            print("Table app_d_type_vaccin tronquée.")

            # Utiliser bulk_create pour insérer les objets D_TYPE_VACCIN en une seule requête
            D_TYPE_VACCIN.objects.bulk_create([
                D_TYPE_VACCIN(
                    vaccinlabel=vaccinlabel
                )
                for vaccinlabel in unique_types_vaccin
            ])

            # Stocker le DataFrame dans une variable
            df_d_type_vaccin = pd.DataFrame.from_records(D_TYPE_VACCIN.objects.values())
            # print("Colonnes de df_d_type_vaccin:", df_d_type_vaccin.columns)

            # Afficher un message de succès
            print("Script D_TYPE_VACCIN terminé avec succès!")

        except IntegrityError as e:
            print(f"Erreur lors de l'insertion des données : {e}")

    # Bulk create D_DATE records, handling possible duplicates
    with transaction.atomic():
        try:
            # Créer une liste unique de dates
            unique_dates = sorted(set(df_flux['date_fin_semaine']))

            # Supprimer toutes les données de la table D_DATE avant l'insertion
            D_DATE.objects.all().delete()
            print("Table app_d_date tronquée.")

            # Utiliser bulk_create pour insérer les objets D_DATE en une seule requête
            D_DATE.objects.bulk_create([
                D_DATE(
                    date_fin_semaine=date_fin_semaine
                )
                for date_fin_semaine in unique_dates
            ])

            # Stocker le DataFrame dans une variable
            df_d_date = pd.DataFrame.from_records(D_DATE.objects.values())
            # print("Colonnes de df_d_date:", df_d_date.columns)

            # Afficher un message de succès
            print("Script D_DATE terminé avec succès!")

        except IntegrityError as e:
            print(f"Erreur lors de l'insertion des données : {e}")

    # Bulk create D_LOCATION records, handling possible duplicates
    with transaction.atomic():
        # Filtrer les lignes où code_departement ne commence pas par un zéro
        df_flux = df_flux[~df_flux['code_departement'].str.startswith('0')]

        # Tri du DataFrame selon les colonnes spécifiées
        df_d_location_sorted = df_flux.sort_values(by=['code_region', 'code_departement'])
        # print("Colonnes de df_d_location_sorted:", df_d_location_sorted.columns)

        # Ajout de la colonne 'code_region_code_departement'
        df_flux = df_flux.copy()
        df_flux['code_region_code_departement'] = df_flux['code_region'] + '_' + df_flux['code_departement']

        try:
            # Supprimer toutes les données de la table D_LOCATION avant l'insertion
            D_LOCATION.objects.all().delete()
            print("Table app_d_location tronquée.")

            for _, row in df_d_location_sorted.iterrows():
                key = f"{row['code_region']}-{row['code_departement']}"
                D_LOCATION.objects.update_or_create(
                    code_region_code_departement=key,
                    defaults={
                        'code_region': row['code_region'],
                        'code_departement': row['code_departement'],
                        'libelle_region': row['libelle_region'],
                        'libelle_departement': row['libelle_departement']
                    }
                )

            # Stocker le DataFrame dans une variable
            df_d_location = pd.DataFrame.from_records(D_LOCATION.objects.values())
            # print("Colonnes de df_d_location:", df_d_location.columns)

            print("Script D_LOCATION terminé avec succès!")
        except IntegrityError as e:
            print(f"Erreur lors de l'insertion des données : {e}")

    # Tri du DataFrame selon la clé primaire concaténée
    df_flux_sorted = df_flux.sort_values(by=['type_de_vaccin', 'date_fin_semaine', 'code_region_code_departement'])

    # Liste pour stocker les objets F_FLUX
    F_FLUX_objects = []
    total_rows = len(F_FLUX_objects)

    # Supprimer toutes les entrées existantes dans la table F_FLUX
    F_FLUX.objects.all().delete()

    # Utiliser une transaction atomique pour garantir l'intégrité de la base de données
    with transaction.atomic():
        total_rows_inserted = 0
        try:
            # Itérer sur les lignes de df_flux_sorted
            for _, row in df_flux_sorted.iterrows():

                # Créer des instances de D_LOCATION, D_DATE, D_TYPE_VACCIN
                d_type_vaccin_instance = D_TYPE_VACCIN(
                    vaccinlabel=row['type_de_vaccin']
                )
                d_date_instance = D_DATE(
                    date_fin_semaine=row['date_fin_semaine']
                )
                d_location_instance = D_LOCATION(
                    code_region_code_departement=row['code_region_code_departement'],
                    code_region=row['code_region'],
                    code_departement=row['code_departement'],
                    libelle_region=row['libelle_region'],
                    libelle_departement=row['libelle_departement']
                )

                # Enregistrez les instances de D_CLUB, D_AGEGRP, D_DATE, D_ETABLISHEMENT, D_SEX
                d_type_vaccin_instance.save()
                d_date_instance.save()
                d_location_instance.save()

                # Créer la clé primaire concaténée
                PK_F_FLUX = f"{row['type_de_vaccin']}_{row['date_fin_semaine']}_{row['code_region_code_departement']}"

                # Créer l'objet F_FLUX avec les relations correctement sauvegardées
                F_FLUX_instance = F_FLUX(
                    PK_F_FLUX,
                    D_LOCATION=d_location_instance,
                    D_DATE=d_date_instance,
                    D_TYPE_VACCIN=d_type_vaccin_instance,
                    nb_ucd=row['nb_ucd'],
                    nb_doses=row['nb_doses']
                )

                F_FLUX_objects.append(F_FLUX_instance)
                print(f"PK_F_FLUX: {PK_F_FLUX}")

                # Mettre à jour le nombre total de lignes insérées
                total_rows_inserted += 1

                # Afficher un message à chaque itération
                if total_rows_inserted % 1000 == 0:
                    print(f"{total_rows_inserted} lignes insérées...")

            # Afficher le nombre total de lignes qui seront insérées
            print(f"Nombre total de lignes à insérer : {total_rows_inserted}")

            # Utilisation de bulk_create avec ignore_conflicts=True
            F_FLUX.objects.bulk_create(F_FLUX_objects, ignore_conflicts=True)

            print(f"Script terminé avec succès! {total_rows_inserted} lignes insérées.")
        except Exception as e:
            print(f"Une erreur s'est produite pendant l'insertion : {str(e)}")

if __name__ == "__main__":
    run()
