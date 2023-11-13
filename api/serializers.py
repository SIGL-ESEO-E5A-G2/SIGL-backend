from rest_framework import serializers


from api.models import Utilisateur, TuteurPedagogique, CoordinatriceAlternance, MaitreAlternance, Apprenti

# =================== EXEMPLE =======================
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
    utilisateur = UtilisateurSerializer(many=False)
    class Meta:
        model = TuteurPedagogique
        fields = '__all__'

class MaitreAlternanceSerializer(serializers.ModelSerializer):
    utilisateur = UtilisateurSerializer(many=False)
    class Meta:
        model = MaitreAlternance
        fields = '__all__'

class CoordinatriceAlternanceSerializer(serializers.ModelSerializer):
    utilisateur = UtilisateurSerializer(many=False)
    class Meta:
        model = CoordinatriceAlternance
        fields = '__all__'

class ApprentiDetailSerializer(serializers.ModelSerializer):
    utilisateur = UtilisateurSerializer(many=False)
    tuteurPedagogique = TuteurPedagogiqueSerializer(many=False)
    maitreAlternance = MaitreAlternanceSerializer(many=False)
    class Meta:
        model = Apprenti
        fields = '__all__'
        
class ApprentiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apprenti
        fields = '__all__'