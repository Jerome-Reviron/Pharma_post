from django.test import TestCase
from rest_framework.test import APIRequestFactory
from api.views import API_Operational_Data_Store_Flux
from api.views import API_Datawarehouse_D_TYPE_VACCIN
from api.views import API_Datawarehouse_D_DATE
from api.views import API_Datawarehouse_D_LOCATION
from api.views import API_Datawarehouse_F_FLUX

from app.models import Flux
from app.models import D_TYPE_VACCIN
from app.models import D_DATE
from app.models import D_LOCATION
from app.models import F_FLUX

import json

class TestFlux(TestCase):
    
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view_flux = API_Operational_Data_Store_Flux.as_view()
        self.test_flux = Flux.objects.create(
            id=1,
            code_region="84",
            libelle_region="ARA",
            code_departement="01",
            libelle_departement="Ain",
            date_fin_semaine="2021-06-13",
            type_de_vaccin="AstraZeneca",
            nb_ucd="378",
            nb_doses="3780"
        )

    def test_get_flux_list(self):
        request = self.factory.get('/flux/')
        response = self.view_flux(request)
        self.assertEqual(response.status_code, 200)
        data = response.data
        self.assertEqual(data['count'], Flux.objects.count())

    def test_get_flux_detail(self):
        request = self.factory.get(f'/flux/{self.test_flux.id}/')
        response = self.view_flux(request, id=self.test_flux.id)
        self.assertEqual(response.status_code, 200)
        data = response.data
        self.assertEqual(data['data'][0]['id'], self.test_flux.id)

    def test_create_flux(self):
        new_flux_data = {
            "code_region": "85",
            "libelle_region": "New Region",
            "code_departement": "02",
            "libelle_departement": "New Departement",
            "date_fin_semaine": "2022-01-01",
            "type_de_vaccin": "Pfizer",
            "nb_ucd": "500",
            "nb_doses": "5000"
        }
        request = self.factory.post('/flux/', new_flux_data, format='json')
        response = self.view_flux(request)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Flux.objects.count(), 2)

    def test_update_flux(self):
        updated_data = {
            "id": 1,
            "code_region": "84",
            "libelle_region": "Updated Region",
            "code_departement": "01",
            "libelle_departement": "Ain",
            "date_fin_semaine": "2021-06-13",
            "type_de_vaccin": "AstraZeneca",
            "nb_ucd": "400",
            "nb_doses": "4000"
        }
        request = self.factory.put(f'/flux/{self.test_flux.id}/', updated_data, format='json')
        response = self.view_flux(request, id=self.test_flux.id)
        response.render()
        print(response.content)
        self.assertEqual(response.status_code, 200)
        updated_flux = Flux.objects.get(id=updated_data['id'])
        self.assertEqual(updated_flux.libelle_region, updated_data['libelle_region'])
        self.assertEqual(updated_flux.nb_ucd, updated_data['nb_ucd'])

    def test_partial_update_flux(self):
        updated_data = {
            "libelle_region": "Updated Region",
        }
        request = self.factory.patch(f'/flux/{self.test_flux.id}/', updated_data, format='json')
        response = self.view_flux(request, id=self.test_flux.id)
        self.assertEqual(response.status_code, 200)
        updated_flux = Flux.objects.get(id=self.test_flux.id)
        self.assertEqual(updated_flux.libelle_region, updated_data['libelle_region'])

    def test_delete_flux(self):
        request = self.factory.delete(f'/flux/{self.test_flux.id}/')
        response = self.view_flux(request, id=self.test_flux.id)
        self.assertEqual(response.status_code, 204)
        self.assertFalse(Flux.objects.filter(id=self.test_flux.id).exists())

