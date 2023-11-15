from rest_framework import serializers
from api.models import *
from django.contrib.auth import authenticate

# =================== EXEMPLE =======================
# class PersonSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = Person
#        fields = ('name', 'birth_year', 'eye_color', 'species')
# =================== EXEMPLE =======================

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'

#--- Utilisateur ---

class UtilisateurSerializer(serializers.ModelSerializer):
    roles = RoleSerializer(many=True)

    class Meta:
        model = Utilisateur
        fields = '__all__'

class AuthentificationSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
    def validate(self, data):
        email = data.get('email')
        password = data.get('password')
        if email and password:
            utilisateur =Utilisateur.objects.filter(email=email, password=password).first()
            if utilisateur:
                data['utilisateur'] = utilisateur
            else:
                raise serializers.ValidationError("L'adresse e-mail ou le mot de passe est incorrect.")
        else:
            raise serializers.ValidationError("L'adresse e-mail et le mot de passe sont requis.")

        return data


class AdministrateurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Administrateur
        fields = '__all__'
#--- TuteurPedagogique ---

class TuteurPedagogiqueDetailSerializer(serializers.ModelSerializer):
    utilisateur = UtilisateurSerializer(many=False)
    class Meta:
        model = TuteurPedagogique
        fields = '__all__'

class TuteurPedagogiqueSerializer(serializers.ModelSerializer):
    utilisateur = UtilisateurSerializer(many=False)
    class Meta:
        model = TuteurPedagogique
        fields = '__all__'

#--- MaitreAlternance ---


class MaitreAlternanceDetailSerializer(serializers.ModelSerializer):
    utilisateur = UtilisateurSerializer(many=False)
    class Meta:
        model = MaitreAlternance
        fields = '__all__'

class MaitreAlternanceSerializer(serializers.ModelSerializer):
    utilisateur = UtilisateurSerializer(many=False)
    class Meta:
        model = MaitreAlternance
        fields = '__all__'

#--- CoordinatriceAlternance ---


class CoordinatriceAlternanceDetailSerializer(serializers.ModelSerializer):
    utilisateur = UtilisateurSerializer(many=False)
    class Meta:
        model = CoordinatriceAlternance
        fields = '__all__'


class CoordinatriceAlternanceSerializer(serializers.ModelSerializer):
    utilisateur = UtilisateurSerializer(many=False)
    class Meta:
        model = CoordinatriceAlternance
        fields = '__all__'

#--- Apprenti ---

class ApprentiDetailSerializer(serializers.ModelSerializer):
    utilisateur = UtilisateurSerializer(many=False)
    tuteurPedagogique = TuteurPedagogiqueDetailSerializer(many=False)
    maitreAlternance = MaitreAlternanceDetailSerializer(many=False)
    class Meta:
        model = Apprenti
        fields = '__all__'
        
class ApprentiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apprenti
        fields = '__all__'


# --- Apprenti ---

class MessageDetailSerializer(serializers.ModelSerializer):
    utilisateur = UtilisateurSerializer(many=False)

    class Meta:
        model = Message
        fields = '__all__'


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'

class DepotDetailSerializer(serializers.ModelSerializer):
    message = MessageDetailSerializer(many=False)

    class Meta:
        model = Depot
        fields = '__all__'


class DepotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Depot
        fields = '__all__'

