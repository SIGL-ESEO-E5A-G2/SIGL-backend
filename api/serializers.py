from rest_framework import serializers

# =================== EXEMPLE =======================
from api.models import Person, Species

class PersonSerializer(serializers.ModelSerializer):
   class Meta:
       model = Person
       fields = ('name', 'birth_year', 'eye_color', 'species')


class SpeciesSerializer(serializers.ModelSerializer):
   class Meta:
       model = Species
       fields = ('name', 'classification', 'language', 'planet')
# =================== EXEMPLE =======================