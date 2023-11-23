from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticated

from api.serializers import *

from api.models import *

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from django.core import serializers as core_serializers
from rest_framework.views import APIView
import jwt, datetime

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
        print(request.data)
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
            response = Response({'jwt_token': jwt_token, 'id': utilisateur.id}, status=status.HTTP_200_OK)

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
