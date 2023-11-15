from rest_framework import status
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from api.serializers import *
from api.models import Utilisateur, TuteurPedagogique, MaitreAlternance, CoordinatriceAlternance, Apprenti

# =================== EXEMPLE =======================
# class PersonViewSet(viewsets.ModelViewSet):
#    queryset = Person.objects.all()
#    serializer_class = PersonSerializer

# =================== EXEMPLE =======================

#--- Utilisateur ---

class UtilisateurViewSet(ModelViewSet):
    serializer_class = UtilisateurSerializer

    def get_queryset(self):
        return Utilisateur.objects.all()

class AuthentificationUtilisateurView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = AuthentificationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True) :
            utilisateur = serializer.validated_data['utilisateur']
            token, created = Token.objects.get_or_create(user=utilisateur)
            return Response({'token': token.key, 'id': utilisateur.id}, status=status.HTTP_200_OK)
        return Response({}, status=status.HTTP_401_UNAUTHORIZED)

#--- TuteurPedagogique ---

class TuteurPedagogiqueViewSet(ModelViewSet):
    serializer_class = TuteurPedagogiqueSerializer
    def get_queryset(self):
        return TuteurPedagogique.objects.all()


class TuteurPedagogiqueDetailViewSet(ModelViewSet):
    serializer_class = TuteurPedagogiqueDetailSerializer
    def get_queryset(self):
        return TuteurPedagogique.objects.all()

#--- MaitreAlternance ---
class MaitreAlternanceDetailViewSet(ModelViewSet):
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

class ApprentiDetailViewSet(ReadOnlyModelViewSet):
    serializer_class = ApprentiDetailSerializer

    def get_queryset(self):
        return Apprenti.objects.all()
