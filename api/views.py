from rest_framework import viewsets

from api.serializers import PersonSerializer, SpeciesSerializer
from api.models import Person, Species

# =================== EXEMPLE =======================
# class PersonViewSet(viewsets.ModelViewSet):
#    queryset = Person.objects.all()
#    serializer_class = PersonSerializer

# =================== EXEMPLE =======================