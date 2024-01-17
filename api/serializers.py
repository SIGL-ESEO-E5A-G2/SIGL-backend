from rest_framework import serializers
from api.models import *
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response

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
    utilisateur = UtilisateurSerializer(many=False)
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
        
class ProfesseurDetailSerializer(serializers.ModelSerializer):
    utilisateur = UtilisateurSerializer(many=False)
    class Meta:
        model = Professeur
        fields = '__all__'

class ProfesseurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professeur
        fields = '__all__'
        
class MembreExterieurDetailSerializer(serializers.ModelSerializer):
    utilisateur = UtilisateurSerializer(many=False)
    class Meta:
        model = MembreExterieur
        fields = '__all__'

class MembreExterieurSerializer(serializers.ModelSerializer):
    class Meta:
        model = MembreExterieur
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

class MessageFeedSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)
    class Meta:
        model = Message
        fields = '__all__'
        
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        
        createur = Utilisateur.objects.get(email=instance.createur)
        representation['createur'] = f'{createur.nom} {createur.prenom}'
        del representation['destinataire']
        try :
            depot = Depot.objects.get(message = instance)
            representation['depot'] = DepotSerializer(depot, many = False).data
        except :
            pass
        
        try :
            all_commentaire = Commentaire.objects.filter(message = instance)
            commentaire_list = []
            for commentaire in all_commentaire :
                commentaire_list.append(CommentaireDetailSerializer(commentaire, many = False).data)
            commentaire_list.reverse()

            representation['commentaire'] = commentaire_list
        except :
            pass

        return representation


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'
        
class MessageDetailSerializer(serializers.ModelSerializer):
    createur = UtilisateurSerializer(many=False)
    destinataire = UtilisateurSerializer(many=True)
    tags = TagSerializer(many=True)
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

from django.shortcuts import get_object_or_404
from rest_framework import status

class GrilleEvaluationSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrilleEvaluation
        fields = '__all__'
    
    def create(self, validated_data):
        
        id_apprenti = self.context['request'].data.get('id_apprenti', None)
        apprenti = get_object_or_404(Apprenti, id=id_apprenti)
        if apprenti.grilleEvaluation != None :
            return apprenti.grilleEvaluation
        
        grille_evaluation = GrilleEvaluation.objects.create(**validated_data)
        
        apprenti.grilleEvaluation = grille_evaluation
        apprenti.save()
        # Crée 6 compétences apprentis pour chaque compétence existante
        competences_existantes = Competence.objects.all()
        semestre = ['S5','S6','S7','S8','S9','S10']
        
        for competence in competences_existantes:
            i = 0
            for _ in range(6):
                CompetenceApprenti.objects.create(
                    grilleEvaluation=grille_evaluation,
                    competence=competence,
                    semestre=semestre[i]
                )
                i += 1

        return grille_evaluation
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        competences_existantes = Competence.objects.all()
        i = 0
        for competence in competences_existantes:
            i+=1
            competences_apprentis = CompetenceApprenti.objects.filter(grilleEvaluation=instance, competence= competence)
            representation[f'competence_{i}'] = CompetenceSerializer(competence, many=False).data
            representation[f'competenceApprenti_{i}'] = CompetenceApprentiSerializer(competences_apprentis, many=True).data

        return representation

        
class CompetenceApprentiSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompetenceApprenti
        fields = '__all__'
        
class CompetenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Competence
        fields = '__all__'

class CompetenceApprentiDetailSerializer(serializers.ModelSerializer):
    competence = CompetenceSerializer(many=False)
    class Meta:
        model = CompetenceApprenti
        fields = '__all__'

class CommentaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commentaire
        fields = '__all__'
        
class CommentaireDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commentaire
        fields = '__all__'
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        createur = Utilisateur.objects.get(email=instance.createur)
        representation['createur']=f'{createur.nom} {createur.prenom}'
        return representation