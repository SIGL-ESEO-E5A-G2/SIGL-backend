from django.urls import reverse_lazy
from rest_framework.test import APITestCase

from api.models import Utilisateur

class TestUtilisateur(APITestCase):
    url = reverse_lazy('utilisateurs-list')

    def test_utilisateur(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

class TestApprenti(APITestCase):
    url = reverse_lazy('apprenti-list')

    def test_apprenti(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

class TestTuteurPedagogique(APITestCase):
    url = reverse_lazy('tuteurpedagogique-list')

    def test_tuteurpedagogique(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

class TestMaitreAlternance(APITestCase):
    url = reverse_lazy('maitrealternance-list')

    def test_maitrealternance(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

class TestCoordinatriceAlternance(APITestCase):
    url = reverse_lazy('coordinatricealternance-list')

    def test_coordinatricealternance(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

class TestApprentiDetail(APITestCase):
    url = reverse_lazy('apprentidetail-list')

    def test_apprentidetail(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

class TestAuthentification(APITestCase):
    url = reverse_lazy('authentification')

    def setUp(self):
        self.utilisateur = Utilisateur.objects.create(email='test@test.com', password='motdepasse')

    def test_authentification_succes(self):
        data = {'email': 'test@test.com', 'password': 'motdepasse'}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 200)

    def test_authentification_echec(self):
        data = {'email': 'test@test.com', 'password': 'motdepasse_faux'}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 400)