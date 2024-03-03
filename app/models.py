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

class D_TYPE_VACCIN(models.Model):
    """
    Modèle de données pour les types de vaccins.

    Attributes:
        vaccinlabel (str): Libellé du type de vaccin.
    """
    vaccinlabel = models.CharField(max_length=20, primary_key=True)


class D_DATE(models.Model):
    """
    Modèle de données pour les dates de fin de semaine.

    Attributes:
        date_fin_semaine (Date): Date de fin de semaine, utilisée comme clé primaire.
    """
    date_fin_semaine = models.DateField(primary_key=True)

class D_LOCATION(models.Model):
    """
    Modèle de données pour les informations de localisation.

    Attributes:
        code_region_code_departement (str): Clé primaire concaténée de code_region et code_departement.
        code_region (int): Code de la région.
        code_departement (str): Code du département.
        libelle_region (str): Libellé de la région.
        libelle_departement (str): Libellé du département.
    """
    code_region_code_departement = models.CharField(max_length=10, primary_key=True)
    code_region = models.IntegerField()
    code_departement = models.CharField(max_length=5, blank=True, null=True, default=None)
    libelle_region = models.CharField(max_length=5, blank=True, null=True, default=None)
    libelle_departement = models.CharField(max_length=30, blank=True, null=True, default=None)

    def save(self, *args, **kwargs):
        """
        Surcharge de la méthode save pour concaténer les champs et créer la clé primaire.
        """
        self.code_region_code_departement = f"{self.code_region}-{self.code_departement}"
        super().save(*args, **kwargs)

class F_FLUX(models.Model):
    """
    Modèle de données pour les flux de vaccins.

    Attributes:
        PK_F_FLUX (str): Clé primaire concaténée de plusieurs champs.
        D_TYPE_VACCIN (ForeignKey): Clé étrangère vers D_TYPE_VACCIN.
        D_DATE (ForeignKey): Clé étrangère vers D_DATE.
        D_LOCATION (ForeignKey): Clé étrangère vers D_LOCATION.
        nb_ucd (float): Nombre d'unités de consommation.
        nb_doses (float): Nombre de doses.
    """
    PK_F_FLUX = models.CharField(max_length=100, primary_key=True)
    D_TYPE_VACCIN = models.ForeignKey(D_TYPE_VACCIN, on_delete=models.CASCADE, db_column='D_TYPE_VACCIN')
    D_DATE = models.ForeignKey(D_DATE, on_delete=models.CASCADE, db_column='D_DATE')
    D_LOCATION = models.ForeignKey(D_LOCATION, on_delete=models.CASCADE, db_column='D_LOCATION')
    nb_ucd = models.FloatField(blank=True, null=True, default=None)
    nb_doses = models.FloatField(blank=True, null=True, default=None)

    def save(self, *args, **kwargs):
        """
        Surcharge de la méthode save pour concaténer les champs et créer la clé primaire.
        """
        self.PK_F_FLUX = f"{self.D_TYPE_VACCIN.vaccinlabel}§{self.D_DATE.date_fin_semaine}§{self.D_LOCATION.code_region_code_departement}"
        super().save(*args, **kwargs)