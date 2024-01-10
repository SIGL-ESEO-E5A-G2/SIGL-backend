from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticated

from api.serializers import *
from django.conf import settings
from api.models import *

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from django.core import serializers as core_serializers
from django.http import HttpResponseBadRequest, HttpResponse, HttpResponseNotFound
from rest_framework.views import APIView
import jwt, datetime

from django.views.decorators.csrf import csrf_exempt

from azure.storage.blob import BlobServiceClient

# =================== EXEMPLE =======================
# class PersonViewSet(viewsets.ModelViewSet):
#    queryset = Person.objects.all()
#    serializer_class = PersonSerializer

# =================== EXEMPLE =======================

#--- Utilisateur ---

class UtilisateurViewSet(ModelViewSet):
    serializer_class = UtilisateurSerializer
    #permission_classes = {IsAuthenticated, }
    def get_queryset(self):
        return Utilisateur.objects.all()

    def create(self, request, *args, **kwargs):

        utilisateur = Utilisateur.objects.create_user(email=request.data['email'],
                                                      nom=request.data['nom'],
                                                      prenom=request.data['prenom'],
                                                      mot_de_passe=request.data['password'])

        return Response({'id': utilisateur.id}, status=status.HTTP_200_OK)


class UtilisateurDetailViewSet(ReadOnlyModelViewSet):
    serializer_class = UtilisateurDetailSerializer

    def get_queryset(self):
        return Utilisateur.objects.all()

class AuthentificationUtilisateurView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = AuthentificationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True) :
            utilisateur = serializer.validated_data['utilisateur']
            payload={
                'id':utilisateur.id,
                'nom': utilisateur.nom,
                'prenom': utilisateur.prenom,
                'email': utilisateur.email,
                'roles':core_serializers.serialize("json",utilisateur.roles.all()),
                'exp': datetime.datetime.utcnow()+datetime.timedelta(minutes=60),
                'iat':datetime.datetime.utcnow(),
            }

            jwt_token = jwt.encode(payload, 'secret', algorithm='HS256')
            token = Token.objects.get_or_create(user=utilisateur)

            response = Response({'jwt_token': jwt_token, 'access_token': str(token[0]), 'id': utilisateur.id}, status=status.HTTP_200_OK)

            # Autoriser les connexions depuis le domaine de l'application front-end
            response["Content-Security-Policy"] = "default-src 'self' https://sigl.francecentral.cloudapp.azure.com"

            return response
        else:
            return Response({}, status=status.HTTP_401_UNAUTHORIZED)

class AdministrateurViewSet(ModelViewSet):
    serializer_class = AdministrateurSerializer
    def get_queryset(self):
        return Administrateur.objects.all()

#--- TuteurPedagogique ---

class TuteurPedagogiqueViewSet(ModelViewSet):
    serializer_class = TuteurPedagogiqueSerializer
    def get_queryset(self):
        return TuteurPedagogique.objects.all()


class TuteurPedagogiqueDetailViewSet(ReadOnlyModelViewSet):
    serializer_class = TuteurPedagogiqueDetailSerializer
    def get_queryset(self):
        return TuteurPedagogique.objects.all()

#--- MaitreAlternance ---
class MaitreAlternanceDetailViewSet(ReadOnlyModelViewSet):
    serializer_class = MaitreAlternanceDetailSerializer
    def get_queryset(self):
        return MaitreAlternance.objects.all()

class MaitreAlternanceViewSet(ModelViewSet):
    serializer_class = MaitreAlternanceSerializer
    def get_queryset(self):
        return MaitreAlternance.objects.all()
#--- CoordinatriceAlternance ---
class CoordinatriceAlternanceDetailViewSet(ReadOnlyModelViewSet):
    serializer_class = CoordinatriceAlternanceDetailSerializer
    def get_queryset(self):
        return CoordinatriceAlternance.objects.all()

#--- CoordinatriceAlternance ---

class CoordinatriceAlternanceViewSet(ModelViewSet):
    serializer_class = CoordinatriceAlternanceSerializer
    def get_queryset(self):
        return CoordinatriceAlternance.objects.all()

#--- Apprenti ---

class ApprentiDetailViewSet(ReadOnlyModelViewSet):
    serializer_class = ApprentiDetailSerializer
    def get_queryset(self):
        return Apprenti.objects.all()


class ApprentiViewSet(ModelViewSet):
    serializer_class = ApprentiSerializer
 
    def get_queryset(self):
        return Apprenti.objects.all()

class TagViewSet(ModelViewSet):
    serializer_class = TagSerializer

    def get_queryset(self):
        return Tag.objects.all()

class MessageViewSet(ModelViewSet):
    serializer_class = MessageSerializer

    def get_queryset(self):
        return Message.objects.all()


class MessageDetailViewSet(ReadOnlyModelViewSet):
    serializer_class = MessageDetailSerializer

    def get_queryset(self):
        return Message.objects.all()

class DepotViewSet(ModelViewSet):
    serializer_class = DepotSerializer

    def get_queryset(self):
        return Depot.objects.all()


class DepotDetailViewSet(ReadOnlyModelViewSet):
    serializer_class = DepotDetailSerializer

    def get_queryset(self):
        return Depot.objects.all()

class PromotionViewSet(ModelViewSet):
    serializer_class = PromotionSerializer
    def get_queryset(self):
        return Promotion.objects.all()

class EntrepriseViewSet(ModelViewSet):
    serializer_class = EntrepriseSerializer
    def get_queryset(self):
        return Entreprise.objects.all()

class OpcoViewSet(ModelViewSet):
    serializer_class = OpcoSerializer
    def get_queryset(self):
        return Opco.objects.all()

