from rest_framework import serializers

# =================== EXEMPLE =======================
from api.models import Utilisateur, TuteurPedagogique, CoordinatriceAlternance, MaitreAlternance, Apprenti

# class PersonSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = Person
#        fields = ('name', 'birth_year', 'eye_color', 'species')

# =================== EXEMPLE =======================

class UtilisateurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Utilisateur
        fields = '__all__'

class TuteurPedagogiqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = TuteurPedagogique
        fields = '__all__'

class MaitreAlternanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaitreAlternance
        fields = '__all__'

class CoordinatriceAlternanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoordinatriceAlternance
        fields = '__all__'

class ApprentiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apprenti
        fields = '__all__'