from rest_framework import serializers
from api.models import *
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed

# =================== EXEMPLE =======================
# class PersonSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = Person
#        fields = ('name', 'birth_year', 'eye_color', 'species')
# =================== EXEMPLE =======================

class PromotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promotion
        fields = '__all__'
class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'

#--- Utilisateur ---

class UtilisateurSerializer(serializers.ModelSerializer):

    class Meta:
        model = Utilisateur
        fields = '__all__'

class UtilisateurDetailSerializer(serializers.ModelSerializer):
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
            utilisateur =authenticate(email=email, password=password)
            if utilisateur:
                data['utilisateur'] = utilisateur
            else:
                raise AuthenticationFailed("L'adresse e-mail ou le mot de passe est incorrect.")
        else:
            raise AuthenticationFailed("L'adresse e-mail et le mot de passe sont requis.")

        return data


class AdministrateurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Administrateur
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class OpcoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Opco
        fields = '__all__'

class EntrepriseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entreprise
        fields = '__all__'
class ResponsableEntrepriseDetailSerializer(serializers.ModelSerializer):
    entreprise = EntrepriseSerializer(many=False)
    class Meta:
        model = ResponsableEntreprise
        fields = '__all__'

class ResponsableEntrepriseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResponsableEntreprise
        fields = '__all__'


#--- TuteurPedagogique ---

class TuteurPedagogiqueDetailSerializer(serializers.ModelSerializer):
    utilisateur = UtilisateurSerializer(many=False)
    class Meta:
        model = TuteurPedagogique
        fields = '__all__'

class TuteurPedagogiqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = TuteurPedagogique
        fields = '__all__'

#--- MaitreAlternance ---


class MaitreAlternanceDetailSerializer(serializers.ModelSerializer):
    utilisateur = UtilisateurSerializer(many=False)
    entreprise = EntrepriseSerializer(many=False)
    class Meta:
        model = MaitreAlternance
        fields = '__all__'

class MaitreAlternanceSerializer(serializers.ModelSerializer):
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
    class Meta:
        model = CoordinatriceAlternance
        fields = '__all__'

#--- Apprenti ---

class ApprentiDetailSerializer(serializers.ModelSerializer):
    utilisateur = UtilisateurSerializer(many=False)
    tuteurPedagogique = TuteurPedagogiqueDetailSerializer(many=False)
    maitreAlternance = MaitreAlternanceDetailSerializer(many=False)
    entreprise = EntrepriseSerializer(many=False)
    opco = EntrepriseSerializer(many=False)
    promotion = PromotionSerializer(many=False)
    class Meta:
        model = Apprenti
        fields = '__all__'
        
class ApprentiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apprenti
        fields = '__all__'


# --- Apprenti ---

class MessageDetailSerializer(serializers.ModelSerializer):
    createur = UtilisateurSerializer(many=False)
    destinataire = UtilisateurSerializer(many=True)
    tags = TagSerializer(many=True)
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

class EvenementDetailSerializer(serializers.ModelSerializer):
    apprenti = ApprentiDetailSerializer(many=False)
    class Meta:
        model = Evenement
        fields = '__all__'

class EvenementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evenement
        fields = '__all__'


class EntretienSemestrielDetailSerializer(serializers.ModelSerializer):
    evenement = EvenementDetailSerializer(many=False)
    tuteurPedagogique = TuteurPedagogiqueDetailSerializer(many=False)
    maitreAlternance = MaitreAlternanceDetailSerializer(many=False)
    class Meta:
        model = EntretienSemestriel
        fields = '__all__'


class EntretienSemestrielSerializer(serializers.ModelSerializer):
    class Meta:
        model = EntretienSemestriel
        fields = '__all__'