class TestD_TYPE_VACCIN(TestCase):
    
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view_d_type_vaccin = API_Datawarehouse_D_TYPE_VACCIN.as_view()
        self.test_d_type_vaccin = D_TYPE_VACCIN.objects.create(
            vaccinlabel="AstraZeneca"
        )

    def test_get_d_type_vaccin_list(self):
        request = self.factory.get('/d_type_vaccin/')
        response = self.view_d_type_vaccin(request)
        self.assertEqual(response.status_code, 200)
        data = response.data
        self.assertEqual(data['count'], D_TYPE_VACCIN.objects.count())

    def test_get_d_type_vaccin_detail(self):
        request = self.factory.get(f'/d_type_vaccin/{self.test_d_type_vaccin.vaccinlabel}/')
        response = self.view_d_type_vaccin(request, vaccinlabel=self.test_d_type_vaccin.vaccinlabel)
        self.assertEqual(response.status_code, 200)
        data = response.data
        self.assertEqual(data['data'][0]['vaccinlabel'], self.test_d_type_vaccin.vaccinlabel)

    def test_create_d_type_vaccin(self):
        new_d_type_vaccin_data = {
            "vaccinlabel": "Pfizer"
        }
        request = self.factory.post('/d_type_vaccin/', new_d_type_vaccin_data, format='json')
        response = self.view_d_type_vaccin(request)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(D_TYPE_VACCIN.objects.count(), 2)

    def test_update_d_type_vaccin(self):
        updated_data = {
            "vaccinlabel": "Updated AstraZeneca"
        }
        request = self.factory.put(f'/d_type_vaccin/{self.test_d_type_vaccin.vaccinlabel}/', updated_data, format='json')
        response = self.view_d_type_vaccin(request, vaccinlabel=self.test_d_type_vaccin.vaccinlabel)
        self.assertEqual(response.status_code, 200)
        updated_d_type_vaccin = D_TYPE_VACCIN.objects.get(vaccinlabel=updated_data['vaccinlabel'])
        self.assertEqual(updated_d_type_vaccin.vaccinlabel, updated_data['vaccinlabel'])

    def test_partial_update_d_type_vaccin(self):
        updated_data = {
            "vaccinlabel": "Updated AstraZeneca"
        }
        request = self.factory.patch(f'/d_type_vaccin/{self.test_d_type_vaccin.vaccinlabel}/', updated_data, format='json')
        response = self.view_d_type_vaccin(request, vaccinlabel=self.test_d_type_vaccin.vaccinlabel)
        self.assertEqual(response.status_code, 200)
        updated_d_type_vaccin = D_TYPE_VACCIN.objects.get(vaccinlabel=updated_data['vaccinlabel'])
        self.assertEqual(updated_d_type_vaccin.vaccinlabel, updated_data['vaccinlabel'])

    def test_delete_d_type_vaccin(self):
        request = self.factory.delete(f'/d_type_vaccin/{self.test_d_type_vaccin.vaccinlabel}/')
        response = self.view_d_type_vaccin(request, vaccinlabel=self.test_d_type_vaccin.vaccinlabel)
        self.assertEqual(response.status_code, 204)

class TestD_DATE(TestCase):
    
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view_d_date = API_Datawarehouse_D_DATE.as_view()
        self.test_d_date = D_DATE.objects.create(
            date_fin_semaine="2020-12-27"
        )

    def test_get_d_date_list(self):
        request = self.factory.get('/d_date/')
        response = self.view_d_date(request)
        self.assertEqual(response.status_code, 200)
        data = response.data
        self.assertEqual(data['count'], D_DATE.objects.count())

    def test_get_d_date_detail(self):
        request = self.factory.get(f'/d_date/{self.test_d_date.date_fin_semaine}/')
        response = self.view_d_date(request, date_fin_semaine=self.test_d_date.date_fin_semaine)
        self.assertEqual(response.status_code, 200)
        data = response.data
        self.assertEqual(data['data'][0]['date_fin_semaine'], self.test_d_date.date_fin_semaine)

    def test_create_d_date(self):
        new_d_date_data = {
            "date_fin_semaine": "2021-01-03"
        }
        request = self.factory.post('/d_date/', new_d_date_data, format='json')
        response = self.view_d_date(request)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(D_DATE.objects.count(), 2)

    def test_update_d_date(self):
        updated_data = {
            "date_fin_semaine": "2021-01-10"
        }
        request = self.factory.put(f'/d_date/{self.test_d_date.date_fin_semaine}/', updated_data, format='json')
        response = self.view_d_date(request, date_fin_semaine=self.test_d_date.date_fin_semaine)
        self.assertEqual(response.status_code, 200)
        updated_d_date = D_DATE.objects.get(date_fin_semaine=updated_data['date_fin_semaine'])
        self.assertEqual(updated_d_date.date_fin_semaine.strftime('%Y-%m-%d'), updated_data['date_fin_semaine'])

    def test_partial_update_d_date(self):
        updated_data = {
            "date_fin_semaine": "2021-01-17"
        }
        request = self.factory.patch(f'/d_date/{self.test_d_date.date_fin_semaine}/', updated_data, format='json')
        response = self.view_d_date(request, date_fin_semaine=self.test_d_date.date_fin_semaine)
        self.assertEqual(response.status_code, 200)
        updated_d_date = D_DATE.objects.get(date_fin_semaine=updated_data['date_fin_semaine'])
        self.assertEqual(updated_d_date.date_fin_semaine.strftime('%Y-%m-%d'), updated_data['date_fin_semaine'])

    def test_delete_d_date(self):
        request = self.factory.delete(f'/d_date/{self.test_d_date.date_fin_semaine}/')
        response = self.view_d_date(request, date_fin_semaine=self.test_d_date.date_fin_semaine)
        self.assertEqual(response.status_code, 204)
        self.assertFalse(D_DATE.objects.filter(date_fin_semaine=self.test_d_date.date_fin_semaine).exists())

