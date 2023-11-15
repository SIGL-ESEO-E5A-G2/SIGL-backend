from django.urls import reverse_lazy
from rest_framework.test import APITestCase

from api.models import Utilisateur
from api.models import Apprenti

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