class ResponsableEntrepriseViewSet(ModelViewSet):
    serializer_class = ResponsableEntrepriseSerializer
    def get_queryset(self):
        return ResponsableEntreprise.objects.all()

class ResponsableEntrepriseDetailViewSet(ReadOnlyModelViewSet):
    serializer_class = ResponsableEntrepriseDetailSerializer
    def get_queryset(self):
        return ResponsableEntreprise.objects.all()

class ApprentiPromotionViewSet(ModelViewSet):
    serializer_class = ApprentiDetailSerializer
    def get_queryset(self):
        try :
            promotion = self.request.query_params.get('promotion')
            print(self.request.query_params)
            return Apprenti.objects.filter(promotion = promotion)
        except Exception as error :
            print(error)
            raise serializers.ValidationError({'promotion': 'Veuillez indiquer une promotion'})
        
class ApprentiUtilisateurViewSet(ReadOnlyModelViewSet):
    serializer_class = ApprentiDetailSerializer
    def get_queryset(self):
        try :
            utilisateur = self.request.query_params.get('utilisateur')
            print(self.request.query_params)
            return Apprenti.objects.filter(utilisateur = utilisateur)
        except Exception as error :
            print(error)
            raise serializers.ValidationError({'utilisateur': 'Veuillez indiquer un utilisateur'})
        
class MessageUtilisateurViewSet(ModelViewSet):
    serializer_class = MessageSerializer
    def get_queryset(self):
        try :
            utilisateur = self.request.query_params.get('utilisateur')
            print(self.request.query_params)
            return Message.objects.filter(destinataire = utilisateur)
        except Exception as error :
            print(error)
            raise serializers.ValidationError({'utilisateur': 'Veuillez indiquer un utilisateur'})
    


class EvenementViewSet(ModelViewSet):
    serializer_class = EvenementSerializer
    def get_queryset(self):
        return Evenement.objects.all()

class EntretienSemestrielViewSet(ModelViewSet):
    serializer_class = EntretienSemestrielSerializer
    def get_queryset(self):
        return EntretienSemestriel.objects.all()

class EntretienSemestrielDetailViewSet(ReadOnlyModelViewSet):
    serializer_class = EntretienSemestrielDetailSerializer
    def get_queryset(self):
        return EntretienSemestriel.objects.all()

# views.py
@csrf_exempt
def upload_pdf_to_azure(request):
    if request.method == 'POST' and request.FILES.get('pdf_file') and request.POST['file_path']:
        pdf_file = request.FILES['pdf_file']
        path = request.POST['file_path']
        print(request.POST['file_path'])
        # Connexion au compte Azure Storage Blob
        blob_service_client = BlobServiceClient(account_url=f"https://{settings.AZURE_ACCOUNT_NAME}.blob.core.windows.net", credential=settings.AZURE_ACCOUNT_KEY)
        container_client = blob_service_client.get_container_client(settings.AZURE_CONTAINER)

        # Enregistrement du fichier PDF dans le blob storage Azure
        blob_client = container_client.upload_blob(name=path+pdf_file.name, data=pdf_file.read(), overwrite=True)

        # Vous pouvez maintenant retourner une réponse ou effectuer d'autres actions nécessaires
        return HttpResponse("Fichier PDF téléchargé avec succès.")

    return HttpResponseBadRequest("Erreur lors du téléchargement du fichier PDF.")


# views.py
import json
from urllib.parse import unquote  # Import unquote
@csrf_exempt
def get_pdf_from_azure(request):
    try:
        # Obtenir le corps de la requête
        body = json.loads(request.body.decode('utf-8'))

        # Obtenir le chemin du fichier à partir du corps de la requête
        file_path = body.get('file_path', '')

        if not file_path:
            return HttpResponseBadRequest("Le paramètre 'file_path' est requis dans le corps de la requête.")

        # Décodez le chemin si nécessaire (peut être nécessaire pour les caractères spéciaux)
        file_path = unquote(file_path)

        # Connexion au compte Azure Storage Blob
        blob_service_client = BlobServiceClient(account_url=f"https://{settings.AZURE_ACCOUNT_NAME}.blob.core.windows.net", credential=settings.AZURE_ACCOUNT_KEY)
        container_client = blob_service_client.get_container_client(settings.AZURE_CONTAINER)

        # Vérifier si le fichier existe dans le blob storage Azure
        blob_client = container_client.get_blob_client(blob=file_path)
        if blob_client.exists():
            # Récupérer le contenu du fichier PDF
            blob_data = blob_client.download_blob()
            pdf_content = blob_data.read()

            # Configurer la réponse HTTP pour le fichier PDF
            response = HttpResponse(pdf_content, content_type='application/pdf')
            response['Content-Disposition'] = f'inline; filename="{file_path}"'
            return response
        else:
            # Retourner une réponse 404 si le fichier n'existe pas
            return HttpResponseNotFound("Fichier PDF non trouvé.")
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Le corps de la requête doit être au format JSON.")

from django.http import Http404

class GrilleEvaluationViewSet(viewsets.ModelViewSet):
    serializer_class = GrilleEvaluationSerializer
    def get_queryset(self):
        return GrilleEvaluation.objects.all()
    
    # def perform_destroy(self, instance): 
    #     try:
    #          # Supprime la grille d'évaluation et toutes les compétences apprentis associées
    #         competences_apprentis = CompetenceApprenti.objects.filter(grilleEvaluation=instance)
    #         competences_apprentis.delete()

    #         instance.delete()
    #     except Http404:
    #         pass
    #     return Response(status=status.HTTP_204_NO_CONTENT)
    
class CompetenceApprentiViewSet(viewsets.ModelViewSet):
    serializer_class = CompetenceApprentiSerializer
    def get_queryset(self):
        return CompetenceApprenti.objects.all()