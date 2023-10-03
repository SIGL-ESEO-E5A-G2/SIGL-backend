from django.urls import include, path

from rest_framework import routers

from api.views import PersonViewSet, SpeciesViewSet

router = routers.DefaultRouter()
# =================== EXEMPLE =======================
router.register(r'people', PersonViewSet)
router.register(r'species', SpeciesViewSet)
# =================== EXEMPLE =======================

urlpatterns = [
   path('', include(router.urls)),
]