class TestD_LOCATION(TestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        self.view_d_location = API_Datawarehouse_D_LOCATION.as_view()
        self.test_d_location_data = {
            "code_region": 1,
            "code_departement": "971",
            "libelle_region": "GDP",
            "libelle_departement": "Guadeloupe"
        }

    def test_get_d_location_list(self):
        D_LOCATION.objects.create(**self.test_d_location_data)

        request = self.factory.get('/d_location/')
        response = self.view_d_location(request)
        
        self.assertEqual(response.status_code, 200)
        data = response.data
        self.assertEqual(data['count'], D_LOCATION.objects.count())

    def test_get_d_location_detail(self):
        d_location_instance = D_LOCATION.objects.create(**self.test_d_location_data)
        
        request = self.factory.get(f'/d_location/{d_location_instance.code_region_code_departement}/')
        response = self.view_d_location(request, code_region_code_departement=d_location_instance.code_region_code_departement)

        self.assertEqual(response.status_code, 200)
        data = response.data
        self.assertEqual(data['data'][0]['code_region'], self.test_d_location_data['code_region'])

    def test_create_d_location(self):
        # Préparer les données à envoyer en POST
        new_d_location_data = {
            "code_region_code_departement": "2-972",
            "code_region": 2,
            "code_departement": "972",
            "libelle_region": "MTP",
            "libelle_departement": "Martinique"
        }
        # Envoyer la requête POST à la vue
        request = self.factory.post('/d_location/', new_d_location_data)
        response = self.view_d_location(request)

        # Vérifier le code de statut et le contenu de la réponse
        self.assertEqual(response.status_code, 201)
        data = response.data
        self.assertEqual(data['code_region'], new_d_location_data['code_region'])
        self.assertEqual(data['code_departement'], new_d_location_data['code_departement'])
        self.assertEqual(data['libelle_region'], new_d_location_data['libelle_region'])
        self.assertEqual(data['libelle_departement'], new_d_location_data['libelle_departement'])

        # Vérifier que l'objet a bien été créé dans la base de données
        d_location_instance = D_LOCATION.objects.get(code_region_code_departement=data['code_region_code_departement'])
        self.assertIsNotNone(d_location_instance)

    def test_update_d_location(self):
        d_location_instance = D_LOCATION.objects.create(**self.test_d_location_data)
        updated_data = {
            "libelle_region": "Updated Region",
        }
        request = self.factory.patch(f'/d_location/{d_location_instance.code_region_code_departement}/', updated_data, format='json')
        response = self.view_d_location(request, code_region_code_departement=d_location_instance.code_region_code_departement)

        self.assertEqual(response.status_code, 200)

        d_location_instance.refresh_from_db()
        self.assertEqual(d_location_instance.libelle_region, updated_data['libelle_region'])

    def test_partial_update_d_location(self):
        d_location_instance = D_LOCATION.objects.create(**self.test_d_location_data)
        updated_data = {
            "libelle_region": "Updated Region",
        }
        request = self.factory.patch(f'/d_location/{d_location_instance.code_region_code_departement}/', updated_data, format='json')
        response = self.view_d_location(request, code_region_code_departement=d_location_instance.code_region_code_departement)

        self.assertEqual(response.status_code, 200)
        updated_d_location = D_LOCATION.objects.get(code_region_code_departement=d_location_instance.code_region_code_departement)
        self.assertEqual(updated_d_location.libelle_region, updated_data['libelle_region'])

    def test_delete_d_location(self):
        d_location_instance = D_LOCATION.objects.create(**self.test_d_location_data)
        request = self.factory.delete(f'/d_location/{d_location_instance.code_region_code_departement}/')
        response = self.view_d_location(request, code_region_code_departement=d_location_instance.code_region_code_departement)

        self.assertEqual(response.status_code, 204)
        self.assertFalse(D_LOCATION.objects.filter(code_region_code_departement=d_location_instance.code_region_code_departement).exists())
