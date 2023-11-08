from django.urls import include, path

from rest_framework import routers

from api.views import UtilisateurViewSet

router = routers.SimpleRouter()

# Puis lui déclarons une url basée sur le mot clé ‘category’ et notre view
# afin que l’url générée soit celle que nous souhaitons ‘/api/category/’
router.register('utilisateurs', UtilisateurViewSet, basename='utilisateurs')

urlpatterns = [
   path('', include(router.urls)),
]