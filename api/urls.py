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
from django.conf import settings

schema_view = get_schema_view(
    openapi.Info(
        title="Projet SIGL",
        default_version='v1',),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router.register('utilisateur', UtilisateurViewSet, basename='utilisateurs')
router.register('apprenti', ApprentiViewSet, basename='apprenti')
router.register('apprentidetail', ApprentiDetailViewSet, basename='apprenti')
router.register('tuteurpedagogique', TuteurPedagogiqueViewSet, basename='utilisateurs')
router.register('tuteurpedagogiquedetail', TuteurPedagogiqueViewSet, basename='utilisateurs')
router.register('maitrealternance', MaitreAlternanceViewSet, basename='utilisateurs')
router.register('maitrealternancedetail', MaitreAlternanceViewSet, basename='utilisateurs')
router.register('coordinatricealternance', CoordinatriceAlternanceViewSet, basename='utilisateurs')
router.register('coordinatricealternancedetail', CoordinatriceAlternanceViewSet, basename='utilisateurs')
router.register('administrateur', AdministrateurViewSet, basename='utilisateurs')

urlpatterns = [
   path('', include(router.urls)),
   path('authentification/', AuthentificationUtilisateurView.as_view(), name='authentification'),
   path('docs/', schema_view.with_ui('swagger', cache_timeout=0),name='schema-swagger-ui'),

]