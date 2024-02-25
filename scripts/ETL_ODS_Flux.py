import os
import pandas as pd
from app.models import Flux

def run():

    # Charger le fichier CSV dans un DataFrame Pandas
    df = pd.read_csv("data/flux-total-dep.csv", delimiter=",", encoding="ISO-8859-1", keep_default_na=False)
    # print(df.columns)

    print(f"Chargement du fichier CSV terminé. Nombre de lignes connues : {len(df)}")

    # Tronquer la table Club
    Flux.objects.all().delete()
    print("Table Flux tronquée.")

    # Utiliser une compréhension de liste avec to_dict
    Fluxs = [
        Flux(
            id=index + 1,
            code_region=row['code_region'],
            libelle_region=row['libelle_region'],
            code_departement=row['code_departement'],
            libelle_departement=row['libelle_departement'],
            date_fin_semaine=row['date_fin_semaine'],
            type_de_vaccin=row['type_de_vaccin'],
            nb_ucd=row['nb_ucd'],
            nb_doses=row['nb_doses']
        )
        for index, row in df.iterrows()
    ]

    print(f"{len(Fluxs)} objets Flux créés.")

# Utiliser bulk_create pour insérer les objets Flux en une seule requête
    Flux.objects.bulk_create(Fluxs)
    print("Insertion des objets Flux terminée.")

    # Récupérer les données après bulk_create dans un DataFrame
    df_Flux_apres_bulk_create = pd.DataFrame.from_records(Flux.objects.values())

if __name__ == "__main__":
    run()
