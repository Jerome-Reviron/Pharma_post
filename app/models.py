from django.db import models

class Flux(models.Model):
    """
    Modèle représentant les données d'un flux provenant du fichier "flux-total.

    Attributes:
        code_region (str): Code de la région associé au flux.
        libelle_region (str): Libellé de la région associé au flux.
        code_departement (str): Code du département associé au flux.
        libelle_departement (str): Libellé du département associé au flux.
        date_fin_semaine (Date): Date de fin de la semaine du flux.
        type_de_vaccin (str): Type de vaccin associé au flux.
        nb_ucd (int): Nombre d'unités de consommation directe du vaccin.
        nb_doses (int): Nombre total de doses du vaccin.

    Methods:
        __str__(): Retourne une représentation sous forme de chaîne de caractères du flux.
    """

    code_region = models.CharField(max_length=255)
    libelle_region = models.CharField(max_length=255)
    code_departement = models.CharField(max_length=255)
    libelle_departement = models.CharField(max_length=255)
    date_fin_semaine = models.DateField()
    type_de_vaccin = models.CharField(max_length=255)
    nb_ucd = models.CharField(max_length=255)
    nb_doses = models.CharField(max_length=255)

    def __str__(self) -> str:
        """
        Retourne une représentation sous forme de chaîne de caractères du flux.
        """
        return f"{self.code_region} - {self.code_departement} - {self.type_de_vaccin}"
