from django.urls import include, path

from rest_framework import routers


from api.views import UtilisateurViewSet, ApprentiViewSet, TuteurPedagogiqueViewSet, MaitreAlternanceViewSet, CoordinatriceAlternanceViewSet


router = routers.SimpleRouter()

# Puis lui déclarons une url basée sur le mot clé ‘category’ et notre view
# afin que l’url générée soit celle que nous souhaitons ‘/api/category/’

router.register('utilisateur', UtilisateurViewSet, basename='utilisateurs')
router.register('apprenti', ApprentiViewSet, basename='apprenti')
router.register('tuteurpedagogique', TuteurPedagogiqueViewSet, basename='utilisateurs')
router.register('maitrealternance', MaitreAlternanceViewSet, basename='utilisateurs')
router.register('coordinatricealternance', CoordinatriceAlternanceViewSet, basename='utilisateurs')

urlpatterns = [
   path('', include(router.urls)),
]