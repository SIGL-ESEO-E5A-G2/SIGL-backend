from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet

from api.serializers import UtilisateurSerializer
from api.models import Utilisateur

# =================== EXEMPLE =======================
# class PersonViewSet(viewsets.ModelViewSet):
#    queryset = Person.objects.all()
#    serializer_class = PersonSerializer

# =================== EXEMPLE =======================

class UtilisateurViewSet(ModelViewSet):
    serializer_class = UtilisateurSerializer
 
    def get_queryset(self):
        return Utilisateur.objects.all()