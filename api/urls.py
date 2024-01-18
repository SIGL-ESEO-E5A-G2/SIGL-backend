from django.urls import include, path

from rest_framework import routers

from api.views import *
router = routers.SimpleRouter()

# Puis lui déclarons une url basée sur le mot clé ‘category’ et notre view
# afin que l’url générée soit celle que nous souhaitons ‘/api/category/’

"""django_rest_swagger URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

from django.conf.urls.static import static
from rest_framework_swagger.views import get_swagger_view
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from rest_framework.authtoken.views import obtain_auth_token
from django.conf import settings

schema_view = get_schema_view(
    openapi.Info(
        title="Projet SIGL",
        default_version='v1',),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router.register('utilisateur', UtilisateurViewSet, basename='utilisateurs')
router.register('utilisateurDetail', UtilisateurDetailViewSet, basename='utilisateurs')
router.register('apprenti', ApprentiViewSet, basename='apprenti')
router.register('apprentidetail', ApprentiDetailViewSet, basename='apprentidetail')
router.register('tuteurpedagogique', TuteurPedagogiqueViewSet, basename='tuteurpedagogique')
router.register('maitrealternance', MaitreAlternanceViewSet, basename='maitrealternance')
router.register('professeur', ProfesseurViewSet, basename='professeur')
router.register('membreexterieur', MembreExterieurViewSet, basename='membreexterieur')
router.register('professeurdetail', ProfesseurDetailViewSet, basename='professeurdetail')
router.register('membreexterieurdetail', MembreExterieurDetailViewSet, basename='membreexterieurdetail')
router.register('coordinatricealternance', CoordinatriceAlternanceViewSet, basename='coordinatricealternance')
router.register('tuteurpedagogiquedetail', TuteurPedagogiqueDetailViewSet, basename='tuteurpedagogiquedetail')
router.register('maitrealternancedetail', MaitreAlternanceDetailViewSet, basename='maitrealternancedetail')
router.register('coordinatricealternance', CoordinatriceAlternanceViewSet, basename='coordinatricealternance')
router.register('coordinatricealternancedetail', CoordinatriceAlternanceDetailViewSet, basename='coordinatricealternancedetail')
router.register('administrateur', AdministrateurViewSet, basename='administrateur')
router.register('message', MessageViewSet, basename='message')
router.register('messagedetail', MessageDetailViewSet, basename='messagedetail')
router.register('messagefeed', MessageFeedViewSet, basename='messagefeed')
router.register('messageutilisateurfeed', MessageUtilisateurFeedViewSet, basename='messageutilisateurfeed')
router.register('messageutilisateurdetail', MessageUtilisateurViewSet, basename='messageutilisateurdetail')

router.register('depot', DepotViewSet, basename='depot')
router.register('depotdetail', DepotDetailViewSet, basename='depotdetail')
router.register('promotion', PromotionViewSet, basename='promotion')
router.register('apprentipromotion', ApprentiPromotionViewSet, basename='apprentipromotion')
router.register('apprentiutilisateurdetail', ApprentiUtilisateurViewSet, basename='apprentiutilisateurdetail')
router.register('maitrealternanceutilisateurdetail', MaitreAlternanceUtilisateurViewSet, basename='maitrealternanceutilisateurdetail')
router.register('tuteurpedagogiqueutilisateurdetail', TuteurPedagogiqueUtilisateurViewSet, basename='tuteurpedagogiqueutilisateurdetail')
router.register('entreprise', EntrepriseViewSet, basename='entreprise')
router.register('responsableentreprise', ResponsableEntrepriseViewSet, basename='responsableentreprise')
router.register('responsableentreprisedetail', ResponsableEntrepriseDetailViewSet, basename='responsableentreprisedetail')
router.register('tag', TagViewSet, basename='tag')
router.register('opco', OpcoViewSet, basename='opco')
router.register('evenement', EvenementViewSet, basename='evenement')
router.register('entretiensemestriel', EntretienSemestrielViewSet, basename='entretiensemestriel')
router.register('entretiensemestrieldetail', EntretienSemestrielDetailViewSet, basename='entretiensemestrieldetail')

router.register('grilleevaluation', GrilleEvaluationViewSet, basename='grilleevaluation')
router.register('competenceapprenti', CompetenceApprentiViewSet, basename='competenceapprenti')
router.register('commentaire', CommentaireViewSet, basename='commentaire')


urlpatterns = [
   path('', include(router.urls)),
   path('authentification/', AuthentificationUtilisateurView.as_view(), name='authentification'),
   path('docs/', schema_view.with_ui('swagger', cache_timeout=0),name='schema-swagger-ui'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),  # <-- And here
    path('upload-pdf/', upload_pdf_to_azure, name='upload_pdf_to_azure'),
    path('get-pdf/', get_pdf_from_azure, name='get_pdf_from_azure'),


]