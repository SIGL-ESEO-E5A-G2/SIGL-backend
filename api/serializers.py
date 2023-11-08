from rest_framework import serializers

# =================== EXEMPLE =======================
from api.models import Utilisateur

# class PersonSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = Person
#        fields = ('name', 'birth_year', 'eye_color', 'species')

# =================== EXEMPLE =======================

class UtilisateurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Utilisateur
        fields = '__all__'