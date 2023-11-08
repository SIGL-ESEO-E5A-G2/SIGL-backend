from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet

from api.serializers import UtilisateurSerializer, TuteurPedagogiqueSerializer, MaitreAlternanceSerializer, CoordinatriceAlternanceSerializer, ApprentiSerializer
from api.models import Utilisateur, TuteurPedagogique, MaitreAlternance, CoordinatriceAlternance, Apprenti

# =================== EXEMPLE =======================
# class PersonViewSet(viewsets.ModelViewSet):
#    queryset = Person.objects.all()
#    serializer_class = PersonSerializer

# =================== EXEMPLE =======================

class UtilisateurViewSet(ModelViewSet):
    serializer_class = UtilisateurSerializer
 
    def get_queryset(self):
        return Utilisateur.objects.all()

class TuteurPedagogiqueViewSet(ModelViewSet):
    serializer_class = TuteurPedagogiqueSerializer
 
    def get_queryset(self):
        return TuteurPedagogique.objects.all()

class MaitreAlternanceViewSet(ModelViewSet):
    serializer_class = MaitreAlternanceSerializer
 
    def get_queryset(self):
        return MaitreAlternance.objects.all()

class CoordinatriceAlternanceViewSet(ModelViewSet):
    serializer_class = CoordinatriceAlternanceSerializer
 
    def get_queryset(self):
        return CoordinatriceAlternance.objects.all()

class ApprentiViewSet(ModelViewSet):
    serializer_class = ApprentiSerializer
 
    def get_queryset(self):
        return Apprenti.objects.all()
